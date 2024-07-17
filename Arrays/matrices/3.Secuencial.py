matriz = [[0]* 3 for _ in range(4)] 


M = len(matriz)
N = len(matriz[0])

for i in range(M):
    for j in range(N):
        matriz[i][j] = int(input("ingrese un numero: "))

for i in range(M):#FILAS
   
    for j in range(N):# COLUMNAS
        print(f"{matriz[i][j]:5}", end = f" ")
    print("")




print(matriz)