import pygame  
  
pygame.init()  

HEIGHT = 800
WIDTH = 600

TILE_HEIGHT = 18
TILE_WIDTH = 35


brick_tile = pygame.image.load('img/brick.png')  

maze = ['00F0BAC000AAAABCDA0000A0000000',
        '00F000BAC000AAAABCDA00A0000000',
        '00F000000BAC000AAAA000A0000000',
        '0000000F0BAC0ABCDA0000A0000000',
        '00F0000BAC000AAAABC000A0000000']

screen = pygame.display.set_mode((HEIGHT,WIDTH))  
done = False  
  
def redraw():
    for j in range(len(maze)):
        line = maze[j]
        for i in range(len(line)):
            if line[i:i+1] != '0':
                screen.blit(brick_tile, ( TILE_WIDTH* i, TILE_HEIGHT * j))
    pygame.display.flip()  

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    redraw()
    