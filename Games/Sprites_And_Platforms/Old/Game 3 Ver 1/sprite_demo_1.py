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
    HEIGHT = 480
    WIDTH = 640
    size = [WIDTH,HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("demo with sprite sheets")

    active_sprite_list = pygame.sprite.Group()
    # Create the player
    player = Player()

    # Create the platforms
    
    platforms = []
    
    p1 = Box(pygame.color.Color("blue"),50,90) 
    p1.rect.x = 450
    p1.rect.y = HEIGHT - p1.rect.h - 50

    p2 = Box(pygame.color.Color("blue"),50,250) 
    p2.rect.x = 50
    p2.rect.y = HEIGHT - p2.rect.h

    platforms.append(p1)
    platforms.append(p2)
    # Create all the levels

    player.rect.x = 100 
    player.rect.y = HEIGHT - player.rect.height - 70
    active_sprite_list.add(player)
    for p in platforms:
        active_sprite_list.add(p)

    #Loop until the user clicks the close button.
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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    player.stop()
                if event.key == pygame.K_RIGHT:
                    player.stop()

        # Update the player.
        
        active_sprite_list.update()

        player.simulate(platforms)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        #current_level.draw(screen)
        screen.fill(pygame.color.Color("gray14")) 
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
