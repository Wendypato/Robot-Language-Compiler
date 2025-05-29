import pygame
from pygame.locals import *
import time

# Variables del Display
width = 750
height = 750
window = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("CPU")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variables del Bot
positionX = 0
positionY = 0
degrees = 0

# Variables del archivo
# Se abre el archivo y se lee su contenido
archivo = open("test.txt", "r")
instructions = archivo.read()
archivo.close()
# Se separa las instrucciones en lineas y luego en comas
instructions = instructions.splitlines()
for i in range(len(instructions)):
    instructions[i] = instructions[i].split(",")

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

def check_position():
    global positionX
    global positionY
    if positionX < 0 or positionX > 10 or positionY < 0 or positionY > 10:
        print("El bot se ha salido de los límites del tablero.")
        return 

def bot_movement(num):
    global positionY
    global positionX
    global degrees
    if degrees == 0:  
        positionY += num
    elif degrees == 90: 
        positionX += num
    elif degrees == 180: 
        positionY -= num
    else: 
        positionX -= num
    

def rotate_bot(num):
    global degrees
    degrees = degrees + num
    if degrees >= 360:
        degrees = degrees - 360

def  bot_logic():
    for i in range(len(instructions)):
        if instructions[i][0] == "MOV":
            bot_movement(int(instructions[i][1]))
            draw()
        else:
            rotate_bot(int(instructions[i][1]))
    return 0

def draw_bot():
    pygame.draw.circle(window, (0, 0, 255), (positionX*75+37.5, positionY*75+37.5), 10)

def draw():
    dibujar_matrix()
    draw_bot()
    pygame.display.flip()  # Actualizar la pantalla
    time.sleep(1)  # Esperar un poco para ver el cambio

def main():
    draw()
    bot_logic()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            
    input("Presiona Enter para salir...")  # Esperar a que el usuario presione Enter
    pygame.quit()

if __name__ == "__main__":
    main()
    # Simulación de CPU ocupada