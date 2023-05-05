import pygame  
  
pygame.init()  

HEIGHT = 800
WIDTH = 600

TILE_HEIGHT = 18
TILE_WIDTH = 35


brick_tile = pygame.image.load('img/brick.png')  
brick_red = pygame.image.load('img/brick_red.png') 
brick_green = pygame.image.load('img/brick_green.png') 
brick_blue = pygame.image.load('img/brick_blue.png') 
maze = [
        '002000000000000000000000000000',
        '001111111111111111111111111100',
        '0040000BAC000AAAABC00000000000',
        '001111111111111111111111111100',
        '002000000000000000000000000000',
        '001111011111111111111111111100',
        '0040000BAC000AAAABC00000000000',
        '001111111111111111101111111100',
        '002000000000000000000000000000',
        '001111111111111111111111111100',
        '0040000BAC000AAAABC00000000000',
        '001111111111111111111111011100',
        '0040000BAC000AAAABC00000000000',
        '00110111111111111111111A111100',
        '002000000000000000000000000000',
        '001111111111110111111110111100',
        '004000000000000000000000001000',
        '001111111111111111111111111100']

screen = pygame.display.set_mode((HEIGHT,WIDTH))  
done = False  
  
def redraw():
    for j in range(len(maze)):
        line = maze[j]
        for i in range(len(line)):
            if line[i:i+1] in '123456789':
                screen.blit(brick_tile, ( TILE_WIDTH* i, TILE_HEIGHT * j))
            elif line[i:i+1] in 'AB':
                screen.blit(brick_red, ( TILE_WIDTH* i, TILE_HEIGHT * j))
            elif line[i:i+1] in 'CD':
                screen.blit(brick_blue, ( TILE_WIDTH* i, TILE_HEIGHT * j))
            elif line[i:i+1] in 'EF':
                screen.blit(brick_green, ( TILE_WIDTH* i, TILE_HEIGHT * j))
    pygame.display.flip()  

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    redraw()
    