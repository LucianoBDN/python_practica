
# diccionario =[
#     {"dni": 2,"nombre":"Lucho","apellido": "Bordon","nota": 9},
#     {"dni": 1,"nombre":"Marcos","apellido": "Perez","nota": 7},
#     {"dni": 6,"nombre":"Pedro","apellido": "Caniggia","nota": 4},
#     {"dni": 6,"nombre":"Manso","apellido": "Cachondo","nota": 2},
# ]

# eliminar_alumno(diccionario, 1)
# mostrar_todos_los_alumnos(diccionario)

from Alumno import *
from os import system

def mostrar_menu():
    opcion = input("MENU\n1. Cargar\n2. Modificar\n3. Eliminar\n4. Mostrar\n5. Salir\nElija una opcion\n")
    opcion = int(opcion)
    return opcion
#################################################

lista_alumnos = [
     {"dni": 2334152,"nombre":"Lucho","apellido": "Bordon","nota": 9},
     {"dni": 1321432,"nombre":"Marcos","apellido": "Perez","nota": 7},
     {"dni": 6421432,"nombre":"Pedro","apellido": "Caniggia","nota": 4},
     {"dni": 6412432,"nombre":"Manso","apellido": "Cachondo","nota": 2}
]
system('cls')
while True:
    menu = mostrar_menu()
    match menu:
        case 1:
            agregar_alumno_lista(lista_alumnos)
        case 2:
            dni = int(input("Ingrese el dni: "))
            modificar_alumno(lista_alumnos, dni)
        case 3:
            dni = int(input("Ingrese el dni: "))
            eliminar_alumno(lista_alumnos, dni)
        case 4:
            mostrar_todos_los_alumnos(lista_alumnos)
        case 5:
            break
    system('pause')
    system('cls')