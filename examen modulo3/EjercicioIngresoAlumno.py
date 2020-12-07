import time
global lista
lista = list()

# defino los atributos de floristeria

class Floristeria:
    #def __init__ (self, rut, nombre, sucursal):
        rut = ""
        nombre= ""
        sucursal = 0




def menu (self):
    op = 0
    while op != 4:
        #mostrar el menu
        print ("Menu Floristeria")
        print ("1. - Registrar Floristeria")
        print ("2. - Listar Floristeria")
        print ("3. - Buscar Floristeria")
        print ("4. - Salir de Floristeria")
        op = input ("Digite Opcion:")

        if op == 1:
            self.registrarFloristeria()
        elif op == 2:
            self.listarFloristeria()
        elif op == 3:
            self.buscarFloristeria()
        elif op == 4:
            self.salir()
        time.sleep(0.1)
        
def registrarFloristeria(self):
    print ("Registro de Floristeria")

def listarFloristeria(self):
    print ("Lista de Floristerias")

def buscarFloristeria(self):
    print ("Buscar Floristeria")

def salir(self):
    print ("Gracias por Utilizar la Aplicacion")
        
menu("")