from flask import Flask, render_template
import csv
import random as ra

import numpy as np
import pylab as pl
import random as ran
import json

from flask import request

def read_csv_file(filename):
    data = []
    for row in csv.reader(open(filename)):
        data.append(row)
    #print (data)
    return data

def procesar (data):
    x=[0]
    y=[0]
    z=[0] 
    k=[0] 
    for fila in range(1, len(data)):
        x.append(float(data[fila][5]))
        y.append(float(data[fila][6]))
        z.append(float(data[fila][7]))
        k.append(float(data[fila][13]))
    #print (y)
    return x,y,z ,k




#Pruebas con datos y parametros
datos         = read_csv_file('uma_02.csv')

x,y,z,k = procesar(datos)



app = Flask(__name__)

@app.route('/')
def template():
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/map')
def map():
    return render_template('mapa2.html')

@app.route('/mapa2',methods=['POST'])
def mapa2():
    e=request.form.get("e")
    ide=int(e)
    def latlong (data):
        ltln = []
        for fila in range(1, len(data)):
            if fila == ide : 
                print (fila)
                lat=(float(data[fila][2]))
                lon=(float(data[fila][3])) 
                ltln.append([lat,lon])
        return ltln
    datos2         = read_csv_file('ruta.csv')
    latlon = latlong(datos2)

    return render_template('mapa2.html',latlon=latlon)


@app.route('/grafi')
def grafi():
    return render_template('grafi.html',x= x,y = y, z=z , k=k)

@app.route('/simu')
def simu():
    return render_template('simulador.html')

    #return render_template('simulador.html',Prediccion=Prediccion,Correccion=Correccion)

#Simulacion 
@app.route("/simu2",methods=['POST'])
def simu2():
    zona=request.form.get("zona")
    t_1=request.form.get("t1")
    t_2=request.form.get("t2") 
    zon=int(zona)
    t1=int(t_1) 
    t2=int(t_2) 
    F = lambda c,u :[
            [c*(u[1]+u[2]+u[9]-3*u[0])] ,        #u1
            [c*(u[0]+u[2]+u[9]-3*u[1])] ,        #u2
            [c*(u[0]+u[1]+u[3]-3*u[2])] ,        #u3
            [c*(u[2]+u[4]+u[5]-3*u[3])] ,        #u4
            [c*(u[3]+u[5]-2*u[4])]      ,        #u5
            [c*(u[3]+u[4]+u[6]-3*u[5])] ,        #u6
            [c*(u[5]+u[7]+u[8]-3*u[6])] ,        #u7
            [c*(u[6]+u[8]-2*u[7])]      ,        #u8
            [c*(u[6]+u[7]+u[9]-3*u[8])] ,        #u9
            [c*(u[1]+u[0]+u[8]-3*u[9])]         #u10
             ]
     

    Ti =t1
    Tf= t2
        #valores para
    U=ran.sample(range(0,50),10)
        #DT
    h=ran.random()
        #Valor para C
    C= ran.randint (0,50)
    def metodoHeun (t,u,h,Tf,F,c):
        T=[t]
        P=[]
        C=[]
        CU=u
        for i in range (0,len(u)):
            P.append([u[i]])
            C.append([u[i]])
        for i in range (0,Tf):
            T.append(T[i]+h)
            for j in range (0,len(u)):
                SF = F(c,CU)
                DT = T[i+1]-T[i]
                P[j].append (P[j][i]+ ((SF[j][0])* DT))
                CUP=[]
                for data in P:
                    CUP.append (data[i])
                SFP= F(c,CUP)
                C[j].append(C[j][i]+((SFP [j][0] +SF [j][0])/2)*DT)
        return P,C,T

    Prediccion , Correccion , TiempoH = metodoHeun ( Ti ,U ,h , Tf ,F , C )
    Max = len( Prediccion )
    for i in range(0,Max):
        if zon-1==i:
            print (zon,i)
            print( "u"+str(i+1),"prediccion:",Prediccion[i])
            print ("u"+str(i+1),"correcion:",Correccion[i],"\n")
 
    
    return render_template('simulador.html', Prediccion=Prediccion[zon-1] , Correccion=Correccion[zon-1])


"""@app.route('/json', methods=['GET', 'POST'])
def parse_request():
    data = request.data 
    dataDict = json.loads(data)
    return render_template('grafi.html')
"""

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='127.0.0.1')
