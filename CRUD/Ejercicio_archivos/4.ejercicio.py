def contar_elementos(path: str):
    
    contador_linea = 0
    contador_caracteres = 0
    lineas = []

    with open(path, "r") as archivo:
        for linea in archivo:
            lineas.append(linea)
            contador_linea += 1
            contador_caracteres += len(linea.rstrip())

    poema = "".join(lineas)
    print(poema)
    lista_palabras = poema.split()
    

    cantidad_palabras = len(lista_palabras)

    datos = {
       'lineas': contador_linea,
       'caracteres': contador_caracteres,
       'palabras': cantidad_palabras
   }

    return datos



datos = contar_elementos(r"E:\Programacion_1\CRUD\Ejercicio_archivos\poema.txt")


print("+----------------------------------------+")
print("|       Estadísticas del Poema           |")
print("+----------------------------------------+")
print(f"|  Cantidad de caracteres: {datos['caracteres']}               |")
print(f"|  Cantidad de líneas:     {datos['lineas']}             |")
print(f"|  Cantidad de palabras:   {datos['palabras']}             |")
print("+----------------------------------------+")