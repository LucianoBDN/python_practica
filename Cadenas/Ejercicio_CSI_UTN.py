'''CASO INVESTIGACIÓN CRIMINAL: CSI UTN 

Se ha encontrado una muestra de ADN en el lugar del crimen que contiene la siguiente secuencia de bases nitrogenadas: “CGTTTAATG”. 
La investigación ha revelado tres posibles sospechosos, cada uno con su propia muestra de ADN:
Juan Pérez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
María Rodríguez
Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
Carlos Sánchez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"

Para resolver el caso, nos piden que desarrollemos un programa que compare las combinaciones de bases nitrogenadas de la muestra encontrada con 
las muestras de los sospechosos. 
Mostrar el nombre por pantalla en caso de encontrar al asesino, o la leyenda “SON TODOS INOCENTES”. 

Luciano 
Ezequiel
Bordon
'''





def encontrar_culpable_CSI(nombre:str ,muestra_sospechoso:str, muestra_prueba:str) -> str:

    for i in range(len(muestra_sospechoso) - len(muestra_prueba) + 1):
        buscar = muestra_sospechoso[i:i + len(muestra_prueba)]
        if buscar == muestra_prueba:
            culpable = f"el analisis verifico que el asesino es {nombre}"
            break
        
        else:
            culpable = f"el sospechozo {nombre} es inocente"

    return culpable

nombre = input("ingrese nombre: ")
muestra_sospechoso = input("ingrese muestra del sospechozo: ")
prueba = input("ingrese prueba encontrada: ")


resultado = encontrar_culpable_CSI(nombre, muestra_sospechoso, prueba)

print(resultado)