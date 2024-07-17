'''Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.

Luciano
Ezequiel
Bordon
'''

def contar_sub_cadenas(cadena:str, subcadena:str) -> int:
    contador = 0

    for i in range(len(cadena) - len(subcadena) + 1):
        buscar = cadena[i:i + len(subcadena)]
        if buscar == subcadena:
            contador += 1
        

    return contador




resultado = contar_sub_cadenas("El pan del panadero", "pan")

print(resultado)