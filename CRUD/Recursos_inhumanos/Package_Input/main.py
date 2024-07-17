from empleados import *
from funciones_empleados import *
from os import system

lista_empleados = [{'id':6, 'nombre': 'naruto', 'apellido': 'boludo', 'dni': 53347578, 'puesto': 'asistente', 'salario': 239234}, 
                   {'id':5, 'nombre': 'Goku', 'apellido': 'fasito', 'dni': 5000000, 'puesto': 'gerente', 'salario': 600000},
                {'id':4, 'nombre': 'Asta', 'apellido': 'añanin', 'dni': 5446434, 'puesto': 'encargado', 'salario': 500000}
                ]





id = 0

while True:
   opcion = int(input("1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado\n4. Mostrar todos los empleados\n5. Calcular promedio de los salarios\n6. Buscar empleado por dni\n7. Ordenar empleados\n8. Salir \nElija una opcion: "))


   match opcion:
      case 1:
         id_incrementado = increentar_id(id)
         id += id_incrementado
         agregar_empleado_lista(lista_empleados, id_incrementado)
      case 2:
         empleado_id = int(input("Ingrese ID: "))
         modificar_empleado(lista_empleados, empleado_id)
      case 3:
         eliminar_empleado(lista_empleados)
      case 4:
         mostrar_todos_los_empleados(lista_empleados)
      case 5:
         calcular_salario_promedio(lista_empleados)
      case 6:
         buscar_empleado(lista_empleados)
      case 7:
         menu_opciones_ordenamiento(lista_empleados)
      case 8:
         break
      
   system("pause")
   system("cls")
   