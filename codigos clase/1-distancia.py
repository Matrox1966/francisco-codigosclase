from random import randrange
from time import sleep

'''
 import    de les llibreries especificçqyes del sensor de distancia
que fem servir com a comptapersones
import dv345

'''

def grafica(llista):
    # amb matplotlib.pyplot graficarem les dates
    pass

def distancia():
    #codi del del sensor suggerida per velleman
    distancia = randrange(0,4)
    return distancia



#codi principal

#faig una crida a la funcio distancia

comptador  = 0

buleana = True

llista=[]

while buleana:
    llista.append(distancia())
    comptador += 1 # comptador = comptador +  1
    if comptador == 10:
        print(llista)
        grafica(llista) # ara mateix te 10 valors
        comptador = 0
        llista = []
    sleep(1)
