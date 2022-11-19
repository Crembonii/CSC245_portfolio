##
##

import pygame
#from rectangle import Rectangle

class Brick:

    def __init__ (self, x, y, w, h, color, be):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.be = be
        
    def draw (self, window):
        if self.be:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
        elif self.be == False:
            pygame.draw.rect(window, "black", (self.x, self.y, self.w, self.h))

# Get fnt.s
    def getx (self):
        return self.x

    def gety (self):
        return self.y

    def getw (self):
        return self.w

    def geth (self):
        return self.h
        
    def getBe (self):
        return self.be

    # runs when the ball collides with a brick
    def destroy (self):
        self.be = False
        # draws over the old brick
  
        