#validate int
def validate_int(numero, mensaje_error: str, minimo: int, maximo: int, reintentos : int)-> int | None:
    
    while (numero < minimo or numero > maximo) and reintentos != 0:
            numero = input(mensaje_error)
            numero = int(numero)
            reintentos -= 1
            
    if reintentos == 0:
            numero = None
    
    return numero

def validate_float(numero, mensaje_error: str, minimo: int, maximo: int, reintentos : int)-> float | None:
       
        while (numero < minimo or numero > maximo) and reintentos != 0:
                numero = input(mensaje_error)
                numero = float(numero)
                reintentos -= 1
                
        if reintentos == 0:
                numero = None

        return numero

def validate_length(string: str, mensaje_error: str, longitud_min: int, longitud_max: int, reintentos: int) -> str | None:
       
         while reintentos !=0 and (len(string) < longitud_min or len(string) > longitud_max):
             string = input(mensaje_error)
             reintentos -= 1
    
         if reintentos == 0:
             string = None

         return string

