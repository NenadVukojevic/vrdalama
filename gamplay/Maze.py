import pygame
import random
from enum import Enum

black = (0, 0, 0)
red = (255, 0, 0)
gray = (120, 120, 120) 

TILE_SIZE = 12
TILE_SPACING = 13
RADIUS = 5
TOP = 20
LEFT = 10

class States(Enum):
    OPEN = 0
    CLOSED = 1
    VISITED = 2
    DEADEND = 3

class Tile:
    
    def __init__(self, x, y, state):
        self.x = x
        self.y =  y
        self.state = state

    def drawTile(self, screen):
        if(self.state == States.CLOSED):
            pygame.draw.rect(screen, black, pygame.Rect(LEFT + self.x*TILE_SPACING, TOP +  self.y*TILE_SPACING,  TILE_SIZE, TILE_SIZE))
        if(self.state == States.VISITED):
            pygame.draw.circle(screen, red, (LEFT + self.x*TILE_SPACING + 7,  TOP +  self.y*TILE_SPACING  + 7),  RADIUS)
        if(self.state == States.DEADEND):
            pygame.draw.circle(screen, gray, (LEFT + self.x*TILE_SPACING + 7,  TOP +  self.y*TILE_SPACING  + 7),  RADIUS)

class Maze:
    
    def __init__(self, row, col):
        self.row = row
        self.col =  col
        self.tiles = []
        self.pos = (11,10)
        self.path = []
        
    def randomStatus(self):
        if(random.random()*10>2):
            status = States.OPEN
        else:
            status = States.CLOSED
        return status

    def generateRandom (self):
        print('generate')
        for i in range(self.row):
            row = []
            for j in range(self.col):
                if(i == 0 or j==0 or i == self.row-1 or j == self.col-1):
                    t = Tile(i, j, States.CLOSED)
                else:
                    t = Tile(i, j, self.randomStatus())
                row.append(t)    
            self.tiles.append(row)

        self.tiles[10][10].state = States.VISITED

        self.tiles[11][10].state = States.DEADEND

    def drawMaze (self, screen):
        for i in range(self.row):
            for j in range(self.col):
                self.tiles[i][j].drawTile(screen)


    def move (self):
        x = self.pos[0]
        y = self.pos[1]
        listOfOpen = self.findAdjacent(States.OPEN)
        if len(listOfOpen) > 0 :
            next = listOfOpen[0]
            self.tiles[next.x][next.y].state = States.VISITED
            self.pos = (next.x, next.y)
            self.path.append(next)
        else:
            self.tiles[x][y].state = States.DEADEND
            next = self.path.pop()
            self.pos = (next.x, next.y)

    def findAdjacent(self, state):
        possible = []
        x = self.pos[0]
        y = self.pos[1]
        t = self.getTileAt(x-1, y, state)
        if t != None:
            possible.append(t)
        t = self.getTileAt(x+1, y, state)
        if t != None:
            possible.append(t)
        t = self.getTileAt(x, y-1, state)
        if t != None:
            possible.append(t)
        t = self.getTileAt(x, y+1, state)
        if t != None:
            possible.append(t)
        return possible
            

    def getTileAt(self, x, y, state):
        response = None
        try:
            if self.tiles[x][y].state == state:
                response = self.tiles[x][y]
        except:
            response = None
        return response    