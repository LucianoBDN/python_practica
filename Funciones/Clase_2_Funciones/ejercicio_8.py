#Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

#Luciano Bordon

def calcular_potencia(base, exponente):

    potencia = base ** exponente 

    return potencia

base = input("ingrese base: ")
base = int(base)
exponente = input("ingrese exponente: ")
exponente = int(exponente)

resultado = calcular_potencia(base, exponente)

print(f"la potencia es {resultado}")