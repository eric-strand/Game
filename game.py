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


    if x_pos <= 0:
        x_pos = 0
        x_direction = 0
    elif x_pos >= 600:
        x_pos = 600
        x_direction = 0
    if y_pos <= 0:
        y_pos = 0
        y_direction = 0
    elif y_pos >= 600:
        y_pos = 600
        y_direction = 0

    if keys[pygame.K_UP]:
        y_direction = -40
        x_direction = 0
    if keys[pygame.K_DOWN]:
        y_direction = 40
        x_direction = 0
    if keys[pygame.K_LEFT]:
        y_direction = 0
        x_direction = -40
    if keys[pygame.K_RIGHT]:
        y_direction = 0
        x_direction = 40
    
    x_pos += x_direction
    y_pos += y_direction
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (x_pos, y_pos, 40, 40))
     
    pygame.display.update()

pygame.quit()

