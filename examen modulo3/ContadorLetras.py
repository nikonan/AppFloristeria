def contarletra(string, letra):
    contador = 0
    for elemento in string:
        if elemento == letra:
            contador = contador + 1
    return contador
texto = open ("Flores_L.txt")
letra = input ("ingrese letra: ")

contador = contarletra (texto, letra)

print ("la letra", letra, "aparece", contador, "veves")


####################################################

