
def actualizar_archivo_empleados(lista_empleados: list [dict], path: str):

    with open(path, "w") as archivo:
        for empleado in lista_empleados:
            linea = f"{empleado['id']},{empleado['nombre']},{empleado['apellido']},{empleado['dni']},{empleado['puesto']},{empleado['salario']}\n"
            archivo.write(linea)



import re
def cargar_archivo_csv(path: str)-> list[dict]:

    lista_empleados = []

    try:
        with open(path, "r") as archivo:
            for linea in archivo:
                registro = re.split(",|\n", linea)

                empleado = {
                    'id': registro[0],
                    'nombre': registro[1],
                    'apellido': registro[2],
                    'dni': registro[3],
                    'puesto': registro[4],
                    'salario': registro[5]
                }
                
                lista_empleados.append(empleado)
    except:
        print("no hay empleados cargados")

    return lista_empleados        





import json
def cargar_archivo_json (path: str):

    try:
        with open(path, "r", encoding= 'utf-8' ) as archivo:
            data = json.load(archivo)

    except:
        print("no hay bajas de empleados")
        
    return data


def buscar_proximo_id(lista_activos :list[dict], lista_bajas: list[dict])-> int:

    id_activa_mas_alta = 0
    id_baja_mas_alta = 0

    for empleado in lista_activos:
        activo_id = int(empleado['id'])
        if activo_id > id_activa_mas_alta:
            id_activa_mas_alta = activo_id
    

    for baja in lista_bajas:
        baja_id = int(baja['id'])
        if baja_id > id_baja_mas_alta:
            id_baja_mas_alta = baja_id
    
    if id_activa_mas_alta > id_baja_mas_alta:
        id = id_activa_mas_alta + 1

    else:
        id = id_baja_mas_alta + 1

    
    return id















    