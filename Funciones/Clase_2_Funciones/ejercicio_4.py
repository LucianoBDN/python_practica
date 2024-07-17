#Validacion de numeros enteros y lo reorne

#Luciano Bordon

# validar int
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos : int)-> int | None:
    numero = input(mensaje)
    numero = int(numero)
    

    while (numero < minimo or numero > maximo) and reintentos != 0:
            numero = input(mensaje_error)
            numero = int(numero)
            reintentos -= 1
    if reintentos == 0:
          return None
    else:
        return numero


# numero_int = get_int("ingrese numero","reingrese numero", 10, 20, 3)

# print(f"el numero que retorna es el numero {numero_int}")

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos : float)-> float | None:
        numero = input(mensaje)
        numero = float(numero)

        while (numero < minimo or numero > maximo) and reintentos != 0:
                numero = input(mensaje_error)
                numero = float(numero)
                reintentos -= 1
                
        if reintentos == 0:
            numero = None
        
        return numero

# numero_float = get_float("ingrese numero","reingrese numero", 10, 20, 3)
# print(f"el numero que retorna es {numero_float}")

def retornar_cadena(primer_texto, segundo_texto, tercero_texto ):

    retornar_cadena = primer_texto + segundo_texto + tercero_texto
    
    if not primer_texto or not segundo_texto or not tercero_texto:
        retornar_cadena = None


    return retornar_cadena


# primer_texto = input(" ingrese un texto: ")

# segundo_texto = input(" ingrese otro texto: ")

# tercer_texto = input(" ingrese un texto: ")

# resultado = retornar_cadena(primer_texto, segundo_texto, tercer_texto)

# print(f"el texto que retorna es: {resultado}")
      


   