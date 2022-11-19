"""
Derived from code provided at
http://programarcadegames.com/

Edited heavily by: Nolan Kelley
"""
import pygame


from spritesheet_functions import SpriteSheet
from vector import Vector

class Player(pygame.sprite.Sprite):

    # -- Attributes

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames = []
    

    # -- Methods
    def __init__(self):
        """ Constructor function """
        #This is ugly, but it came with the example code...

        # Set player stats
        self.pspeed = 4         #Horizontal speed
        self.jheight = 6        #Vertical velocity subtracted when jumping
        self.tvel = 6           #Fastest falling speed
        self.grounded = True    #Whether or not player is on a platform
        self.dropping = False    #Whether the player is dropping or not


        #direction facing (True = right, False = left)
        self.face = True

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.v = Vector(0,0)
        sprite_sheet = SpriteSheet("Squig.walk.png")
        # Load all the images into a list
        #0 
        image = sprite_sheet.get_image(0, 86, 141, 88)
        self.walking_frames.append(image)
        #2
        image = sprite_sheet.get_image(400, 67, 124, 69)
        self.walking_frames.append(image)
        #3
        image = sprite_sheet.get_image(550, 61, 126, 71)
        self.walking_frames.append(image)
        #1
        image = sprite_sheet.get_image(254, 83, 109, 78)
        self.walking_frames.append(image)
        #4
        image = sprite_sheet.get_image(703, 30, 128, 98)
        self.walking_frames.append(image)
        #5
        image = sprite_sheet.get_image(850, 33, 131, 75)
        self.walking_frames.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()


    def update(self):
        """ Only used for animations """

        # Jumping animations
        if self.v.y < 0:
            self.image = self.walking_frames[1]
            if self.face == False:
                self.image = pygame.transform.flip(self.image, True, False)
        elif self.v.y > 0:
            self.image = self.walking_frames[4]
            if self.face == False:
                self.image = pygame.transform.flip(self.image, True, False)

        # Moving left/right animation
        elif self.v.x != 0:
            frame = (self.rect.x // 30) % (len(self.walking_frames)-1)
            self.image = self.walking_frames[frame +1]
            if self.face == False:
                self.image = pygame.transform.flip(self.image, True, False)
           
        # Idle position
        elif self.v.x == 0:
            self.image = self.walking_frames[0]
            if self.face:
                 self.image = pygame.transform.flip(self.image, True, False)


    def simulate(self,platforms):
        """ Calculate effects of gravity and collision. """
        ## NOTE USE self.rect for position
        self.rect.x += self.v.x
        self.rect.y += self.v.y

        # Set to "not grounded" when not colliding with something
        for p in platforms:
            if pygame.sprite.collide_rect(self,p) == False:
                self.grounded = False

        # Collisions checked here:
        for p in platforms:
            if pygame.sprite.collide_rect(self,p):
                # Check to make sure it's not a wall collision
                if (self.rect.x + self.rect.width > p.rect.x + 3
                    and self.rect.x < p.rect.x + p.rect.width - 3):
                    # Check if grounded
                    if p.rect.y + (p.rect.height/3) > self.rect.y + self.rect.height > p.rect.y:
                        self.grounded = True
                        if self.rect.y + self.rect.height > p.rect.y + 1:
                            self.rect.y -= abs(self.rect.y + self.rect.height - p.rect.y -1)
                    # Check if hit ceiling
                    elif p.rect.y + (p.rect.height/1.5 ) < self.rect.y < p.rect.y + p.rect.height:
                        self.v.y = 0
                        self.rect.y += 1
                # Check to make sure it's not a floor/celing collision
                if (self.rect.y < p.rect.y + p.rect.height - 3
                and self.rect.y + self.rect.height > p.rect.y + 3):
                    # Check if hit wall
                    if (self.rect.x + self.rect.width > p.rect.x 
                    and self.rect.x < p.rect.x + p.rect.width):
                        self.rect.x -= self.v.x # Prevents button mashing through walls
                        self.v.x *= 0
        
        # Set velocity based on if grounded
        if self.grounded == False:
            if self.v.y < self.tvel:
                self.v.y += 0.1
                if self.dropping:
                    self.v.y += 0.4
            pass
        elif self.grounded == True:
            self.v.y = 0
            pass

    # Player-controlled movement:
    def jump(self):
        """ Called when user hits 'jump' button. """
        self.v.y = -self.jheight

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.v.x = -self.pspeed
        self.face = False

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.v.x = self.pspeed
        self.face = True

    def drop(self):
        if self.v.y < self.tvel:
            self.dropping = True
    
    def stop_drop(self):
        self.dropping = False

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.v.x = 0


if __name__ == "__main__":
    size = (640,480)
    screen = pygame.display.set_mode(size)
    p = Player()