def sumar_numeros(un_numero, otro_numero):
    suma = un_numero + otro_numero

    return suma

bandera_seguir = True

while bandera_seguir == True:
    opcion = int(input("1.Ingresar numeros \n2.Sumar\n3.Restar\n4.Salir\nElija una opcion :"))

    match opcion:
        case 1:
            primer_numero = int(input("ingrese un numero: "))
            segundo_numero = int(input("ingrese un numero: "))
        case 2:
            suma = sumar_numeros(primer_numero, segundo_numero)
            print(f"La suma es: {suma}")