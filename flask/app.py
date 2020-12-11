from flask import Flask, render_template
import csv

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

def latlong (data):
    ltln = []
    for fila in range(1, len(data)):
        lat=(float(data[fila][2]))
        lon=(float(data[fila][3])) 
        ltln.append([lat,lon])
    
    return ltln
    


datos         = read_csv_file('uma_02.csv')
x,y,z,k = procesar(datos)
latlon = latlong(datos)


app = Flask(__name__)

@app.route('/')
def template():
    return render_template('index.html',x= x,y = y, z=z , k=k)

@app.route('/mapa')
def mapa():
    return render_template('mapa.html',latlon=latlon)

@app.route('/grafi')
def grafi():
    return render_template('grafi.html',latlon=latlon)

@app.route('/json', methods=['GET', 'POST'])
def parse_request():
    data = request.data 
    dataDict = json.loads(data)
    return render_template('grafi.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='127.0.0.1')
