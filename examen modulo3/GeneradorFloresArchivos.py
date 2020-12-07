import random
import time
import json
import string
class ProduciendoFlores():
    def __init__(self):
        pass
    def Producciendo(self):
        i = 0
        print ("Producciendo Flores L y S")
        while i<50:# modificar el numero 50 para quegenere la cantidad de letras
            Flor_saliente = open("Flores_S.txt", "a")
            Flor_saliente.write(random.choice(string.ascii_lowercase)+ "\n")    
            Flor_saliente = open("Flores_L.txt", "a")
            Flor_saliente.write(random.choice(string.ascii_lowercase)+ "\n")
            time.sleep(0.01)
            i+=1
        print ("Ya hay Flores")


produduciendo1=ProduciendoFlores()
produduciendo1.Producciendo()