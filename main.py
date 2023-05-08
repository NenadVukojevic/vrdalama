import pygame  

from gamplay.state_machine import StateMachine, Actions

pygame.init()  

stateMachine = StateMachine()


HEIGHT = 800
WIDTH = 600

TILE_HEIGHT = 18
TILE_WIDTH = 35


brick_tile = pygame.image.load('img/brick.png')  
brick_red = pygame.image.load('img/brick_red.png') 
brick_green = pygame.image.load('img/brick_green.png') 
brick_blue = pygame.image.load('img/brick_blue.png') 
maze = [
        '00000000000000000000',
        '000000AAAAAAAAA00000',
        '00000ACCCCCCCCCA0000',
        '00000ACCCCCCCCCA0000',
        '00000ACCCCCCCCCA0000',
        '00000ACCCCCCCCCA0000',
        '000000AAAAAAAAA00000',
        '00000000000000000000',
        '0000EEEEEEEEEEEEE000',
        '00000000000000000000',

        ]

screen = pygame.display.set_mode((HEIGHT,WIDTH))  
done = False  
  
def redraw():
    for j in range(len(maze)):
        line = maze[j]
        for i in range(len(line)):
            if line[i:i+1] in '123456789':
                screen.blit(brick_tile, ( TILE_WIDTH/2 + TILE_WIDTH* i, TILE_HEIGHT * j))
            elif line[i:i+1] in 'AB':
                screen.blit(brick_red, ( TILE_WIDTH/2 + TILE_WIDTH* i, TILE_HEIGHT * j))
            elif line[i:i+1] in 'CD':
                screen.blit(brick_blue, (TILE_WIDTH/2 +  TILE_WIDTH* i, TILE_HEIGHT * j))
            elif line[i:i+1] in 'EF':
                screen.blit(brick_green, ( TILE_WIDTH/2 +TILE_WIDTH* i, TILE_HEIGHT * j))
    pygame.display.flip()  

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    redraw()
    