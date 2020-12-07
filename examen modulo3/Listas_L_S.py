import random
import time
import json
import string

i = 0
print ("Producciendo Flores L y S")
while i<50:# modificar el numero 50 para que genere la cantidad de letras que queramos
    Flor_saliente = open("Flores_S.txt", "a")
    Flor_saliente.write(random.choice(string.ascii_lowercase)+ "\n")    
    Flor_saliente = open("Flores_L.txt", "a")
    Flor_saliente.write(random.choice(string.ascii_uppercase)+ "\n")
    time.sleep(0.1)
    i+=1