

print ("\n1-Mostrar ramos s", "\n2-Actualizar ramos s", "\n3-Mostrar ramos L", "\n4-Actualizar ramos L", "\n3-Salir")

opcion = input("Elije una opcion: ")

if opcion == "1":
    print ("Mostrar Ramos s\n")
    archivo = open ("prueba/ramo_s.txt")
    arch = archivo.readlines()
    archivo.close()
    print(arch)

elif opcion == "2":
    print ("Actualizar Ramos s\n")
    archivo = open ("prueba/ramo_s.txt", "a" )
    arch = archivo.write()
    archivo.close()
    print(arch)


elif opcion == "3":
    print ("Mostrar Ramos L\n")
    archivo = open ("prueba/ramo_L.txt")
    arch = archivo.readlines()
    archivo.close()
    print(arch)

elif opcion == "4":
    print ("Actualizar Ramos L\n")
    archivo = open ("prueba/ramo_L.txt")
    arch = archivo.readlines()
    archivo.close()
    print(arch)


elif opcion == "3":
    print ("desea cerrar la vista")
    archivo.close()


