import time

lista = [4, 5, 3, 1, 2]


start = time.time()

print(start)

for i in range(0, len(lista)-1):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar

end = time.time()
print(end)
print(lista)
start = time.time()

print(f"Tiempo: {(end - start)*1000}")



