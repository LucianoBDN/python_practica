from Input import *
import datetime
import re

def reporte_auto_incremental(path_reporte: str):
    try:
        with open(path_reporte, "r") as archivo:
            for linea in archivo:
                numero_reporte = re.split(" |:|\n", linea)
                numero = numero_reporte[3]
                print(numero)
                break
        numero = int(numero)

        match numero:
            case " ":
                numero = 1
            case _: 
                numero += 1
    except:    
        numero = 1

    return numero


def buscar_coincidencias(lista_empleados: list[dict]):

    buscar_mayor_sueldo = get_int("Ingresar sueldo a buscar: ", "Ingresar de nuevo el sueldo a buscar: ", 234315, 10000000, 5)
   
    lista_salario_mayor = []

    for empleado in lista_empleados:
        salario = int(empleado['salario'])
        if buscar_mayor_sueldo < salario:
            lista_salario_mayor.append(empleado)
    
    return lista_salario_mayor




def generar_reporte(lista_empleados: list[dict], path_reporte: str):

    reporte_numero = reporte_auto_incremental(path_reporte)
    lista_coincidencias = buscar_coincidencias(lista_empleados)

    

    fecha_reporte = datetime.date.today()

    reporte = f"""\tReporte N°: {reporte_numero}
    \tFecha: {fecha_reporte}
    \tCantidad de coincidencias: {len(lista_coincidencias)}
        ID  Apellido y Nombre                Sueldo     Puesto
    ---------------------------------------------------------------
    """

    
    for dato in lista_coincidencias:
        reporte += f"\n\t{dato['id']}  {dato['apellido']},{dato['nombre']:25} {dato['salario']:8}  {dato['puesto']}\n"

    
    with open(path_reporte, "w") as archivo:
        archivo.write(reporte)


lista = [
    {
        "id": "24",
        "nombre": "lucho",
        "apellido": "napole",
        "dni": "12345678",
        "puesto": "asistente",
        "salario": "300000"
    },
    {
        "id": "27",
        "nombre": "lucho",
        "apellido": "napole",
        "dni": "12345678",
        "puesto": "asistente",
        "salario": "200000"
    },
    {
        "id": "25",
        "nombre": "lucho",
        "apellido": "napole",
        "dni": "12345678",
        "puesto": "asistente",
        "salario": "400000"
    },
    {
        "id": "22",
        "nombre": "lucho",
        "apellido": "napole",
        "dni": "12345678",
        "puesto": "asistente",
        "salario": "1000000"
    }
]

generar_reporte(lista,r"E:\Programacion_1\CRUD\Recursos_inhumanos_con_archivos\reporte.txt")