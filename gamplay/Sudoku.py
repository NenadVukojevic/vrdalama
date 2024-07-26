import pygame
import random
from gamplay.TileStatus import States
from gamplay.Tile import Tile 
from gamplay.States import MovementStates

black = (0, 0, 0)
gray = (200, 200, 200)
silver = (240, 240, 240)
gray = (225,225,225)
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
        self.rList = []
        self.cList = []
        self.nList = []
        self.comm = []
        self.stepState = MovementStates.NEXT_STEP

    def draw(self, screen):

        if(self.current != None):
            if self.stepState in [MovementStates.COMMON_AVAILABLE, MovementStates.BEST_PICK]:
                self.shadeCommon(screen, self.comm)
                
            if self.stepState in [MovementStates.COLUMN_AVAILABLE, MovementStates.ROW_AVAILABLE, MovementStates.NONIUS_AVAILABLE, MovementStates.COMMON_AVAILABLE, MovementStates.BEST_PICK]:
                self.shadeRow(screen, self.current.row)
                #self.showAvailableRow(screen)
                self.showAvailable(screen, self.rList, 0)
            if self.stepState in [MovementStates.COLUMN_AVAILABLE, MovementStates.NONIUS_AVAILABLE, MovementStates.COMMON_AVAILABLE, MovementStates.BEST_PICK]:
                self.shadeCol(screen, self.current.col)
                #self.showAvailableCol(screen)
                self.showAvailable(screen, self.cList, 1)
            if self.stepState in [MovementStates.NONIUS_AVAILABLE, MovementStates.COMMON_AVAILABLE, MovementStates.BEST_PICK]:
                self.shadeNon(screen, self.current.row, self.current.col)
                #self.showAvailableNon(screen)
                self.showAvailable(screen, self.nList, 2)

            
            self.shadeBest(screen, self.current.col, self.current.row)    
        self.drawGrid(screen)


        for t in self.tiles:
            if t != self.current or self.stepState in [MovementStates.BEST_PICK, MovementStates.NEXT_STEP]:
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
        pygame.draw.line(screen, gray, (20, 40*row), (380, 40*row), 38);

    def shadeCol(self, screen, col):
        pygame.draw.line(screen, gray, (  40*col, 20), (  40*col, 380), 38);


    def shadeCommon(self, screen, comm):
        for i in comm:
            pygame.draw.line(screen, pink, (36 + 40* (9 + i), 20),(36 + 40* (9 + i),  50 * 3), 38)

    def shadeNon(self, screen, row, col):
        nRow = int((row-1)/3)
        nCol = int((col-1)/3)
        x1 = 20 + 120*nRow
        x2 = 20 + 120*nCol

        pygame.draw.rect(screen, gray, pygame.Rect(20 + 120*nCol, 20+ 120*nRow, 120 , 120 ));

    def shadeBest(self, screen, col, row):
        pygame.draw.circle(screen, pink, (40 + 40* (col-1),42 + 40* (row-1) ), 12)
            

    def drawTile(self, screen, tile):
        if tile.status == States.LOCKED:
            pygame.draw.circle(screen, gray, (40 + 40* (tile.col-1),42 + 40* (tile.row-1) ), 12)
            pygame.draw.circle(screen, silver, (40 + 40* (tile.col-1),42 + 40* (tile.row-1) ), 11)
            screen.blit(text_surfaces[tile.value], (36 + 40* (tile.col-1), 33 + 40* (tile.row-1)))
        elif tile.status == States.TAKEN:
            screen.blit(text_surfaces[tile.value], (36 + 40* (tile.col-1), 33 + 40* (tile.row-1)))
    
    
    def showAvailable(self, screen, available, row):
        byRange = range(1, 10)
        for i in byRange:
            if i in available:
                screen.blit(text_surfaces[i], (36 + 40* (9 + i), 33 + 40* (row)))
        
    def showAvailableRow(self, screen):
        byRange = range(1, 10)
        usedByRows = [t.value for t in self.tiles if t.row == self.current.row and t.value != 0]
        for i in byRange:
            if i not in usedByRows or i == self.current.value:
                screen.blit(text_surfaces[i], (36 + 40* (9 + i), 33 + 40* (0)))
        
    def showAvailableCol(self, screen):
        byRange = range(1, 10)
        usedByCols = [t.value for t in self.tiles if t.col == self.current.col and t.value != 0]
        for i in byRange:
            if i not in usedByCols or i == self.current.value:
                screen.blit(text_surfaces[i], (36 + 40* (9 + i), 33 + 40* (1)))    
        
    def showAvailableNon(self, screen):
        byRange = range(1, 10)
        usedByNons = [t.value for t in self.tiles if int((t.row-1)/3) == int((self.current.row - 1)/3) and int((t.col-1)/3) == int((self.current.col - 1)/3) and t.value != 0]
        for i in byRange:
            if i not in usedByNons or i == self.current.value:
                screen.blit(text_surfaces[i], (36 + 40* (9 + i), 33 + 40* (2)))  
                    
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

        return (rowsAvailable, colsAvailable, nonsAvailable, minCommon)
    
    def step(self):
        if self.stepState == MovementStates.NEXT_STEP:
            current = None
            minVal = 9
            rList = []
            cList = []
            nList = []
            mList = []
            
            for t in [a for a in self.tiles if a.status == States.AVAILABLE]:
                (r, c, n, m) = self.getListOfChoices(t.row, t.col)
                if(len(m) < minVal):
                    minVal = len(m)
                    current = t
                    rList = r
                    cList = c
                    nList = n
                    mList = m
            self.current = current
            if(minVal > 0):
                current.status = States.TAKEN
                current.value = mList[0]
                self.rList = rList
                self.cList = cList
                self.nList = nList
                self.comm = mList
                current.show()
            self.stepState = MovementStates.ROW_AVAILABLE
        elif self.stepState == MovementStates.ROW_AVAILABLE:
            self.stepState = MovementStates.COLUMN_AVAILABLE
        elif self.stepState == MovementStates.COLUMN_AVAILABLE:
            self.stepState = MovementStates.NONIUS_AVAILABLE
        elif self.stepState == MovementStates.NONIUS_AVAILABLE:
            self.stepState = MovementStates.COMMON_AVAILABLE
        elif self.stepState == MovementStates.COMMON_AVAILABLE:
            self.stepState = MovementStates.BEST_PICK
        elif self.stepState == MovementStates.BEST_PICK:
            self.stepState = MovementStates.NEXT_STEP
        
        print(self.stepState)