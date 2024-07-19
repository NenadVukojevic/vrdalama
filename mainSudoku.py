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
sudoku.initiate('000800000010009000000002000060000030000070000000000500001000004000000000800000000')
    



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
                
    sudoku.step()
    draw()
    clock.tick(4) 