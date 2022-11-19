
import pygame

#from rectangle import Rectangle

class Paddle:

    def __init__ (self, x, y, w, h, v, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = v
        self.color = color
        
    def draw (self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))

    def simulate (self, width):
        self.move(width)

    def setVelocity (self, vel):
        self.v = vel

    def setVelLeft (self, vel):
        self.v = -vel

    def move (self, width):
        # If statements prevent going past a wall
        if (self.v > 0 and self.x + self.w < width):
            self.x += self.v
        elif (self.v < 0 and self.x > 0):
            self.x += self.v

    # Get fnt.s
    def getx (self):
        return self.x

    def gety (self):
        return self.y

    def getw (self):
        return self.w

    def geth (self):
        return self.h


