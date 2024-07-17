# UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

# Las posibles aplicaciones son las siguientes:
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA),
# Internet de las cosas (IOT)

# Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

# A) Los datos a ingresar por cada empleado encuestado son:
# nombre del empleado
# edad (no menor a 18)
# género (Masculino - Femenino - Otro)
# tecnologia (IA, RV/RA, IOT)  
# B) Cargar por terminal 10 encuestas.
# C) Determinar:
# Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
# Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
# Nombre y tecnología que votó, uno de los empleados de género masculino con mayor edad de ese género.

#Luciano Ezequiel Bordon

contador_ra = 0
contador_rv = 0
contador_iot = 0
contador_ia = 0
contador_masculino_ia_iot = 0
no_voto_ia = 0
contador = 0
contador_cumple_condiciones = 0

for i in range(1, 11):

    nombre = input("ingrese su nombre: ")

    edad = input("ingrese su edad: ")
    edad = int(edad)

    while edad <18:
        edad = input("Reingrese su edad solo mayor a 18 anios: ")
        edad = int(edad)

    genero = input("ingese su genero: ")

    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input(" reingese su genero: ")

    tecnologia = input("a que se postula: ")
     
    while tecnologia != "ia" and tecnologia != "rv" and tecnologia != "ra" and tecnologia != "iot":
        tecnologia = input("a que se postula: ")


    match tecnologia:
        case "ia":
            if genero == "masculino":
                if 25 <= edad <= 50:
                    contador_masculino_ia_iot += 1
                    contador_ia += 1
            else:
                contador_ia += 1
        case "iot":
            if genero == "masculino":
                if 25 <= edad <= 50:
                    contador_masculino_ia_iot += 1
                    contador_iot += 1
                    if edad < 32 and edad > 41:
                        contador_cumple_condiciones += 1     
            else:
                contador_iot += 1
            match genero:
                case "femenino":
                    contador_cumple_condiciones += 1



        case "ra":
            if edad < 32 and edad > 41:
                contador_cumple_condiciones += 1 
            elif genero == "femenino":
                contador_cumple_condiciones += 1 
            else:
                contador_ra += 1
                no_voto_ia += 1  
        case "rv":
            if edad < 32 and edad > 41:
                contador_cumple_condiciones += 1
            elif genero == "femenino":
                contador_cumple_condiciones += 1   
            else:
                contador_rv += 1
                no_voto_ia += 1

        



    match genero:
        case "masculino":
            if contador == 0:
                nombre_masculino_mayor_edad = nombre
                edad_masculino_mayor_edad = edad
                tecnologia_mayor_edad = tecnologia
            else:
                if edad_masculino_mayor_edad < edad:
                    nombre_masculino_mayor_edad = nombre
                    edad_masculino_mayor_edad = edad
                    tecnologia_mayor_edad = tecnologia
        
    contador += 1



no_votaron_por_ia = (contador / no_voto_ia) * 100


print(f"Cantidad de empleados de genero masculino que votaron por IOT o IA cuya edad este entre 25 y 50 anios: {contador_masculino_ia_iot}")
print(f"el porcentaje de gente que no voto por ia es {no_votaron_por_ia}")
print(f"El masculino con mayor edad es {nombre_masculino_mayor_edad} y la tecnologia a la que se postulo es {tecnologia_mayor_edad}")