#Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.

# def calcular_promedio_lista(mi_lista):

#     for i in range(len(mi_lista)):
#         enteros = input(f"Ingrese el número {i+1}: ")
#         enteros = int(enteros)
#         mi_lista[i] = enteros

#         seguir = input("desea seguir si/no)")

#         if seguir == "no":
#             break


#     suma_total = sum(mi_lista)

#     promedio = suma_total / len(mi_lista)

#     return promedio

# mi_lista = [0] * 5

# promedio_total = calcular_promedio_lista(mi_lista)

# print(f"el promedio de todos los numeros de la lista es {promedio_total}")

#Calcular Promedio


def calcular_promedio(lista : list) -> float:
    suma_total = 0

    for i in range(len(lista)):

        suma_total += lista[i]

    promedio = suma_total / len(lista)

    return promedio

# lista = [10,15,20,25,30]

# promedio_total = calcular_promedio(lista)

# print(f"el promedio de todos los numeros de la lista es {promedio_total}")

#calcular promedio de positivos

def calcular_promedio_positivo(lista : list) -> float:
    suma_total = 0
    positivo = 0

    for i in range(len(lista)):

        if lista[i] > 0:
            suma_total += lista[i]
            positivo += 1
    if positivo > 0:
        promedio = suma_total / positivo
    else:
        promedio = 0

    return promedio

# lista =  [36, -72, 15, -91, 20]

# promedio_positivo = calcular_promedio_positivo(lista)

# print(f"el promedio de todos los numeros de la lista es {promedio_positivo}")


# calcular producto


def calcular_producto(lista:list) -> int:

    producto_toal = 1

    for i in range(len(lista)):

        producto_toal *= lista[i]

    return producto_toal

# lista = [36, 72, 15, 91, 20]

# producto_total = calcular_producto(lista)

# print(f"El producto de la multiplicacion de los elementos es {producto_total}")


def buscar_posicion_num_max(lista:list) -> int:

    valor_max = lista[0]
    posicion_valor_max = 0

    for i in range(len(lista)):

       if lista[i] >= valor_max:
            valor_max = lista[i]
            posicion_valor_max = i



    return posicion_valor_max


# lista = [36, 72, 15, 110, 110]


# posicion_maximo = buscar_posicion_num_max(lista)
# print(f"la posicion del numero maximo es {posicion_maximo}")

def buscar_valores_maximos(lista: list) -> list:
    valor_max = lista[0]
    posicion_valor_max = []
    for i in range(len(lista)):
        if lista[i] > valor_max:
            valor_max = lista[i]
            posicion_valor_max = [i]
        elif lista[i] == valor_max:
            posicion_valor_max = posicion_valor_max + [i]

    return posicion_valor_max

lista = [110, 110, 110, 110, 110]
posiciones_maximo = buscar_valores_maximos(lista)
print(f"las posiciones son {posiciones_maximo}")

def reemplazar_nombres(lista:list):
    cantidad_reemplazos = 0

    for i in range(len(lista)):
        print(f"{i}_{lista[i]}")

        opcion = input("Queres cambiar el nombre de la lista si/no?")

        if opcion == "si":
            lista[i] = input("ingrese nombre")
            cantidad_reemplazos += 1

    return lista, cantidad_reemplazos

lista_sin_cambios = ["luciano", "ezequiel", "bordon"]

lista_con_cambios = reemplazar_nombres(lista_sin_cambios)

print(f"la lista nueva es {lista_con_cambios[0]}, y la cantidad de reemplazos es {lista_con_cambios[1]}")
        
    
        
        
        


















