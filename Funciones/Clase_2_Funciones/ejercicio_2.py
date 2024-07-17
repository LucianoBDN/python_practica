#bordon luciano
def retornar_numero_flotante(numero_flotante):
    numero_flotante = float(numero_flotante)

    return numero_flotante

numero_flotante = input("ingrese un numero con '.' ")

resultado = retornar_numero_flotante(numero_flotante)

print(f"el numero que retorna es: {resultado}")

