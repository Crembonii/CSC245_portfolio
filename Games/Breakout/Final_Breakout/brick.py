##
##

import pygame
#from rectangle import Rectangle

class Brick:

    def __init__ (self, x, y, w, h, color, exists):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.exists = exists
        
    def draw (self, window):
        if self.exists:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(window, "black", (self.x, self.y, self.w, self.h))

  
        