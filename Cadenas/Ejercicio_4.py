'''
Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.


	Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

Luciano 
Ezequiel
Bordon
'''


def eliminar_caracteres_rep(cadena : str) -> str:
	cadena_2 = ""
	
	for i in range(len(cadena)):
		if cadena[i] != cadena[i - 1]:
			cadena_2 += cadena[i]

	return cadena_2



cadena = "luuuuuuchooooooooo"


resultado = eliminar_caracteres_rep(cadena)

print(f"{resultado}")
