'''Crear una función que reciba una cadena y un caracter. La función deberá
devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.
Luciano
Ezequiel
Bordon
'''


cadena = "hola locura"
caracter = "u"

def encontrar_indice_coincidencia(cadena:str, caracter:str)-> str | int:
    posicion_coincidencia = "o-1"
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            posicion_coincidencia = i
            break
    
    
    return posicion_coincidencia
            



hola = encontrar_indice_coincidencia(cadena, caracter)

print(hola)

