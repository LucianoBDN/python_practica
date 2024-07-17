matriz_a = [
    [5,3],
    [-2,9],
    [7,-4]
]

matriz_b = [
    [-2,8,5,3],
    [5,-6,7,-7]
]



multiplicar_matriz = [[0] * len(matriz_b[0]) for _ in range(len(matriz_a))]

for i in range(len(matriz_a)):
    for j in range(len(matriz_b[0])):
        for k in range(len(matriz_b)):
            multiplicar_matriz[i][j] += matriz_a[i][k] * matriz_b[k][j]
    print("")


print(multiplicar_matriz)