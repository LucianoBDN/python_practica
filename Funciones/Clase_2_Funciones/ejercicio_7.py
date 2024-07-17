# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

# Luciano Bordon

def encontrar_maximo_numero(numero_1, numero_2, numero_3):

    if numero_1 > numero_2 and numero_1 > numero_3:
        maximo_numero = numero_1
    elif numero_2 > numero_1 and numero_2 > numero_3:
        maximo_numero = numero_2
    else:
        maximo_numero = numero_3
    
    return maximo_numero

numero_1 = int(input("ingrese numero 1: "))

numero_2 = int(input("ingrese numero 2: "))

numero_3 = int(input("ingrese numero 3: "))

maximo_numero = encontrar_maximo_numero(numero_1, numero_2, numero_3)

print(f"el numero mas grande es: {maximo_numero}")
    