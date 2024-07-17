def validar_linea(numero: int, mensaje: str, mensaje_error: str,) -> int:
    while numero < 1 or numero < 3:
        numero = (mensaje_error)

    return numero

def validar_coche(numero: int, mensaje: str, mensaje_error: str,) -> int:
    while numero < 1 or numero < 15:
        numero = (mensaje_error)

    return numero

def validar_legajo(numero:int, list: list) -> int:
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == numero:
                numero_existe = True
                break
            else:
                numero_existe = None
    return numero_existe