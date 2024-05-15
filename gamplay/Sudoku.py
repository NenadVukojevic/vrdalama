import pygame
import random
from enum import Enum


black = (0, 0, 0)
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Tahoma', 14)
text_surfaces = []
for i in range (10):
    text_surfaces.append(my_font.render(str(i), False, (0, 0, 0)))

class Sudoku:
    def __init__(self):
        self.tiles = []


    def draw(self, screen):

        for i in range(10):
            if(i%3 == 0):
                w = 2
            else:
                w = 1
            pygame.draw.line(screen, black, (20, 20 + 40*i), (380, 20 + 40*i), w)
            pygame.draw.line(screen, black, ( 20 + 40*i, 20), ( 20 + 40*i, 380), w)

        for i in range(9):
            for j in range(9):        
                screen.blit(text_surfaces[i+1], (36 + 40*i, 33 + 40*j))
            