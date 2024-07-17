from class_boligrafo import *

lapicera_azul = boligrafo("Azul","Fino")

lapicera_roja = boligrafo("Rojo", "Grueso")


print(lapicera_roja.recargar(100))
print(lapicera_roja.escribir_texto("Ricardito hacete culear viejo peroncho"))

print(lapicera_azul.recargar(10))
print(lapicera_azul.escribir_texto("InstanciaBolígrafoCapacidadMáximaCienTintaInicialOchentaConstructorSinParámetros"))