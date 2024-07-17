'''Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una 
(individualmente). 
La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ej:cadena = “murcielaguito”
Luciano
Ezequiel
Bordon
'''
vocales = [["a",0], 
           ["e",0],
           ["i",0],
           ["o",0],       
           ["u",0]]

cadena = "murcielaguito"
def contar_vocales(cadena:str,matriz:list[list]):

    for i in range(len(cadena)):
       
       match cadena[i]:
            case "a":
                matriz[0][1] += 1
            case "e":
                matriz[1][1] += 1
            case "i":
                matriz[2][1] += 1
            case "o":
                matriz[3][1] += 1
            case "u":
                matriz[4][1] += 1

    return matriz

resultado = contar_vocales(cadena, vocales)

for i in range(len(resultado)):
    for j in range(len(resultado[0])):
        print(f"{resultado[i][j]}", end = f" ")
    print("")
    



