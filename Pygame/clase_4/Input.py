import pygame
 
ANCHO_VENTANA = 800
ALTO_VENTANA = 800
DIMENSION_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)


pygame.init()

#VENTANA
ventana = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Comisión 311")



#TEXTO
fuente = pygame.font.SysFont("Arial",30)

input = pygame.Rect(50,50,200,32)
color_inactivo = ROJO
color_activo = VERDE
color = color_inactivo
activo = False
texto = ""

bandera_texto = False
bandera = True

while bandera == True:
    
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
        
        elif evento.type == pygame.KEYDOWN:
            if activo:
                if evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif evento.key == pygame.K_ESCAPE:
                    texto = ""
                    activo = not activo
                else:
                    texto += evento.unicode

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(evento.pos):
                activo = not activo
        
    if activo:
        color = color_activo
    else:
        color = color_inactivo




    ventana.fill("Black")
    pygame.draw.rect(ventana, color, input, 2)

    texto_superficie = fuente.render(texto, True, "White")

    ventana.blit(texto_superficie, (input.x +5, input.y - 5))

    
    pygame.display.update()


pygame.quit()