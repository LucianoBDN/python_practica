import pygame


lista_nombres = ["Luciano", "Pio", "Alexis", "Jero"]

pygame.init() #inicializo pygame

#COLORES RGB
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255,255,255)


ventana = pygame.display.set_mode((800, 600)) #ancho y alto en px
pygame.display.set_caption("Mi primer ventana")#Titulo ventana
 #declaramos el icono de la ventana
# y aca lo usamos

ventana.fill(VERDE)#color verde

fuente = pygame.font.SysFont("Arial", 30) #fuente y tamaño



flag = True
while flag == True: #bucle infinito para que se muestre la pantalla
    y = 50
    x = 50
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT: #pregunto si preciono la x de la ventana
            flag = False
    
    for nombre in lista_nombres:
        texto = fuente.render(nombre, False, ROJO, AZUL_CLARO) #crear superficie con texto
        ventana.blit(texto,(x,y))
        x += 30
        y += 30
    

    pygame.display.update()

pygame.quit()#cierra la ventana