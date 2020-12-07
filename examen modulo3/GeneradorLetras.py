import random
import string
import time
from random import randrange, choice

class ProducirFlores:
    def __init__(self):
        pass
    def produciendo(self, cantidad):
        print ("Producciendo Flores")
        i = 0
        while i<cantidad:
            especie_flor=(random.choice(string.ascii_uppercase))
            # lowercase: Minusculas
            # letters: Minusculas y Mayusculas
            # uppercase: Mayusculas
            tamano_flor=(choice(["S", "L"]))
            flor=str(especie_flor)+str(tamano_flor)
            Flor_saliente = open("Flores.txt", "a")
            Flor_saliente.write((flor)+ "\n")    
            time.sleep(0.001)
            i+=1
        print ("Ya hay Flores")

producir_flores=ProducirFlores()
producir_flores.produciendo(10)



