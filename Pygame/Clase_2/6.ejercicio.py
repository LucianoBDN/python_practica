import pygame
pygame.init() #inicializo pygame


lista_personajes = [{
    'nombre': 'Jonny',
    'edad': 20,
    'imagen': r"Pygame\Clase_2\Jonny_bravo.png"
},{
    'nombre': 'Goku',
    'edad': 6,
    'imagen': r"Pygame\Clase_2\Goku.png"
},{
    'nombre': 'Messi',
    'edad': 36,
    'imagen': r"Pygame\Clase_2\messi.png"
}]

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

icono = pygame.image.load("Pygame\Clase_2\icono_a.jpeg") #declaramos el icono de la ventana

pygame.display.set_icon(icono)# y aca lo usamos

#creamos la ventana
ventana = pygame.display.set_mode(TAMAÑO_VENTANA)

escenario = pygame.image.load(r"Pygame\Clase_2\escenario.jpg")
escenario = pygame.transform.scale(escenario,(1600,960))

fuente = pygame.font.SysFont("Arial", 30) #fuente y tamaño

flag = True
while flag == True: #bucle infinito para que se muestre la pantalla
    lista_evento = pygame.event.get()
    ventana.blit(escenario,(0, 0))
    for evento in lista_evento:
        if evento.type == pygame.QUIT: #pregunto si preciono la x de la ventana
            flag = False
    x = 0
    y = 0
    for personaje in lista_personajes:
        personaje['edad'] = str(personaje['edad'])
        texto = fuente.render(personaje['nombre'], False, ROJO, AZUL_CLARO)
        edad = fuente.render(personaje['edad'], False, ROJO,AZUL_CLARO)
        img = pygame.image.load(personaje['imagen'])
        img = pygame.transform.scale(img,(300,300))
        ventana.blit(img,(x,y))
        ventana.blit(img,(x,y))
        ventana.blit(texto, (x,y))
        ventana.blit(edad,(200,y))

        if y == 0:
            y = 300
        else:
            y = 600
        while y >= ALTO_VENTANA:
            y = 0

    pygame.display.update()

pygame.quit()#cierra la ventana