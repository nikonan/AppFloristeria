import random
import string
import time
from random import randrange, choice

class GenerandoRamo():
    def __init__(self):
        pass
    def generar(self):
        print ("Producciendo Ramos")
        #############################
        i = 0
        while i<1:
            especie_flor=(random.choice(string.ascii_uppercase))
            tamano_flor=(choice(["S", "L"]))
            flor=str(especie_flor)+str(tamano_flor)
            Flor_saliente = open("Ramo.txt", "a")
            Flor_saliente.write((flor)+ "")
            time.sleep(0.001)
            i+=1
            print (flor)

        ############################
        i = 0
        while i<4:
            flores_ramosL=(random.choice(string.ascii_lowercase))
            cantidad_floresL = random.randint(1,5)
            numero_floresL = str(cantidad_floresL)
            Ramo=str (numero_floresL)+ str(flores_ramosL)
            Flor_saliente = open("Ramo.txt", "a")
            Flor_saliente.write((Ramo)+ "")            
            time.sleep(0.001)
            i+=1
            print (Ramo)
        
generar_ramo1=GenerandoRamo()
generar_ramo1.generar()