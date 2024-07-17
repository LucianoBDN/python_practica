from empleados import *
from funciones_empleados import *
from funciones_archivos import *
from os import system


path = r"E:\Programacion_1\CRUD\Recursos_inhumanos_con_archivos\empleados.csv"
path_eliminado = r"E:\Programacion_1\CRUD\Recursos_inhumanos_con_archivos\Bajas.json"
lista_empleados = cargar_archivo_csv(path)
lista_de_bajas = cargar_archivo_json(path_eliminado)
system("cls")

while True:
   try:   
      opcion = int(input("1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado\n4. Mostrar todos los empleados\n5. Calcular promedio de los salarios\n6. Buscar empleado por dni\n7. Ordenar empleados\n8. Salir \nElija una opcion: "))


      match opcion:
         case 1:
            system("cls")
            id = buscar_proximo_id(lista_empleados,lista_de_bajas)
            agregar_empleado_lista(lista_empleados, id)
         case 2:
            system("cls")
            modificar_empleado(lista_empleados)
         case 3:
            lista_de_empleados_modificada = eliminar_empleado(lista_empleados,path_eliminado,lista_de_bajas)
            lista_empleados = lista_de_empleados_modificada
            
            actualizar_archivo_empleados(lista_empleados,path)
         case 4:
            mostrar_todos_los_empleados(lista_empleados)
         case 5:
            promedio_sueldo = calcular_salario_promedio(lista_empleados)
            print(f"El sueldo promedio es de {promedio_sueldo}")
         case 6:
            buscar_empleado(lista_empleados)
         case 7:
            system("cls")
            lista_ordenada= menu_opciones_ordenamiento(lista_empleados)
            mostrar_todos_los_empleados(lista_ordenada)
         case 8:
            actualizar_archivo_empleados(lista_empleados,path)
            break
   except:
         print("Opcion no valida, ingrese otra opcion")
   system("pause")
   system("cls")
   