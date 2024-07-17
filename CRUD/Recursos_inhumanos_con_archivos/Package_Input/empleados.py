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
    try:
        for empleado in lista_empleados:
            mostrar_empleado(empleado)
    except:
        mostrar_empleado(lista_empleados[0])


#U
def modificar_empleado(lista_empleados: list[dict])-> str:
    id = get_int("Ingrese el id: ", "Error reingrese id: ", 0, 99999999, 2)
    
    for empleado in lista_empleados:
        if empleado["id"] == id:
            opcion = input("A. Modificar nombre\nB. Modificar apellido\nC. Modificar dni\nD. Modificar puesto\nE. Modificar sueldo\nF. Volver\nElija: ")
            opcion.lower()
            match opcion:
                case "a":
                    nuevo_nombre =  get_string("Ingrese el nombre: ", "Reingrese el nombre: ",3, 20, 2)
                    empleado["nombre"] = nuevo_nombre
                    mensaje = "Se modifico al empleado"
                case "b":
                    nuevo_apellido = get_string("Ingrese el apellido: ", "Reingrese el apellido: ",3, 20, 2)
                    empleado["apellido"] = nuevo_apellido
                    mensaje = "Se modifico al empleado"
                case "c":
                    nuevo_dni = get_int("Ingrese el dni: ", "Error reingrese dni: ",5000000, 99999999, 2)
                    empleado["dni"] = nuevo_dni
                    mensaje = "Se modifico al empleado"
                case "d":
                    nuevo_puesto = validar_puesto("ingrese puesto del empleado: ", "ese puesto no existe: ")
                    empleado["puesto"] = nuevo_puesto
                    mensaje = "Se modifico al empleado"
                case "e":
                    nuevo_salario = get_int("ingrese el salario: ", "reingrese salario: ", 234315, 10000000, 2)
                    empleado["salario"] = nuevo_salario
                    mensaje = "Se modifico al empleado"
                case "f":
                    break       
  
    return mensaje

#D
import json
def eliminar_empleado(lista_empleados: list[dict], path_eliminados: str, lista_bajas: list[dict]):



    lista_modificada = lista_empleados 
    id = get_int("Ingrese el id: ", "Error reingrese id: ",0, 99999999, 5)
    
    eliminado = None
    for empleado in lista_empleados:
        id_baja = int(empleado['id'])
        if id_baja == id:
            eliminado = empleado
            print("se ha encontrado el, empleado a eliminar")
            break
    
    
    if eliminado != None:
        lista_bajas.append(eliminado)
        lista_modificada.remove(eliminado)
        with open(path_eliminados, "w", encoding= 'utf-8') as archivo:
            json.dump(lista_bajas, archivo, indent=4)

    return lista_modificada