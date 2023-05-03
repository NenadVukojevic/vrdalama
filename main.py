import pygame  
  
pygame.init()  

HEIGHT = 800
WIDTH = 600

brick_tile = pygame.image.load('img/brick.png')  


screen = pygame.display.set_mode((HEIGHT,WIDTH))  
done = False  
  
def redraw():
    screen.blit(brick_tile, (20, 40))
    screen.blit(brick_tile, (80, 80))
    screen.blit(brick_tile, (120, 80))
    screen.blit(brick_tile, (160, 80))
    screen.blit(brick_tile, (200, 80))
    pygame.display.flip()  

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    redraw()
    