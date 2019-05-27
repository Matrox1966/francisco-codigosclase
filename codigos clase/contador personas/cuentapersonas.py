from graficar import grafic
from random import randint
from time import sleep

def distancia():
    #codi del del sensor suggerida per velleman
    distancia = randint(0,1)
    return distancia


numeropersonas=[]
minutos=0
while minutos<10:
    contador=0
    for segundos in range(60):
        contador += distancia()
        sleep (1)
    numeropersonas.append(contador)
    minutos+=1
    print (numeropersonas)     
grafic(numeropersonas)   
