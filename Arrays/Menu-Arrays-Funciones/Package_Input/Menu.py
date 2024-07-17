#menu
from Input import *
from Especificas import *
from os import system

#Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
num_ingresado = False
bandera_seguir = True
while bandera_seguir == True:

    opcion = int(input("1.Ingresar numeros\n2.Mostrar cantidad de numeros positivos y negativos\n3.Sumar numeros pares\n4.Informar el mayor de los numeros inpares\n5.Listar todos los numeros ingresados\n6.Listar todos los numeros pares\n7.Listar numeros de las posiciones impares\n8.Salir"))

    match opcion:
        case 1:
            
            lista_numeros = [0] * 10
            for i in range(len(lista_numeros)):
                numeros = get_int("ingrese numero", "reingrese numero",-1000, 1000, 5)
                lista_numeros[i] = numeros
            num_ingresado = True
            
            print(f"{lista_numeros}")
    
        case 2:
            if num_ingresado == True:
                positivo_negativo_cantidad = mostrar_cantidad_positivo_negativo(lista_numeros)

                print(f"la cantidad de numeros positivos es {positivo_negativo_cantidad[0]}, y de negativos es {positivo_negativo_cantidad[1]}")
        case 3:
            if num_ingresado == True:
                suma_pares = sumar_numeros_pares(lista_numeros)

                print(f"La suma de solo numeros pares es: {suma_pares}")
        case 4:
            if num_ingresado == True:
                numero_impar_max = informar_mayor_numero_inpar(lista_numeros)

                print(f"el numero impar mas alto ingresado es {numero_impar_max}")
        case 5:
            if num_ingresado == True:
                listar_elementos = listar(lista_numeros)
        case 6:
            if num_ingresado == True:
                listar_pares = listar_numeros_pares(lista_numeros)
        case 7:
            if num_ingresado == True:
                listar_impares = listar_numeros_impares(lista_numeros)
        case 8:
            break
    system('pause')
    system('cls')