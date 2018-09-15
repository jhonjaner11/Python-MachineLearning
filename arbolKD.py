# Abre archivo en modo lectura
import numpy as np   
archivo = open('prueba.txt','r')

# Lee todas la líneas y asigna a lista
lista = archivo.readlines()  
np.sujeto = []
np.migente= []
migente2=[]


#print (sujeto[len(sujeto)-1]) hallar el ultimo valor que es la clasificacion
# Inicializa un contador
numlin = 0  

# Recorre todas los elementos de la lista
for linea in lista:

    # incrementa en 1 el contador  
  	#  sujeto=linea.split() 
  	sujeto=np.loadtxt(linea)


    migente.append(sujeto)


    #migente2.append(np.loadtxt(linea))

    # muestra contador y elemento (línea)





#migente.sort()

print (migente)


archivo.close  # cierra archivo