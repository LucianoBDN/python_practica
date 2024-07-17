'''Crear una función que reciba como parámetro una cadena y
 determine si la misma es o no un palíndromo. Deberá retornar un valor
 booleano indicando lo sucedido.
 Luciano
 Ezequiel
 Bordon
 '''



def determinar_palindromo(cadena:str) -> bool:
    cadena_invertida = cadena[::-1] 

    if cadena == cadena_invertida:
        es_palindromo = True
    else:
        es_palindromo = False

    return es_palindromo
    

cadena = "reconocer"

resultado = determinar_palindromo(cadena)

print(f"Es palindromo ? {resultado}")










