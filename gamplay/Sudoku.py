import pygame
import random
from gamplay.TileStatus import States
from gamplay.Tile import Tile 

black = (0, 0, 0)
gray = (200, 200, 200)
silver = (240, 240, 240)
pink = (230, 200, 230)

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Tahoma', 14)
text_surfaces = []
for i in range (10):
    text_surfaces.append(my_font.render(str(i), False, (0, 0, 0)))

class Sudoku:
    def __init__(self):
        self.tiles = []
        self.current = None

    def draw(self, screen):

        if(self.current != None):
            self.shadeRow(screen, self.current.row)
            self.shadeCol(screen, self.current.col)
            self.shadeNon(screen, self.current.row, self.current.col)
       
        self.drawGrid(screen)


        for t in self.tiles:
            self.drawTile(screen, t)




    def drawGrid(self, screen):
        for i in range(10):
            if(i%3 == 0):
                w = 2
            else:
                w = 1
            pygame.draw.line(screen, black, (20, 20 + 40*i), (380, 20 + 40*i), w)
            pygame.draw.line(screen, black, ( 20 + 40*i, 20), ( 20 + 40*i, 380), w) 
                          
    def shadeRow(self, screen, row):
        pygame.draw.line(screen, pink, (20, 40*row), (380, 40*row), 38);

    def shadeCol(self, screen, col):
        pygame.draw.line(screen, pink, (  40*col, 20), (  40*col, 380), 38);

    def shadeNon(self, screen, row, col):
        nRow = int((row-1)/3)
        nCol = int((col-1)/3)
        x1 = 20 + 120*nRow
        x2 = 20 + 120*nCol
        
 #       print(row, col, nRow, nCol, x1, x2)
        pygame.draw.rect(screen,pink, pygame.Rect(20 + 120*nCol, 20+ 120*nRow, 120 , 120 ));
        
    def drawTile(self, screen, tile):
        if tile.status == States.LOCKED:
            pygame.draw.circle(screen, gray, (40 + 40* (tile.col-1),42 + 40* (tile.row-1) ), 12)
            pygame.draw.circle(screen, silver, (40 + 40* (tile.col-1),42 + 40* (tile.row-1) ), 11)
            screen.blit(text_surfaces[tile.value], (36 + 40* (tile.col-1), 33 + 40* (tile.row-1)))
        elif tile.status == States.TAKEN:
            screen.blit(text_surfaces[tile.value], (36 + 40* (tile.col-1), 33 + 40* (tile.row-1)))
        
    def initiate(self, patt):
#        patt = '000000000010009000000002000060000030000070000000000500000000004000000000800000000'
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
        byRange = range(1, 10)
        
        usedByRows = [t.value for t in self.tiles if t.row == row and t.value != 0]
        usedByCols = [t.value for t in self.tiles if t.col == col and t.value != 0]
        usedByNons = [t.value for t in self.tiles if int((t.row-1)/3) == int((row - 1)/3) and int((t.col-1)/3) == int((col - 1)/3) and t.value != 0]
        
        rowsAvailable = [t for t in byRange if t not in usedByRows]
        colsAvailable = [t for t in byRange if t not in usedByCols]
        nonsAvailable = [t for t in byRange if t not in usedByNons]
        
        
        minCommon = [t for t in rowsAvailable if t in colsAvailable and t in nonsAvailable]

        return minCommon
    
    def step(self):
        current = None
        minVal = 9
        mList = []
        for t in [a for a in self.tiles if a.status == States.AVAILABLE]:
            m = self.getListOfChoices(t.row, t.col)
            if(len(m) < minVal):
                minVal = len(m)
                current = t
                mList = m
        self.current = current
        if(minVal > 0):
            current.status = States.TAKEN
            current.value = mList[0]
            current.show()
        