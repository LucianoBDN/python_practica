from Input import *
from Generales import *
from Validar_colectivos import *
import random 
from os import system


legajo = [[random.randint(1000, 9999)] for _ in range(15)]

matriz_de_recaudo = []
datos_ingresados = False
bandera_seguir = True
while bandera_seguir == True:
    opcion = int(input("1.Cargar Planilla\n2.Mostrar Recaudacion de cada coche y linea\n3.Calcular recaudacion por linea\n4.Calcular recaudacion por coche\n5.Calcular recaudacion total\n6.Salir\n"))

    match opcion:
        case 1:
            legajoz = mostrar_matriz(legajo)
            legajo_exite = False
            ingresar_legajo = get_int("ingrese su legajo", "legajo no exite intente otra vez", 1000, 9999, 5)
            legajo_exite = (validar_legajo(ingresar_legajo, legajo))
            
            if legajo_exite == False:
                print("No hemos podido encontrar su legajo")
            else:

                numero_de_linea = get_int("ingrese numero de linea", "reingrese numero de linea", 1, 3, 5)
                numero_de_coche = get_int("ingrese el numero de interno", "reingrese el numero de interno", 1, 5, 5)
                recaudacion = get_float("ingrese recaudacion","reingrese monto de recaudo", 0, 99999, 5)
                coleccion_datos = [numero_de_linea, numero_de_coche, recaudacion]
                matriz_de_recaudo.append(coleccion_datos)
                datos_ingresados = True
        case 2:
            if datos_ingresados == True:
                mostrar_recaudacion = print_matriz(matriz_de_recaudo,"De la linea", "el coche", "Recaudo un total de")
        case 3:
            if datos_ingresados == True:
                recaudacion_por_linea = sumar_recaudacion_linea(matriz_de_recaudo)
                print(f"El recaudo total de la linea 1 es de {recaudacion_por_linea[0]}\nEl recaudo total de la linea 2 es de {recaudacion_por_linea[1]}\nEl recaudo total de la linea 3 es de {recaudacion_por_linea[2]}")
        case 4:
            if datos_ingresados == True:
                recaudacion_por_coche = calcular_recaudacion_por_coches(matriz_de_recaudo)
                print(f"1 {recaudacion_por_coche[0]}, 2 {recaudacion_por_coche[1]}, 3 {recaudacion_por_coche[2]}, 4 {recaudacion_por_coche[3]}, 5 {recaudacion_por_coche[4]}")
        case 5:
            if datos_ingresados == True:
                total_recaudado = calcular_recaudacion_total(matriz_de_recaudo)
                print(f"el total recaudado es {total_recaudado}")
        case 6:
            break
    system("pause")
    system("cls")