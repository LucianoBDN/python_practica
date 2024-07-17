# strip

# cadena = "          pepe              "
# cadena = cadena.strip()

# print(cadena)

#UPPER
#todo mayuscula
# cadena = "luchoTazo"
# cadena = cadena.upper()
# print(cadena)

# LOWER
#todo minuscula

# cadena = "luchoTazo"
# cadena = cadena.lower()
# print(cadena)

#capitalize

# cadena = "luchoTazo"
# cadena = cadena.capitalize()
# print(cadena)

# Replace

# cadena = "Lucho Lucho Lucho "
# cadena = cadena.replace("Lucho", "BDN")
# print(cadena)

#SPLIT

#utiliza el paramnetro que le pasa y lo usa para separar dentro de una cadena
#deja de ser una cadena y pasa a ser lista

# cadena = "lucho mauro pepe pedro carlos juan sofia"
# cadena = cadena.split(" ")
# print(cadena)

#Join

# cadena = "lucho mauro pepe pedro carlos juan sofia"
# lista_nombres = cadena.split(" ")
# lista_nombres.append("carla")
# print(lista_nombres)


# cadena = "*". join(lista_nombres)

# print(cadena)


# zfill

# hora = "1:01"

# print(hora)

# hora = hora.zfill(5)

# print(hora)

# isalpha

# cadena = "lucho"

# print(cadena)

# booleano = cadena.isalpha()

# print(booleano)


# count

# cadena = "pedro pedro pedro pedro pe"

# print(cadena)

# cantidad = cadena.count("pedro")

# print(cantidad)

# nombre = "Luciano"

# apellido = "Bordon"

# cantidad = "nombre: {0} ---- apellido: {1}"

# print(cantidad.format(nombre, apellido))

#slice

cadena = "luciano bordon"

nombre = cadena[0:8]
nombre= nombre.capitalize()

apellido = cadena[9:]
apellido = apellido.capitalize()

cadena = " ".join(nombre,apellido)

print(cadena)



















