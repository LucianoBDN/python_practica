nombres = ["Jose", "Maria", "Pedro"]
apellidos = ["Gomez", "Ruiz", "Perez"]
edades = [20,45,18]

with open("agenda.csv", "w") as archivo:
    for i in range(len(nombres)):
        linea = f"{nombres[i]},{apellidos[i]},{edades[i]}\n"
        archivo.write(linea)

import re

with open("agenda.csv", "r") as archivo:
    for linea in archivo:
        registro = re.split(",|\n", linea)
        #print(registro)
        #registro = linea.split(",")
        print(f"{registro[0]}--{registro[1]}--{registro[2]}")