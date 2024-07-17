matriz_a = [  [4,7,9],
              [7,9,8],
              [1,9,3],]

matriz_b = [  [5,7,1,6],
              [1,3,4,6],
              ]

escalar = 5

matriz_suma = [[0] * len(matriz_a[0]) for _ in  range(len(matriz_a))]

for i in range(len(matriz_suma)):
    for j in range(len(matriz_suma[0])):
        matriz_suma[i][j] = matriz_a[i][j] + matriz_b[i][j]

for i in range(len(matriz_suma)):
    for j in range(len(matriz_suma[0])):
        print(f"{matriz_suma[i][j]:5}", end="")

    print("")