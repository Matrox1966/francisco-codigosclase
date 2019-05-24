import cayenne.client
from random import randint
from time import sleep



def distancia():
    #codi del del sensor suggerida per velleman
    distancia = randint(0,1)
    return distancia
def cayene(contador):
    client.virtualWrite(1,contador)
    


# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME = "f241fde0-7c80-11e9-b4eb-6bf2c2412b24"
MQTT_PASSWORD = "937facc0ce1cc7a7193e58ae8f01d1a540192bc7"
MQTT_CLIENT_ID = "db0cd670-7e17-11e9-94e9-493d67fd755e"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)


while True:
    client.loop()
    contador=0
    for segundos in range(60):
        contador += distancia()
        sleep(1)
        
    cayene(contador)     
    print (contador)    









