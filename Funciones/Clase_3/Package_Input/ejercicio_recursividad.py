#CLASE 4 Recursividad

from Input import get_int

def sumar_naturales(numero: int)-> int:

    if numero == 0:
        suma_naturales = 0
    else:
        suma_naturales = numero + sumar_naturales(numero - 1)

    return suma_naturales

# numero = 4

# suma_naturales = sumar_naturales(numero)
# print(suma_naturales)

def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        potencia = 1
    else:
        potencia = base * calcular_potencia(base, exponente -1) 

    return potencia

# base = 2
# exponente = 10

# potencia = calcular_potencia(base, exponente)
# print(potencia)

def sumar_digitos(numero: int) -> int:

    if numero == 0:
        sumar = 0

    else:
        sumar = numero % 10 + (sumar_digitos (numero // 10))

    return sumar

# numero = 384

# sumar = sumar_digitos(numero)

# print(sumar)



def calcular_fibonacci(numero: int) -> int:

    if numero == 0:
        numero = 0

    elif numero == 1:
        numero = 1

    else:
    
        numero = calcular_fibonacci(numero -1) + calcular_fibonacci(numero - 2)

    return numero


# numero = get_int("ingrese numero: ", "reingrese numero ", 1, 100, 3)

# fibonacci = calcular_fibonacci(numero)

# print(f"fibonacci es {fibonacci}")




    

