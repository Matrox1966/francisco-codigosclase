from random import randrange
from time import sleep
from graficar import grafic


def lectura():
    #codi del del sensor dht11 velleman temperatura i humitat
    temperatura = randrange(10,35)
    humitat = randrange(50,100)
    return temperatura,humitat



#codi principal

#faig una crida a la funcio distancia

comptador  = 0

temperatura=[]
humitat=[]
while True:
    valors =lectura()
    temperatura.append(valors[0])
    humitat.append(valors[1])
    print(valors,temperatura,humitat)
    comptador += 1 # comptador = comptador +  1
    if comptador == 10:
        grafic(temperatura, humitat) # ara mateix te 10 valors
        comptador = 0
        temperatura=[]
        humitat=[]
     
    sleep(1)
