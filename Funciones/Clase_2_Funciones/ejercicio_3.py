#Luciano Bordon
def retornar_cadena(primer_texto, segundo_texto, tercero_texto ):

    retornar_cadena = primer_texto + segundo_texto + tercero_texto
    
    if not primer_texto or not segundo_texto or not tercero_texto:
        retornar_cadena = None


    return retornar_cadena


primer_texto = input(" ingrese un texto: ")

segundo_texto = input(" ingrese otro texto: ")

tercer_texto = input(" ingrese un texto: ")

resultado = retornar_cadena(primer_texto, segundo_texto, tercer_texto)

print(f"el texto que retorna es: {resultado}")