
import random as ra

import numpy as np
import pylab as pl
import random as ran
from tkinter import*


#Raiz
raiz=Tk()
raiz.title('Calidad de Aire')
raiz.iconbitmap('aire.ico')
raiz.geometry ('950x410')
raiz.config(bg='pink')
raiz.config(relief='sunken')

#Frame
miframe=Frame(raiz)
miframe.pack(side='right' , anchor='n')
numero=StringVar()

miframe.config(bg='purple')
miframe.config(relief='groove')
miframe.config(bd=20)

#Imagenes
img=PhotoImage(file='fotomapa.png')
miLabel=Label(raiz, image=img, fg='red')
miLabel.place(x=2, y=2)


nlabel1=Label(miframe,text= 'Prediccion')
nlabel1.grid(row=0 , column=0 , sticky='e' ,padx=5, pady=5 , columnspan=7)
nlabel2=Label(miframe,text= 'Correccion')
nlabel2.grid(row=2 , column=0 , sticky='e', padx=5, pady=5 , columnspan=7)
            
comen=Text(miframe ,width=60 , height=5)
comen.grid(row=1 , column=1 , padx=5, pady=5, columnspan=7)

comen2=Text(miframe , width=60 , height=5)
comen2.grid(row=3 , column=1 , padx=5, pady=5, columnspan=7)

NC_Int1 = IntVar()
NC_Int2 = IntVar()

nlabel1=Label(miframe,text= 'TI')
nlabel1.grid(row=4 , column=0 ,padx=2, pady=2 , columnspan=5)
ti = Entry(miframe, textvariable = NC_Int1  , width=10)
ti.grid(row=4 , column=1 , padx=2, pady=2, columnspan=5)

nlabel1=Label(miframe,text= 'TF' )
nlabel1.grid(row=4 , column=3 ,padx=2, pady=2 , columnspan=5)
tf = Entry(miframe, textvariable = NC_Int2 ,  width=10)
tf.grid(row=4 , column=4, padx=2, pady=2, columnspan=5)




def click (valor):

    
    

    numcur= NC_Int1.get()
    print("u"+str(numcur))

    numcur2= NC_Int2.get()
    print("u"+str(numcur2))
    
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
    Ti =numcur
    Tf=numcur2
        #valores para
    U=ran.sample(range(0,50),10)
        #DT
    h=ran.random()
        #Valor para C
    C= ran.randint (0,50)
    def metodoHeun (t,u,h,f,F,c):
        T=[t]
        P=[]
        C=[]
        CU=u
        for i in range (0,len(u)):
            P.append([u[i]])
            C.append([u[i]])
        for i in range (0,f):
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

    def ResultadoEcu(t,u,h,f,F,c):
        T=[t]
        U=[]
        for i in range(0,len(u)):
            U.append ([u[i]])
        for ii in range(0,f):
            T.append(T[ii]+h)
            for j in range(0,len(u)):
                CU=[]
                for data in U:
                    CU.append(data[0])
                SF=F(c,CU)
                U[j].append(U[j][ii]+h*SF[j][0])
        return U,T
    Prediccion , Correccion , TiempoH = metodoHeun ( Ti ,U ,h , Tf ,F , C )
    Resultados , Tiempo = ResultadoEcu( Ti , U ,h , Tf ,F , C )
    Max = len( Prediccion )
        
        

        
           
    print (" Metodo de Heun ")
    print ("-------------------------------------")
    print ("Parametros usados")
    print ("Tiempo inicial :"+ str(Ti))
    print ("Tiempo Final :"+str(Tf))
    print ("valores de U :"+str(U))
    print ("Constante:"+str(C))
    print ("Valores de u: \n")
    for i in range(0,Max):
        if valor-1==i:
            print (valor,i)
            print( "u"+str(i+1),"prediccion:",Prediccion[i])
            print ("u"+str(i+1),"correcion:",Correccion[i],"\n")

            
            comen=Text(miframe ,width=60 , height=5)
            comen.insert(INSERT,Prediccion[i] )
            comen.grid(row=1 , column=1 , padx=5, pady=5, columnspan=7)

            comen2=Text(miframe , width=60 , height=5)
            comen2.insert(INSERT,Correccion[i])
            comen2.grid(row=3 , column=1 , padx=5, pady=5, columnspan=7)
            
    return



boton1=Button(miframe , text='1', width=3 , command=lambda:click(1))
boton1.grid(row=5,column=1)

boton2=Button(miframe , text='2', width=3, command=lambda:click(2))
boton2.grid(row=5,column=2)

boton3=Button(miframe , text='3', width=3 , command=lambda:click(3))
boton3.grid(row=5,column=3)

boton4=Button(miframe , text='4', width=3 , command=lambda:click(4))
boton4.grid(row=5,column=4)

boton5=Button(miframe , text='5', width=3 , command=lambda:click(5))
boton5.grid(row=5,column=5)

boton6=Button(miframe , text='6', width=3 , command=lambda:click(6))
boton6.grid(row=6,column=1)

boton7=Button(miframe , text='7', width=3 , command=lambda:click(7))
boton7.grid(row=6,column=2)

boton8=Button(miframe , text='8', width=3 , command=lambda:click(8))
boton8.grid(row=6,column=3)

boton9=Button(miframe , text='9', width=3 , command=lambda:click(9))
boton9.grid(row=6,column=4)

boton10=Button(miframe , text='10', width=3 , command=lambda:click(10))
boton10.grid(row=6,column=5)





raiz.mainloop()

