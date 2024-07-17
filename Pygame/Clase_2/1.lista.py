import pygame
pygame.init() #inicializo pygame

#COLORES RGB
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255,255,255)

#definimos tamaños
ANCHO_VENTANA = 1600
ALTO_VENTANA = 960

#creamos tupla de tamaño
TAMAÑO_VENTANA = (ANCHO_VENTANA,ALTO_VENTANA)


#ventana = pygame.display.set_mode((800, 600)) #ancho y alto en px

pygame.display.set_caption("Prueba imagenes")#Titulo ventana

icono = pygame.image.load("Pygame\Clase_1\icono_a.jpeg") #declaramos el icono de la ventana

pygame.display.set_icon(icono)# y aca lo usamos

#creamos la ventana
ventana = pygame.display.set_mode(TAMAÑO_VENTANA)

escenario = pygame.image.load(r"Pygame\Clase_2\Fondo.jpg")

flag = True
while flag == True: #bucle infinito para que se muestre la pantalla
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT: #pregunto si preciono la x de la ventana
            flag = False
    
    ventana.blit(escenario,(0,0))
  
    

    pygame.display.update()

pygame.quit()#cierra la ventana