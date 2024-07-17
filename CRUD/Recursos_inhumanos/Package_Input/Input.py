# Get INTEGER

from Validate import *

def get_int( mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos : int)-> int | None:
      numero = input(mensaje)
      numero = int(numero)

      numero = validate_int(numero, mensaje_error, minimo, maximo, reintentos)

      return numero



# numero_int = get_int("ingrese numero","reingrese numero", 1, 20, 3)

# print(f"el numero que retorna es el numero {numero_int}")


# Get FLOAT

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos : float)-> float | None:
      numero = input(mensaje)
      numero = float(numero)

      numero = validate_float(numero, mensaje_error, minimo, maximo, reintentos)
           

      return numero

# numero_float = get_float("ingrese numero","reingrese numero", 10.4, 20.6, 3)

# print(f"el numero que retorna es el numero {numero_float}")



# Get string

def get_string(mensaje: str, mensaje_error: str,longitud_min:int, longitud_max: int, reintentos: int) -> str | None:
      
      string = input(mensaje)

      string = validate_length(string, mensaje_error, longitud_min, longitud_max, reintentos)
    
      return string

# string = get_string("Ingrese una cadena: ", "Por favor ingrese una cadena más corta: ", 4, 10,3)

# print(f"El string retornado es: {string}")
