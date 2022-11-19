# Created by Nolan Kelley

import pygame
pygame.init()

class Star:

    x = 0
    y = 0
    v = 0
    r = 1


    def __init__ (self, x, y, v, r,):

        self.x = x
        self.y = y
        self.v = v
        self.r = r