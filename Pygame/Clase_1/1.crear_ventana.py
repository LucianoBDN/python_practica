import pygame

pygame.init() #inicializo pygame

PANTALLA = pygame.display.set_mode((800, 600)) #ancho y alto en px
pygame.display.set_caption("Mi primer ventana")#Titulo ventana


while True: #bucle infinito para que se muestre la pantalla
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT: #pregunto si preciono la x de la ventana
            pygame.quit()
            

