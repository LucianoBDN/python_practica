#########################FUNCIONES#################################
# Definimos la funcion con lo que queremos que haga
def sumar_numeros_1():
    un_numero = input("ingrese un numero")
    un_numero = int(un_numero)

    otro_numero = input("ingrese un numero")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    print (f"La suma es: {suma}")

def sumar_numeros_2():
    un_numero = input("ingrese un numero")
    un_numero = int(un_numero)

    otro_numero = input("ingrese un numero")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    return suma

def sumar_numeros_3(un_numero, otro_numero):
    un_numero = input("ingrese un numero")
    un_numero = int(un_numero)

    otro_numero = input("ingrese un numero")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero


#################MAIN###############################
# El programa empezieza desde fuera de la funcion nunca inicia en la funcion
# Llamamos a la funcion para que la podamos utilizar
# print("Lucho computer programer master")
# sumar_numeros_1()
# print("aguante la delicuencia")

# resultado = sumar_numeros_2()

# # print(f"Lasuma es: {resultado}")

# if resultado > 500:
#     print("Es mayor")
# else:
#     print("Es menor")

import random

numero_1 = random.randint(1, 10)
numero_2 = random.randint(15, 300)

sumar_numeros_3(numero_1, numero_2)

    