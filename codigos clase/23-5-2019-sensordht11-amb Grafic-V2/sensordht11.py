from time import sleep
from auxfunc import grafic,lectura




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
