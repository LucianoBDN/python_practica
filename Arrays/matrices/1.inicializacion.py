matriz = [
    [4,7,9],
    [7,9,8],
    [1,9,3],
    [4,3,7]
]

# rango M 4x3

for i in range(len(matriz)):#FILAS
   
    for j in range(len(matriz[i])):# COLUMNAS
        print(f"{matriz[i][j]}", end = f" ")
    print("")

