"""

Author: John Rieffel

Edited by: Nolan Kelley

Based off of 

Simpson College Computer Science Material

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

from player import Player
from simple_platform import Box

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    HEIGHT = 880
    WIDTH = 1340
    size = [WIDTH,HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("demo with sprite sheets")

    active_sprite_list = pygame.sprite.Group()
    # Create the player
    player = Player()

    # Create the platforms list (used so I can check all platforms w/ out including the player)
    platforms = []
    
    # Create the platforms
    p1 = Box(pygame.color.Color("yellow"),50,250) 
    p1.rect.x = 50
    p1.rect.y = HEIGHT - 61
    p2 = Box(pygame.color.Color("blue"),50,378) 
    p2.rect.x = 450
    p2.rect.y = HEIGHT - 100
    p3 = Box(pygame.color.Color("darkblue"),300,50) 
    p3.rect.x = 900
    p3.rect.y = HEIGHT - 600
    p4 = Box(pygame.color.Color("green"),50,500) 
    p4.rect.x = 100
    p4.rect.y = HEIGHT - 350
    p5 = Box(pygame.color.Color("red"),50,250) 
    p5.rect.x = 1050
    p5.rect.y = HEIGHT - 100
    p6 = Box(pygame.color.Color("darkred"),50,100) 
    p6.rect.x = 1150
    p6.rect.y = HEIGHT - 300
    p7 = Box(pygame.color.Color("darkgreen"),50,100) 
    p7.rect.x = 1050
    p7.rect.y = HEIGHT - 500
    p8 = Box(pygame.color.Color("lightgreen"),200,50) 
    p8.rect.x = 400
    p8.rect.y = HEIGHT - 560
    p9 = Box(pygame.color.Color("aqua"),10,50) 
    p9.rect.x = 350
    p9.rect.y = HEIGHT - 450

    # Appending platforms to 'platforms'
    platforms.append(p1)
    platforms.append(p2)
    platforms.append(p3)
    platforms.append(p4)
    platforms.append(p5)
    platforms.append(p6)
    platforms.append(p7)
    platforms.append(p8)
    platforms.append(p9)

    # Place player
    player.rect.x = 100 
    player.rect.y = HEIGHT - player.rect.height - 70

    # Add player and platforms to active sprites
    active_sprite_list.add(player)
    for p in platforms:
        active_sprite_list.add(p)

    #Loop until the user clicks the close button or the player falls too far.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    if player.grounded:
                        player.jump()
                if event.key == pygame.K_DOWN:
                    if player.grounded == False:
                        player.drop()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    player.stop()
                if event.key == pygame.K_RIGHT:
                    player.stop()
                if event.key == pygame.K_DOWN:
                    player.stop_drop()

        # Update the player.
        active_sprite_list.update()
        player.simulate(platforms)

        #ends game when player falls
        if player.rect.y > HEIGHT + 20:
            done = True

        #current_level.draw(screen)
        screen.fill(pygame.color.Color("gray14")) 
        active_sprite_list.draw(screen)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
