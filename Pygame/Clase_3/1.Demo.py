import pygame
import sys





# Datos de ejemplo
respuestas = ['A', 'B', 'C', 'D']
niveles_premios = [1000, 5000, 10000, 1000]

# Inicialización de pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
background_color = (255, 255, 255)
bar_color = (0, 0, 255)
text_color = (0, 0, 0)

# Fuente
font = pygame.font.SysFont('Arial', 24)
screen.fill(background_color)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    pygame.display.update()

pygame.quit()
sys.exit()


