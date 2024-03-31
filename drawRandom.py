import pygame
import random
import math
from gamplay.Maze import Maze

HEIGHT = 800
WIDTH = 600

black = (0, 0, 0)
blue = (0, 0, 128)
shadow = (128, 128, 128)
white = (255, 255, 255)

screen = pygame.display.set_mode((HEIGHT,WIDTH)) 

done = False  
step = 50

maze = Maze(60, 40)

maze.generateRandom();

def getRandomMove(x, y):
    rn = 45 * round (8*random.random())
    if (x + math.sin(math.radians(rn))*step) > HEIGHT:
        deltaX = HEIGHT
    else: 
        deltaX = x + math.sin(math.radians(rn))*step
    if (y + math.cos(math.radians(rn))*step) > WIDTH:
        deltaY = WIDTH
    else:
        deltaY = y + math.cos(math.radians(rn))*step

    return (deltaX, deltaY)
    

def drawOld():
    screen.fill(white)
    x = 110
    y = 120
    for a in range(2000):
        (z, w) = getRandomMove(x, y)
        pygame.draw.line(screen, blue, (x, y), (z, w), 2)
        x = z
        y = w
    pygame.display.update()

def draw():
    screen.fill(white)
    maze.drawMaze(screen=screen)
    pygame.display.update()

clock=pygame.time.Clock()
status = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                status = True
    draw()
    maze.move()
    clock.tick(29) 