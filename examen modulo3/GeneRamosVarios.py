import random
import string
import time
from random import randrange, choice




class GenerandoRamo():
    def __init__(self):
        pass
    def generar(self):
        print ("Producciendo Ramos")
        i = 0
        while i<4:
            flores_ramosL=(random.choice(string.ascii_lowercase))
            cantidad_floresL = random.randint(1,5)
            numero_floresL = str(cantidad_floresL)
            RamoL=str (numero_floresL)+ str(flores_ramosL)
            Ramo_salienteL = open("Ramo_L.txt", "a")
            Ramo_salienteL.write((RamoL)+ "")
            flores_ramosS=(random.choice(string.ascii_lowercase))
            cantidad_floresS = random.randint(1,5)
            numero_floresS = str(cantidad_floresS)
            RamoS=str (numero_floresS)+ str(flores_ramosS)
            Ramo_salienteS = open("Ramo_S.txt", "a")
            Ramo_salienteS.write((RamoS)+ "")  
            time.sleep(0.001)
            i+=1
        print ("Ramos Producidos")

generar_ramo1=GenerandoRamo()
generar_ramo1.generar()
##################################
'''class GenerarInicial:
    def __init__(self):
        pass
    def produciendo_inicial(self):
        print ("Iniciales Ramo")
        i = 0
        indiceramo = []
        while i<1:
            letra_inicial=(random.choice(string.ascii_uppercase))
            tamano_ramo=(choice(["S", "L"]))
            flor=str(letra_inicial)+str(tamano_ramo)
            indice= indiceramo
            indice.append(flor)
            i+=1
            print (indiceramo) 

producir_Inicial=GenerarInicial()
producir_Inicial.produciendo_inicial()
################################

class GenerandoRamo():
    def __init__(self):
        pass
    def generar(self):
        print ("Producciendo Ramos")
        ramo_L=[] 
        #indiceramo=[]
        #ramo_L[:0]= indiceramo     
        i = 0
        while i<4:
            flores_ramos=(random.choice(string.ascii_lowercase))
            cantidad_flores = random.randint(1,5)
            numero_flores = str(cantidad_flores)
            #tamano_flor=(choice(["S", "L"]))
            Ramo= str (numero_flores)+ str(flores_ramos)#+str(tamano_flor)
            Ramo_saliente = ramo_L
            Ramo_saliente.append(Ramo)   
            time.sleep(0.001)
            i+=1

        print (ramo_L)
        
ramo1=GenerandoRamo()
ramo1.generar()
print (ramo1.generar)'''

##########################################################################
#***************** GENERADOR DE RAMO ARCHIVO Y LISTA ********************#
##########################################################################
class GenerandoRamo():
    def __init__(self):
        pass
    def generar(self):
        #print ("Producciendo Ramos")
        i = 0
        indiceramo = []
        while i<1:
            especie_flor=(random.choice(string.ascii_uppercase))
            tamano_flor=(choice(["S", "L"]))
            flor=str(especie_flor)+str(tamano_flor)
            ############################
            indice= indiceramo
            indice.append(flor)
            ###########################
            Flor_saliente = open("Ramo.txt", "a")
            Flor_saliente.write((flor)+ "")
            time.sleep(0.001)
            i+=1
            #print (flor)

        ############################
        ramo_L=[] 
        ramo_L[:0]= indiceramo
        i = 0
        while i<4:
            flores_ramosL=(random.choice(string.ascii_lowercase))
            cantidad_floresL = random.randint(1,5)
            numero_floresL = str(cantidad_floresL)
            Ramo=str (numero_floresL)+ str(flores_ramosL)
            ###########################
            Ramo_saliente = ramo_L
            Ramo_saliente.append(Ramo)
            ##########################
            Flor_saliente = open("Ramo.txt", "a")
            Flor_saliente.write((Ramo)+ "")            
            time.sleep(0.001)
            i+=1
        print (ramo_L)
        

generar_ramo1=GenerandoRamo()
#generar_ramo1.generar() 

##########################################################################
#*********************** FIN GENERADOR DE RAMO **************************#
##########################################################################