import random
import pygame
pygame.init()

screen = pygame.display.set_mode([900,600])
i = 69
while i > 0:
    pygame.draw.circle(screen, (255, 255, 0), (random.randint(0,900),random.randint(0,600)), random.randint(1,4))
    i = i - 1

#bonus variables
#shootingStar = False
#x = 0

#blatently stolen code
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #bonus work (ran out of time)
#    if x == 0:
#        if random.randint(1,100) > 50:
#           shootingStar = True
#    if shootingStar == True:
#        if x == 0:
#            x = 50
#        pygame.draw.circle(screen, (255, 255, 0), (random.randint(0,900)-x,random.randint(0,600)), random.randint(9,16) + (x/10))
#    x = x-0.1

    pygame.display.flip()

pygame.quit()