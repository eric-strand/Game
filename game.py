import pygame

pygame.init()

screen = pygame.display.set_mode((1000,400))
x = 500
run = True
# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
      
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x += -1
    if keys[pygame.K_RIGHT]:
        x+= 1

    screen.fill((255,255,255))

    pygame.draw.circle(screen,(255,0,0), (x, 100), 20)

    pygame.display.update()

pygame.quit()