"""ramo_de_flores=["NL","2n","5k","3o","1b"]
flores_producidas_L=["4n","1b","3o","5k","5b","4h", "2u", "4n", "2n"]

a= set(ramo_de_flores)  
b= set(flores_producidas_L)

producidas= list(b-a)
enviadas= list(b&a)

print("flores_L enviadas a fabrica", enviadas)
print("Nueva lista de flores", producidas)"""

#################################################################
import random
import string
import time
from random import randrange, choice

class Proveedores():
    def __init__(self):
        pass
    def producir(self):
        i = 0
        numL = []
        while i<10:# modificar el numero 50 para quegenere la cantidad de letras
            numero_flores = random.randint(1,5)
            especie_flor=(random.choice(string.ascii_lowercase))
            flor=str(numero_flores)+ str(especie_flor)
            ########################################
            cant=numL
            cant.append(flor)
            ########################################
            Flor_saliente = open("Flores.txt", "a")
            Flor_saliente.write((flor)+ "\n")    
            time.sleep(0.01)
            i+=1
        print (numL)

producidos=Proveedores()
producidos.producir()