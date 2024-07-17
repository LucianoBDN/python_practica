'''Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.

Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
Luciano
Ezequiel
Bordon

'''

def suprimir_vocales(cadena:str) -> str:
    cadena_2 = ""

    for i in range(len(cadena)):

        match cadena[i]:
            case "a" | "e" | "i" | "o" | "u":
                pass
            case _:
                cadena_2 += cadena[i]

    
    return cadena_2

cadena = "hola"

resultado = suprimir_vocales(cadena)

print(resultado)

