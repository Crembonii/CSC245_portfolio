##
##

import pygame

class Rectangle:

    def __init__ (self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        
    def draw (self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))