import pygame
import random
from gamplay.TileStatus import States
from gamplay.Tile import Tile 

black = (0, 0, 0)
gray = (200, 200, 200)
silver = (240, 240, 240)

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


        for t in self.tiles:
            self.drawTile(screen, t)

#        for i in range(9):
#            for j in range(9):        
#                screen.blit(text_surfaces[i+1], (36 + 40*i, 33 + 40*j))
        

#        self.drawTile(screen, 8, 1, 1)
#        self.drawTile(screen, 3, 7, 2)
#        self.drawTile(screen, 6, 1, 9)
        #screen.blit(text_surfaces[7], (36 + 40* 2, 33 + 40* 4))
               
    def drawTile(self, screen, tile):
        if tile.status == States.LOCKED:
            pygame.draw.circle(screen, gray, (40 + 40* (tile.col-1),42 + 40* (tile.row-1) ), 12)
            pygame.draw.circle(screen, silver, (40 + 40* (tile.col-1),42 + 40* (tile.row-1) ), 11)
            screen.blit(text_surfaces[tile.value], (36 + 40* (tile.col-1), 33 + 40* (tile.row-1)))

    def initiate(self):
        patt = '000000000010009000000002000060000030000070000000000500000000004000000000800000000'
        n = 9
        ptn = [patt[i:i+n] for i in range(0, len(patt), n)]

        for i in range(1,10):
            for j in range(1, 10):
                t = Tile(i, j, States.AVAILABLE)
                val = int(ptn[i-1][j-1])
                t.value= val
                if val > 0:
                    t.status=States.LOCKED
                self.tiles.append(t)

    def getListOfChoices(self, row, col):
        byRow = range(1, 10)
        byCol = range(1, 10)
        byNon = range(1, 10)
        rowTiles = [t for t in self.tiles if t.row == row and t.value != 0]
        colTiles = [t for t in self.tiles if t.col == col and t.value != 0]
        nonTiles = [t for t in self.tiles if int((t.row-1)/3) == int((row - 1)/3) and int((t.col-1)/3) == int((col - 1)/3) and t.value != 0]
        print ("rowTiles")
        for r in rowTiles:
            r.show();
        print ("colTiles")
        for r in colTiles:
            r.show();
        print ("nonTiles")
        for r in nonTiles:
            r.show();