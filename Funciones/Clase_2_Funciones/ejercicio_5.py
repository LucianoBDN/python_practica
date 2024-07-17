#Luciano Bordon

from math import pi

def calcular_area_circulo():

    radio = input("ingrese el radio del ciruculo ")
    radio = float(radio)

    area = pi * radio ** 2

    return area


area = calcular_area_circulo()

print(f"el area del circulo es: {area}")
