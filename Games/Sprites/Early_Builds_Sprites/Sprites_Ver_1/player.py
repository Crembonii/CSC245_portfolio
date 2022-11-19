"""
Derived from code provided at
http://programarcadegames.com/

Edited by: Nolan Kelley
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
        self.pspeed = 2
        self.jspeed = 3
        self.grounded = True

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.v = Vector(0,0)
        sprite_sheet = SpriteSheet("Squig.walk.png")
        self.imageheight = 177
        # Load all the images into a list
        image = sprite_sheet.get_image(0, 0, 141, self.imageheight)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(400, -37, 124, self.imageheight)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(550, -50, 126, self.imageheight)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(254, -15, 109, self.imageheight)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(703, -50, 128, self.imageheight)
        self.walking_frames.append(image)
        image = sprite_sheet.get_image(850, -60, 131, self.imageheight)
        self.walking_frames.append(image)

        # To test grounded
        #self.checkimage = sprite_sheet.get_image(0, 0, 141, 150)

        # Set the image the player starts with
        self.image = self.walking_frames[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()


    def update(self):
        """ Move the player. """
        # Gravity etc
        # self.simulate()

        # Move left or right
        if self.v.y < 0:
            self.image = self.walking_frames[1]
            if self.v.x < 0:
                self.image = pygame.transform.flip(self.image, True, False)
        elif self.v.y > 0:
            self.image = self.walking_frames[4]
            if self.v.x < 0:
                self.image = pygame.transform.flip(self.image, True, False)
        elif self.v.x > 0:
            frame = (self.rect.x // 30) % (len(self.walking_frames)-1)
            self.image = self.walking_frames[frame +1]
        elif self.v.x < 0:
            frame = (self.rect.x // 30) % (len(self.walking_frames)-1)
            self.image = self.walking_frames[frame +1]
            # flips direction sprite faces:
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.v.x == 0:
            self.image = self.walking_frames[0]
        
        # test if grounded
        #if self.grounded:
        #    self.image = self.checkimage


    def simulate(self,platforms):
        """ Calculate effect of gravity. """
        ## NOTE USE self.rect for position
        self.rect.x += self.v.x
        self.rect.y += self.v.y

        # Set if grounded
        
        for p in platforms:
            if pygame.sprite.collide_rect(self,p) == False:
                self.grounded = False

        for p in platforms:
            if pygame.sprite.collide_rect(self,p):
                if self.rect.y + self.rect.height > p.rect.y and self.rect.y + self.rect.height < p.rect.y + p.rect.height:
                    self.grounded = True
                elif self.rect.x + self.rect.width < p.rect.x:
                    self.v.x *= 0
                elif self.rect.x > p.rect.x + p.rect.width:
                    self.v.x *= 0
        
        # Check if grounded
        if self.grounded == False:
            self.v.y += 0.05
            pass
        elif self.grounded == True:
            self.v.y = 0
            pass


    def jump(self):
        """ Called when user hits 'jump' button. """
        self.v.y = -self.jspeed

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.v.x = -self.pspeed

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.v.x = self.pspeed

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.v.x = 0


if __name__ == "__main__":
    size = (640,480)
    screen = pygame.display.set_mode(size)
    p = Player()