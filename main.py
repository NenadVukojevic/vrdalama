import pygame  

from gamplay.state_machine import StateMachine, Actions, States

pygame.init()  

stateMachine = StateMachine()

black = (0, 0, 0)
blue = (0, 0, 128)
shadow = (128, 128, 128)


font = pygame.font.SysFont("comicsans", 50)

HEIGHT = 800
WIDTH = 600

TILE_HEIGHT = 18
TILE_WIDTH = 35


brick_tile = pygame.image.load('img/brick.png')  
brick_red = pygame.image.load('img/brick_red.png') 
brick_green = pygame.image.load('img/brick_green.png') 
brick_blue = pygame.image.load('img/brick_blue.png') 

paddle = pygame.image.load('img/paddle.png')
ball = pygame.image.load('img/ball.png')

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
  
position = pygame.Rect(600, 500, 35, 14)

def draw_level():
    screen.fill(black)
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

    screen.blit(paddle, (position.x, position.y))
    screen.blit(ball, (200, 500))

    pygame.display.flip()  


def handle_paddle_movement(keys_pressed):
    if keys_pressed[pygame.K_LEFT]:
        position.x -= 5;

    if keys_pressed[pygame.K_RIGHT]:
        position.x += 5;


def draw_result():
    title = 'Pavel Jesenski!'
    screen.fill(black)
    screen.blit(font.render(title, True, shadow), (202, 102))
    screen.blit(font.render(title, True, blue), (200, 100))
    

def redraw():
    if stateMachine.state == States.INIT:
        draw_level()
    else:
        draw_result()
    pygame.display.update()


clock=pygame.time.Clock()

while not done:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print ('pressed space')
                stateMachine.transit(Actions.START)

    keys_pressed = pygame.key.get_pressed();
    handle_paddle_movement(keys_pressed);

    redraw()
    clock.tick(60)
    