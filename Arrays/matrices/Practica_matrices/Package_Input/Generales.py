def mostrar_matriz(lista : list) -> list | None:
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end= " ")
        print("")

def agregar_lista_a_matriz(list: list, list_add: list) -> list:
    list.append(list_add)

    return list

def print_matriz(lista: list, mensaje:str, segundomensaje:str, tercermensaje: str):

    for i in range(len(lista)):

        print((mensaje), lista[i][0], (segundomensaje), lista[i][1], (tercermensaje), lista[i][0])

def sumar_recaudacion_linea(lista: list) -> list:
    recaudacion_linea_1 = 0
    recaudacion_linea_2 = 0
    recaudacion_linea_3 = 0
    for i in range(len(lista)):
        if lista[i][0] == 1:
            recaudacion_linea_1 += lista[i][2]
        elif lista[i][0] == 2:
            recaudacion_linea_2 += lista[i][2]
        else:
            recaudacion_linea_3 += lista[i][2]
    
    return recaudacion_linea_1, recaudacion_linea_2, recaudacion_linea_3


def calcular_recaudacion_por_coches(lista: list):
    recaudacion_coche_1 = 0
    recaudacion_coche_2 = 0
    recaudacion_coche_3 = 0
    recaudacion_coche_4 = 0
    recaudacion_coche_5 = 0


    for i in range(len(lista)):
        if lista[i][1] == 1:
            recaudacion_coche_1 += lista[i][2]
        elif lista[i][1] == 2:
            recaudacion_coche_2 += lista[i][2]
        elif lista[i][1] == 3:
            recaudacion_coche_3 += lista[i][2]  
        elif lista[i][1] == 4:
            recaudacion_coche_4 += lista[i][2]
        else:
            recaudacion_coche_5 += lista[i][2]

    recaudacion_coche =[recaudacion_coche_1, recaudacion_coche_2, recaudacion_coche_3, recaudacion_coche_4, recaudacion_coche_5]
    
    return recaudacion_coche

def calcular_recaudacion_total(lista:list)-> float:
    recaudacion_total = 0
    recaudacion_total = float(recaudacion_total)
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            recaudacion_total += lista[i][2]
            
    return recaudacion_total    
