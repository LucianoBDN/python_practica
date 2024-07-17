'''Crear una función que reciba como parámetros una lista de números y el path de un archivo. La misma deberá guardar la lista en un archivo de texto.
'''


def guardar_numeros_archivo(lista_numeros: list, path_archivo: str) :

    with open(path_archivo, "w") as archivo:
        for numero in lista_numeros:
            archivo.write(f"{numero}\n")

    return archivo


def multiplos_de_dos(path_archivo: str):
    with open(path_archivo, "r") as archivo:
        for linea in archivo:
            numero = int(linea.strip())
            if numero % 2 == 0:
                print(numero)


lista_numeros= [1,2,3,4,5,6,7,8]

path = r"E:\Programacion_1\CRUD\Ejercicio_archivos\lista_numeros.txt"

lista_numeros_en_archivo = guardar_numeros_archivo(lista_numeros,path)


multiplos = multiplos_de_dos(path)
