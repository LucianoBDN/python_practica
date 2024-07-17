from empleados import *
from Input import *


def increentar_id(id)-> int:
     
     id += 1
     
     return id

def calcular_salario_promedio(lista_empleados: list[dict])-> float:

    acumulador_salarios = 0

    for empleados in lista_empleados:
        empleados['salario'] = int(empleados['salario'])
        acumulador_salarios += empleados["salario"]
    
    promedio = acumulador_salarios / len(lista_empleados)

    return promedio



def buscar_empleado(lista_empleados: list[dict])-> list[dict]:
    dni = get_int("Ingrese el dni: ", "Error reingrese dni: ",5000000, 99999999, 2)
    for empleados  in lista_empleados:
        if empleados["dni"] == dni:
            mostrar_empleado(empleados)




def ordenar_nombre_ascendente(lista_empleados: list[dict]):

    for i in range(1, len(lista_empleados)):
        key = lista_empleados[i]
        j = i - 1

        while j >= 0 and key["nombre"] < lista_empleados[j]["nombre"]:
            lista_empleados[j + 1] = lista_empleados[j]
            j -= 1
        
        lista_empleados[j + 1] = key

    return lista_empleados


def ordenar_nombre_decendente(lista_empleados: list[dict])-> list[dict]:
    for i in range(1, len(lista_empleados)):
            key = lista_empleados[i]
            j = i - 1

            while j >= 0 and key["nombre"] > lista_empleados[j]["nombre"]:
                lista_empleados[j + 1] = lista_empleados[j]
                j -= 1
            
            lista_empleados[j + 1] = key

    return lista_empleados

def ordenar_apellido_ascendente(lista_empleados: list[dict])-> list[dict]:
    for i in range(1, len(lista_empleados)):
            key = lista_empleados[i]
            j = i - 1

            while j >= 0 and key["apellido"] < lista_empleados[j]["apellido"]:
                lista_empleados[j + 1] = lista_empleados[j]
                j -= 1
            
            lista_empleados[j + 1] = key

    return lista_empleados

def ordenar_apellido_decendente(lista_empleados: list[dict])-> list[dict]:
    for i in range(1, len(lista_empleados)):
            key = lista_empleados[i]
            j = i - 1

            while j >= 0 and key["apellido"] > lista_empleados[j]["apellido"]:
                lista_empleados[j + 1] = lista_empleados[j]
                j -= 1
            
            lista_empleados[j + 1] = key

    return lista_empleados

def ordenar_salario_ascendente(lista_empleados: list[dict])-> list[dict]:
    for i in range(1, len(lista_empleados)):
            key = lista_empleados[i]
            j = i - 1

            while j >= 0 and key["salario"] < lista_empleados[j]["salario"]:
                lista_empleados[j + 1] = lista_empleados[j]
                j -= 1
            
            lista_empleados[j + 1] = key

    return lista_empleados

def ordenar_salario_decendente(lista_empleados: list[dict])-> list[dict]:
    for i in range(1, len(lista_empleados)):
            key = lista_empleados[i]
            j = i - 1

            while j >= 0 and key["salario"] > lista_empleados[j]["salario"]:
                lista_empleados[j + 1] = lista_empleados[j]
                j -= 1
            
            lista_empleados[j + 1] = key

    return lista_empleados

#######################################################################################################

def menu_opciones_ordenamiento(lista_empleados)-> list[dict]:
    try:
        opcion = input("Desea ordenar por\nA. Nombre asecendiente\nB. Nombre descendiente\nC. Apellido ascendiente\nD. Apellido descendiente\nE. Salario ascendiente\nF. Salario descendiente\nG. Salir\n Elija una opcion: ")
        opcion.lower()
        match opcion:
                case "a":
                    lista_ordenada = ordenar_nombre_ascendente(lista_empleados)

                case "b":
                    lista_ordenada = ordenar_nombre_decendente(lista_empleados)

                case "c":
                    lista_ordenada = ordenar_apellido_ascendente(lista_empleados)

                case "d":
                    lista_ordenada = ordenar_apellido_decendente(lista_empleados)

                case "e":
                    lista_ordenada = ordenar_salario_ascendente(lista_empleados)

                case "f":
                    lista_ordenada = ordenar_salario_decendente(lista_empleados)

                case "g":
                    pass
    except:
         print("opcion no valida, ingrese otra opcion")
    return lista_ordenada