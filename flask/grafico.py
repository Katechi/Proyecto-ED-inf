 # procesar_csv.py  
import pylab as pl  
import csv  
 #  
entrada = open('uma_02.csv')  
tabla = []  
for fila in csv.reader(entrada):
    tabla.append(fila)
entrada.close()  
x=[0]
y=[0]
z=[0] 

for fila in range(1, len(tabla)):
    x.append(float(tabla[fila][13]))
    y.append(float(tabla[fila][2]))
    z.append(float(tabla[fila][3]))
    
print(ltln)
#print(x)

pl.plot(x,y,z)  
pl.xlabel('velocidad')  
pl.ylabel('latlong')  
pl.title('Ejemplo de grafica de un archivo csv')  
  
pl.show()  
