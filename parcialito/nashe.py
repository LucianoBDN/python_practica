'''vector = [3,8,14,7]

for i in range(1, len(vector)):
    for j in range(i, len(vector)-1):falta agregarle el + 1 para que empiece de una posicion mas adelante
        if vector[i] == vector[j]: #aca compara si los valores son iguales y no cual es mayor o menor
            vector[j] = auxiliar   #auxiliar no esta definido desde un principio ya que intentamos darle un valor a algo que no existe
            auxiliar = vector[j]
            vector[i] = auxiliar'''


vector = [3,8,14,7]

#el for i recorre la lista desde la posicion 0 a una anterior del final (creo)
for i in range(0, len(vector)-1):
    #el for j desde una posicion mas adelante recorre el len de la lista desde la posicion 0 
    for j in range(i + 1, len(vector)):
        #preguntamos si el numero de la posicion es mayor o menor
        if vector[i] > vector[j]:
            #declaramos la variable auxiliar para guardar el valor
            auxiliar = vector[i]
            #hacemos el cambio
            vector[i] = vector[j]
            #cambiamos el valor de j por lo que guardamos en el auxiliar
            vector[j] = auxiliar

print(vector)
