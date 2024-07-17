from Input import *
#C

def cargar_empleado(id: int, nombre: str, apellido:str, dni: int, puesto: str, salario: int )->dict:
    diccionario_empleado = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "puesto": puesto,
        "salario": salario
    }

    return diccionario_empleado

def agregar_empleado_lista(lista_empleados:list[dict], id_incrementado):
    if len(lista_empleados) < 20:
        id = id_incrementado
        nombre = get_string("Ingrese el nombre: ", "Reingrese el nombre: ",3, 20, 2)
        apellido = get_string("Ingrese el apellido: ", "Reingrese el apellido: ",3, 20, 2)
        dni = get_int("Ingrese el dni: ", "Error reingrese dni: ",5000000, 99999999, 2)
        puesto = validar_puesto("ingrese puesto del empleado: ", "ese puesto no existe: ")
        salario = get_int("ingrese el salario: ", "reingrese salario: ", 234315, 10000000, 2)

        diccionario_empleado = cargar_empleado(id,nombre,apellido,dni,puesto,salario)

        lista_empleados.append(diccionario_empleado)
    else:
        print("limite de empleados alcanzados, solo se podra ingresar otro si uno se da de baja")

#R

def mostrar_empleado(un_empleado:dict):
    print("-" * 60)
    print("| Nombre       | Apellido      | Puesto        | Salario    |")
    print("-" * 60)
    print(f"| {un_empleado['nombre']:<12} | {un_empleado['apellido']:<13} | {un_empleado['puesto']:<13} | ${un_empleado['salario']:<9} | {un_empleado['id']}")
    print("-" * 60)
    

def mostrar_todos_los_empleados(lista_empleados: list[dict]):
    for empleado in lista_empleados:
        mostrar_empleado(empleado)
 
#U
def modificar_empleado(lista_empleados: list[dict], id: int):
    empleado_encontrado = False
    for empleado in lista_empleados:
        if empleado["id"] == id:
            opcion = input("A. Modificar nombre\nB. Modificar apellido\nC. Modificar dni\nD. Modificar puesto\nE. Modificar sueldo\nF. Volver\nElija: ")
            opcion.lower()
            match opcion:
                case "a":
                    nuevo_nombre =  get_string("Ingrese el nombre: ", "Reingrese el nombre: ",3, 20, 2)
                    empleado["nombre"] = nuevo_nombre
                case "b":
                    nuevo_apellido = get_string("Ingrese el apellido: ", "Reingrese el apellido: ",3, 20, 2)
                    empleado["apellido"] = nuevo_apellido
                case "c":
                    nuevo_dni = get_int("Ingrese el dni: ", "Error reingrese dni: ",5000000, 99999999, 2)
                    empleado["dni"] = nuevo_dni
                case "d":
                    nuevo_puesto = validar_puesto("ingrese puesto del empleado: ", "ese puesto no existe: ")
                    empleado["puesto"] = nuevo_puesto
                case "e":
                    nuevo_salario = get_int("ingrese el salario: ", "reingrese salario: ", 234315, 10000000, 2)
                    empleado["salario"] = nuevo_salario
                case "f":
                    break       
        if empleado_encontrado == True:
            mensaje = "Se modifico al empleado"
        else:
            mensaje = "Empleado no existe en la lista activa"
    return mensaje

#D


def eliminar_empleado(lista_empleados: list[dict]):

    id = get_int("Ingrese el id: ", "Error reingrese id: ",0, 99999999, 2)
    
    eliminado = None
    for empleado in lista_empleados:
        if empleado["id"] == id:
            eliminado = empleado
            print("deleteado papu")
            break
        else:
            print("id no encontrado")
    if eliminado != None:
        lista_empleados.remove(eliminado)
    