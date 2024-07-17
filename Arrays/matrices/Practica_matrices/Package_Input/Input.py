# Get INTEGER

from Validate import *

def get_int( mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos : int)-> int | None:
      numero = input(mensaje)
      numero = int(numero)

      numero = validate_int(numero, mensaje_error, minimo, maximo, reintentos)

      return numero


# Get FLOAT

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos : float)-> float | None:
      numero = input(mensaje)
      numero = float(numero)

      numero = validate_float(numero, mensaje_error, minimo, maximo, reintentos)
           

      return numero



# Get string

def get_string(mensaje: str, mensaje_error: str,longitud_min:int, longitud_max: int, reintentos: int) -> str | None:
      
      string = input(mensaje)

      string = validate_length(string, mensaje_error, longitud_min, longitud_max, reintentos)
    
      return string


