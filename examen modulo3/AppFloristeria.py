import random
import string
import time
from random import randrange, choice

##########################################################################
#************ PROVEEDORES PRODUCIR FLORES ARCHIVO Y LISTA ***************#
##########################################################################
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
        #print (numL)
        return numL

producidos=Proveedores()
#producidos.producir()
##########################################################################
#********** FIN PROVEEDORES PRODUCIR FLORES ARCHIVO Y LISTA *************#
##########################################################################

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

##########################################################################
# MENU*********MENU*********MENU*********MENU**********MENU*********MENU #
##########################################################################
opcion = 0

def menu():
    opc = int(input("**************************\n" +
                    "|| Menu App Floristeria || \n" +
                    "**************************\n" +
                    "1. Iniciar Fabrica y ver flores de Proveedores \n" +
                    "2. Generar Ramos a Fabricar \n" +
                    "3. Ver Ramo Generado \n" +
                    "4. Enviar Peticion de Materiales \n" +
                    "5. Ver Stock Proveedores \n" +
                    "6. Revisar Stock de Ramos Fabricados \n" +
                    "Elija una Opcion :) \n")) 
    return opc

while opcion != 6:
    opcion = menu()
    if opcion == 1:
        print ("************************************************")
        print (producidos.producir(),"\nEste es el stock de los Proveedores\n" + 
                "Se entregan por cantidad de flores especifico")
        print ("************************************************")

    if opcion == 2:
        print ("************************************************")
        print ("Nuevo Diseño de Ramo en Creacion")
        print ("************************************************")
         
    if opcion == 3:             
        print ("************************************************")
        print ("Este es el nuevo Ramo Diseñado:", generar_ramo1.generar())
        print ("************************************************")
              
            
    if opcion == 4:
        print ("************************************************")
        input ("Los Materiales se han Pedido")
        print ("************************************************")
        
    if opcion == 5:
        print ("************************************************")
        print("Este es el Stock de Proveedores")
        print ("************************************************")
        
    if opcion == 6:
        print ("************************************************") 
        print("Este es el Stock de Ramos Fabricados")
        print ("************************************************")
        
    if opcion > 6:
        print ("************************************************")
        print("opcion invalida") 
        print ("************************************************")
##########################################################################
# MENU*********MENU*********MENU*********MENU**********MENU*********MENU #
##########################################################################




