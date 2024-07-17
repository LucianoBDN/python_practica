import pygame

pygame.init() #inicializo pygame


NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255,255,255)


ventana = pygame.display.set_mode((800, 600)) #ancho y alto en px
pygame.display.set_caption("Mi primer ventana")#Titulo ventana

ventana.fill(AZUL_CLARO)

icono = pygame.image.load("Pygame\icono_a.jpeg")
pygame.display.set_icon(icono)

flag = True
while flag == True: #bucle infinito para que se muestre la pantalla
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT: #pregunto si preciono la x de la ventana
            flag = False
    pygame.display.update()

pygame.quit()#cierra la ventana