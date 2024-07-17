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
icono = pygame.image.load("Pygame\icono_a.jpeg") #declaramos el icono de la ventana
pygame.display.set_icon(icono)# y aca lo usamos

ventana.fill(VERDE)#color verde

fuente = pygame.font.SysFont("Arial", 60) #fuente y tamaño
texto = fuente.render("Aguante dragon ball", False, ROJO, AZUL_CLARO) #crear superficie con texto
texto2 = fuente.render("la puta madre", False, ROJO, AZUL_CLARO)


flag = True
while flag == True: #bucle infinito para que se muestre la pantalla
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT: #pregunto si preciono la x de la ventana
            flag = False
    ventana.blit(texto,(50,50))
    ventana.blit(texto2,(50,200))
    pygame.display.update()

pygame.quit()#cierra la ventana