#Desarrollar una función que reciba como parametros el precio de un producto y el porcentaje de descuento que se aplicara. La funcion retornara el precio del producto con descuento.  (Enviar aqui link de GDB)

def calcular_descuento(precio:int, descuento:int):

    descuento = precio * (descuento / 100)

    return descuento

precio = input("ingrese precio: ")
precio = int(precio)
descuento = input("ingrese descuento: ")
descuento = int(descuento)
precio_con_descuento = calcular_descuento(precio, descuento)

print(f"el precio con descuento seria {precio_con_descuento}")