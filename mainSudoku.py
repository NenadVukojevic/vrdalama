import pygame
import random
import math
from gamplay.Sudoku import Sudoku

HEIGHT = 800
WIDTH = 600

black = (0, 0, 0)
blue = (0, 0, 128)
shadow = (128, 128, 128)
white = (255, 255, 255)

screen = pygame.display.set_mode((HEIGHT,WIDTH)) 

done = False  
step = 50

sudoku = Sudoku()
sudoku.initiate()
    
sudoku.getListOfChoices(4,5)

def draw():
    screen.fill(white)
    sudoku.draw(screen=screen)
    pygame.display.update()

clock=pygame.time.Clock()
status = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                status = not status

    draw()
    clock.tick(29) 