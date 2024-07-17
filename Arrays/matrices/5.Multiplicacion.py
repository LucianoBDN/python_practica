from os import system

def ingresar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(input(f"Ingrese un numero para la posicion {i}{j}: "))
    print("")

def multiplicar_matrices(matriz_a, matriz_b) -> list[list]:
    matriz_c = [[0] * len(matriz_b[0]) for _ in range(len(matriz_a))]
    for i in range(len(matriz_a)):
        for j in range(len(matriz_b[0])):
            for k in range(len(matriz_a[0])):
                    matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return matriz_c

def validar_multiplicacion(matriz_a, matriz_b) -> bool:
    if len(matriz_a[0]) != len(matriz_b):
        salida = False
    else:
        salida = True
    return salida

def mostrar_matriz(matriz):
     for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]:5}" , end = " ")
        print("")

#Ingreso de datos
system("cls")
F_a = int(input("Ingrese la cantidad de FILAS de la matriz (A): "))
C_a = int(input("Ingrese la cantidad de COLUMNAS de la matriz (A): "))
matriz_a = [[0]* C_a for _ in range(F_a)]
system("cls")
F_b = int(input("Ingrese la cantidad de FILAS de la matriz (B): "))
C_b = int(input("Ingrese la cantidad de COLUMNAS de la matriz (B): "))
system("cls")
matriz_b = [[0]* C_b for _ in range(F_b)]

#Validacion de matrices
while True:
    validacion = validar_multiplicacion(matriz_a, matriz_b)
    if not(validacion):
        print("---Las columnas de (A) tienen que ser iguales a las filas de (B)---\n")
        F_a = int(input("Reingrese la cantidad de FILAS de la matriz (A): "))
        C_a = int(input("Reingrese la cantidad de COLUMNAS de la matriz (A): "))
        system("cls")
        matriz_a = [[0]* C_a for _ in range(F_a)]

        F_b = int(input("Reingrese la cantidad de FILAS de la matriz (B): "))
        C_b = int(input("Reingrese la cantidad de COLUMNAS de la matriz (B): "))
        system("cls")
        matriz_b = [[0]* C_b for _ in range(F_b)]
    else:
        break

ingresar_matriz(matriz_a)
ingresar_matriz(matriz_b)

#Salida de datos
resultado = multiplicar_matrices(matriz_a, matriz_b)
mostrar_matriz(resultado)

