###################Par o impar#####################
# Luciano Ezequiel Bordon
#

def identificador_de_numeros(numero):
    if numero % 2 == 0:
        mensaje = "el numero es par"
    else:
        mensaje = "el numero es impar"
    
    return mensaje

numero = input("Ingrese Numero ")
numero = int(numero)

mensaje = identificador_de_numeros(numero)

print(mensaje)


