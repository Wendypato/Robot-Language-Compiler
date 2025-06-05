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
direccion = "DOWN"  # Direccion inicial del bot

# Variables del archivo
# Se abre el archivo y se lee su contenido
archivo = open("instructions.txt", "r")
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

def check_position(num):
    if positionX+num < 0 or positionX+num > 9 or positionY+num < 0 or positionY+num > 9:
        print("El bot se ha salido de la matriz.")
        exit(1)  # Salir del programa si el bot se sale del tablero
        return 


def bot_movement(num):
    global positionY
    global positionX
    global degrees
    if degrees == 0 or degrees == 90:
        step = 0.25
    else:
        step = -0.25
    # Verificar si el movimiento es válido
    check_position(num)
    # Animar el movimiento del bot
    if direccion == "DOWN" or direccion == "UP":
        for i in range(num*4):
            round = i//4
            positionY += step
            draw(i-4*round)
    else:
        for i in range(num*4):
            round = i//4
            positionX += step
            draw(i-4*round)
    
        
                

def rotate_bot(num):
    global degrees
    global direccion
    degrees = degrees + num
    if degrees >= 360:
        degrees = degrees - 360
    if degrees == 0:  
        direccion = "DOWN"
    elif degrees == 90: 
        direccion = "RIGHT"
    elif degrees == 180: 
        direccion = "UP"
    else: 
        direccion = "LEFT"

def  bot_logic():
    for i in range(len(instructions)):
        if instructions[i][0] == "MOV":
            bot_movement(int(instructions[i][1]))
            draw(0)
        else:
            rotate_bot(int(instructions[i][1]))
            draw(0)
    return 0

def draw_bot(num):
    if num != 2:
        CPU = pygame.image.load(f"sprites/penguin-gray[{direccion}][{num}].png")
    else:
        CPU = pygame.image.load(f"sprites/penguin-gray[{direccion}][{0}].png")
    CPU = pygame.transform.scale(CPU, (75, 75))  # Escalar la imagen del bot
    CPU.convert_alpha()  # Convertir la imagen para mejorar el rendimiento
    window.blit(CPU, (positionX * 75, positionY * 75))

def draw(num):
    dibujar_matrix()
    draw_bot(num)
    pygame.display.flip()  # Actualizar la pantalla
    time.sleep(.2)  # Esperar un poco para ver el cambio

def main():
    draw(0)
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