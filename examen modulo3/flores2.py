from os import times
import random
import string
from random import randrange, choice
from typing import Text

class BodegaFlores(object):
    def __init__(self,florn):
        self.__nombre_archivo_S ="inventario_S.txt"
        self.__nombre_archivo_L ="inventario_L.txt"
        self.tamano_flor=tamano_flor
    
    def agregar_elemento(self, florn):
        if self.tamano_flor == "S":
            with open(self.__nombre_archivo_S, 'a') as file:
                file.write(florn+"\n")
        if self.tamano_flor == "L":
            with open(self.__nombre_archivo_L, 'a') as file:
                file.write(florn+"\n")
    
    def dejar_a_listaS():
        with open('inventario_S.txt','r') as stop_words: 
            lineasS = [linea.strip() for linea in stop_words]
        #print(lineasS)
        return lineasS

    def dejar_a_listaL():
        with open('inventario_L.txt','r') as stop_words: 
            lineasL = [linea.strip() for linea in stop_words]
        #print(lineasL)
        return lineasL

#Eliminar flor de inventario para armar el ramo
class buscar_flor_en_lista():
    def __init__(self):
        self.tipo_flor_S=str(input("que flor necesita en chicas: "))
        self.tipo_flor_L=str(input("que flor necesita en grandes: "))

        self.__Eliminar_flor_de_inventarioS()
        self.__Eliminar_flor_de_inventarioL()

    def __Eliminar_flor_de_inventarioS(self):
        with open('inventario_S.txt','r') as stop_words: 
            lineasS = [linea.strip() for linea in stop_words]
        flor_tipo_contars=lineasS.count(self.tipo_flor_S)
        if flor_tipo_contars>=1:
            lineasS.remove(self.tipo_flor_S)
            fic = open("inventario_S.txt", "w")
            for line in lineasS:
                fic.write(line)
                fic.write("\n")
            fic.close()   

    def __Eliminar_flor_de_inventarioL(self):
        with open('inventario_L.txt','r') as stop_words: 
            lineasL = [linea.strip() for linea in stop_words]
        flor_tipo_contarL=lineasL.count(self.tipo_flor_L)
        if flor_tipo_contarL>=1:
            lineasL.remove(self.tipo_flor_L)
            ficL = open("inventario_L.txt", "w")
            for line in lineasL:
                ficL.write(line)
                ficL.write("\n")
            ficL.close()

class Ramosolicitado():
    def __init__(self):
        self.__ListaRamo={'Tipo':'A','Tamano':'J','a':2, 'b':4} #ramo solicitado
        self.__Tipo_de_Ramo()

    def __Tipo_de_Ramo(self):
        self.valorTipoRamo = self.__ListaRamo.pop('Tipo') #valorTipoRamo
        self.valorTamanoRamo = self.__ListaRamo.pop('Tamano') #valorTamanoRamo
        print('valorTipoRamo: ', self.valorTipoRamo)
        #si el ramo es grande:
        if self.valorTamanoRamo =='J':
            for flores in self.__ListaRamo:
                    print(flores)#caracter de lista la cual quitar
                    print(self.__ListaRamo[flores])#numero de veces para quitar flores de inventario L

Flor2 =Ramosolicitado()

#lista=['AJ','16s','5p', '4a']
#Tipo_Tamaño=lista[0]
#lista.remove(Tipo_Tamaño)
#
#for element in lista:
#    for i in element:
#        print(i)
#
#    print(element)


for i in range(10):
    cantidad_flor=random.randint(1,5)
    especie_flor=(random.choice(string.ascii_lowercase))
    tamano_flor=(choice(["S", "L"]))
    formato2=str(cantidad_flor)+str(especie_flor)
    flor=str(especie_flor)+str(tamano_flor)
    #print("Tipo de Flor:",flor)

    Flor1 = BodegaFlores(tamano_flor)
    Flor1.agregar_elemento(formato2)#especie_flor


