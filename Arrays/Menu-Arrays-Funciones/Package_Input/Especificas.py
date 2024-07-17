


#Mostrar cantidad de positivos y negativos

def mostrar_cantidad_positivo_negativo(lista:list) -> int:

    positivo = 0
    negativo = 0

    for i in range(len(lista)):

        if lista[i] > 0:
            positivo += 1
        else:
            negativo += 1
       
    return positivo, negativo

def sumar_numeros_pares(lista: list) -> int:

    suma_num_pares = 0
    for i in range(len(lista)):

        if lista[i] % 2 == 0:
            suma_num_pares += lista[i]
            

    return suma_num_pares

def informar_mayor_numero_inpar(lista: list) -> int:

    bandera_primer_vuelta = False
    for i in range(len(lista)):

        if lista[i] % 2 == 0:
            pass
        elif bandera_primer_vuelta == False:
            numero_impar_max = lista[i]
            bandera_primer_vuelta = True
        else:
            if lista[i] > numero_impar_max:
                numero_impar_max = lista[i]
            

    return numero_impar_max

def listar(lista:list)-> list:
    for i in range(len(lista)):
        print(f"{i}_{lista[i]}")

def listar_numeros_pares(lista: list)-> list:

    for i in range(len(lista)):

        if lista[i] % 2 == 0:
            print(f"{i},{lista[i]}")
        

def listar_numeros_impares(lista: list)-> list:

    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            print(f"{i},{lista[i]}")
            


   
