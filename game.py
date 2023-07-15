import pygame

pygame.init()
WIDTH = 640
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
x_pos = y_pos = 320
x_direction = 0
y_direction = 0
run = True
screen = pygame.display.set_mode((WIDTH,HEIGHT))
while run:
    pygame.time.delay(100)  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y_direction = -10
        x_direction = 0
    if keys[pygame.K_DOWN]:
        y_direction = 10
        x_direction = 0
    if keys[pygame.K_LEFT]:
        y_direction = 0
        x_direction = -10
    if keys[pygame.K_RIGHT]:
        y_direction = 0
        x_direction = 10
    
    x_pos += x_direction
    y_pos += y_direction
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (x_pos, y_pos, 10, 10))
     
    pygame.display.update()

pygame.quit()

class Snake:
    def __init__(self):
        self.lenght = 1
        self.body = 20
        self.