import random
import string
import time
from random import randrange, choice

class GenerandoRamo():
    def __init__(self):
        pass
    def generar(self):
        print ("Generando Formato")
        i = 0
        indiceramo = []
        while i<1:
            letra_inicial=(random.choice(string.ascii_uppercase))
            tamano_ramo=(choice(["S", "L"]))
            inicial=str(letra_inicial)+str(tamano_ramo)
            indice= indiceramo
            indice.append(inicial)
            time.sleep(0.001)
            i+=1
        ###################
        ramo_L=[] 
        ramo_L[:0]= indiceramo     
        i = 0        
        while i<4:
            flores_ramos=(random.choice(string.ascii_lowercase))
            cantidad_flores = random.randint(1,5)
            numero_flores = str(cantidad_flores)
            Ramo= str (numero_flores)+ str(flores_ramos)
            Ramo_saliente = ramo_L
            Ramo_saliente.append(Ramo)   
            time.sleep(0.001)
            i+=1
        print (ramo_L)
        print ("Formato Generado")

ramo1=GenerandoRamo()
ramo1.generar()