archivo = open(r"C:\Users\Luciano\Desktop\mi primer archivo.txt", "w")
archivo.write("¿hola a todos soy luchito\nvos quien sos? un peronista inmundo seguiro no?")
archivo.close()

archivo = open(r"C:\Users\Luciano\Desktop\mi primer archivo.txt", "r")

cadena = archivo.read()
print (cadena)

archivo.close()

lista = ["Matias","Esteban","German", "Giovanni"]

with open("listanombres.txt", "w") as archivo:
    for nombre in lista:
        archivo.write(f"{nombre}\n")


with open("listanombres.txt", "r") as archivo:
    lista = archivo.read()

print((lista))

with open("listanombres.txt", "r") as archivo:
    for line in archivo:
        print(line, end="")
