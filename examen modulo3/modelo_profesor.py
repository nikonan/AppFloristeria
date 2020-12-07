class Inventario(object):
    def __init__(self, nombre, nombre_archivo):
        self.nombre = nombre
        self.nombre_archivo = nombre_archivo
        self.elemtos = []
    
    def __crear_archivos(self):
        pass
    
    def apend(self):
        pass
    
    def pop(seldf):
        pass
    
    def contenidos(self):
        pass
    
    def vaciar(self):
        pass
    
    def guardar(self):
        pass

class InventarioRamos(Inventario):
    def __init__(self, nombre, nombre_archivo):
        super().__init__(nombre, nombre_archivo)
    
    def obtener_ramos(self, rango_fechas):
        pass

class InventarioTipoRamos(Inventario):
    def __init__(self, nombre, nombre_archivo):
        super().__init__(nombre, nombre_archivo)
    
    def tipos_de_flores_en_usos(self):
        pass

class InventarioFlores(Inventario):
    def __init__(self, nombre, nombre_achivo):
        super().__init__()

    def append(sef, tipos_ramos):
        pass
    
    def extraer_flor(self, nombre, tamano):
        pass

    def inventario(self): #dict
        pass

class Flor:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
    def despachar(self):
        pass

class TipoRamo:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
        self.sec_base = sec_base
        self.largo_sec_extra = largo_sec_extra
    def genera_sec_extra(self):
        pass


class Ramo(TipoRamo):
    def __init__(self):
        self.sec_extra = __genera_sec_extra(self)
        self.ramo
        self.fecha_hora = __genera_fecha_hora(self)

    def despachar():
        pass

    def __genera_sec_extra(self):
        pass

    def __genera_fecha_hora(self):
        pass


class FabricadorRamos():
    def __init__(self):
        pass
    def generar_ramo(self):
        pass
    def despachar_ramo(self):
        pass

class AbastecedorFlores():
    def __init__(self):
        pass
    def generar_flor(self):
        pass
    def abastece__flor(self):
        pass

#Programa Principal
bodega_flores_disponibles = InventarioFlores("inventario", "inventario_L")#instancia
tipos_de_ramos_en_fabricacion = InventarioTipoRamos()#instancia
bodega_ramos_ya_fabricados = InventarioRamos()#instancia
jefe_de_compra_de_flores = AbastecedorFlores(bodega_flores_disponibles, tipos_de_ramos_en_fabricacion)
jefe_de_produccion = FabricadorRamos(bodega_flores_disponibles, tipos_de_ramos_en_fabricacion, bodega_ramos_ya_fabricados)

while True:
    flor_a_agregar = jefe_de_compra_de_flores.generar_flor(tipos_de_ramos_en_fabricacion)
    jefe_de_compra_de_flores.abastece__flor(flor_a_agregar) #bodega recibio flor nueva

    if jefe_de_compra_de_flores() == True:
        ramo = jefe_de_produccion.generar_ramo()
        jefe_de_produccion.despachar_ramo()
