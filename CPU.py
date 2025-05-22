import pygame
from pygame.locals import *
import time

width = 750
height = 750
window = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("CPU")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
degrees = 0
positionX = 0
positionY = 0

def dibujar_matrix():
    window.fill((WHITE))
    for i in range(10):
        for j in range(10):
            if i%2 == 0:
                if j%2 == 0:
                    pygame.draw.rect(window, BLACK, (j * 75, i * 75, 75, 75), 0)
            else:
                if j%2 == 1:
                    pygame.draw.rect(window, BLACK, (j * 75, i * 75, 75, 75), 0)

def  bot_logic():
    return 0

def draw_bot():
    pygame.draw.circle(window, (0, 0, 255), (positionX*75+37.5, positionY*75+37.5), 10)

def main():
    pygame.init()
    dibujar_matrix()
    bot_logic()
    draw_bot()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            
        pygame.display.flip()  # Actualizar la pantalla
        time.sleep(0.1)  # Esperar un poco para ver el cambio
if __name__ == "__main__":
    main()
    # Simulación de CPU ocupada