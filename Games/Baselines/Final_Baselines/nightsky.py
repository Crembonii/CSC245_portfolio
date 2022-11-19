# Eddited by Nolan Kelley

import random
import pygame
pygame.init()
from star import Star

# Instansiate variables
sStarTimer = 80
newSStar = True
numStars = 100
window = [900,600]

screen = pygame.display.set_mode(window)

# Creates the list of stars
stars = []
while numStars > 0:
    s = Star(random.randint(0,window[0]), random.randint(0,window[1]), 0, random.randint(1,4))
    stars.append(s)
    numStars -= 1

# Creates the shooting star
sStar = Star(random.randint(0,window[0]/1.5), random.randint(0,window[1]), random.randint(1,3)/2, random.randint(5,10))

#blatently not stolen code
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Draws the background
    screen.fill(pygame.color.Color("Black"))

    #Draws the stars
    for s in stars:
        pygame.draw.circle(screen, (255, 255, 0), (s.x,s.y), s.r)
        numStars -= 1
    
    #Shooting star code
    if sStarTimer < 60:
        #Creates a shooting star
        if newSStar == True:
            sStar.x = random.randint(0,window[0]/1.5)
            sStar.y = random.randint(0,window[1])
            sStar.r = random.randint(15,30)
            sStar.v = random.randint(1,3)/2
            deceleration = 0
            newSStar = False
        
        # Changes position over time
        sStar.x += sStar.v *(sStarTimer/60)

        # Sets radius
        r = sStar.r

        # Alters radius over time
        if sStarTimer < 50:
            r = sStar.r*(sStarTimer/50)
            sStar.x -= sStar.v * (sStarTimer/150)
            sStarTimer -= deceleration
            deceleration += 0.001

        # Draws the shooting star
        pygame.draw.circle(screen, (255, 200, 60), (sStar.x, sStar.y), r)
        
        # Resets timer and newSStar boolean
        if sStarTimer < 2:
            sStarTimer = 100
            newSStar = True
            
    # Lowers the timer
    sStarTimer -= 0.05

    print(sStarTimer)
    pygame.display.flip()

pygame.quit()