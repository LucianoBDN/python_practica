def transcribir_archivo(path_entrada: str, pat_salida: str):

    try: 
        with open(path_entrada, "r") as archivo:
            with open (pat_salida, "w") as archivo_transcrito:
                for numero in archivo:
                    print(numero)
                    archivo_transcrito.write(numero)
    except:
        print("no se pudo transcribir el archivo")


transcribir_archivo(r"E:\Programacion_1\CRUD\Ejercicio_archivos\lista_numeros.txt", r"E:\Programacion_1\CRUD\Ejercicio_archivos\lista_numeros2.txt")