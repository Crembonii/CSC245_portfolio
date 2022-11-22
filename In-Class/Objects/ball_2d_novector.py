##
## Author: Kristina Striegnitz, John Rieffel
##
## Version: Fall 2022 
##
## This file defines a simple ball class. The ball is stationary; we
## just get to define its position, size and color. This
## implementation uses the vector class.

import pygame
import random

class Ball:

    #initialize state variables

    def __init__ (self, x, y, r, m, color):
        self.x = x
        self.y = y
        self.xv = 0
        self.yv = 0
        self.r = r
        self.m = float(m)
        self.color = color

    def setVelocity(self,inVelocityX,inVelocityY):
        self.xv, self.yv = inVelocityX,inVelocityY


    def updatePosition(self):
        self.x = self.x + self.xv
        self.y = self.y + self.yv

    def setColor(self, color):
        self.color = color

    def randomizeColor(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.setColor(pygame.color.Color(r,g,b))

    def bounce(self, height, width):
        if (self.x <= self.r):
            self.x = self.r
            self.xv *= -1
            self.randomizeColor()
        if (self.x >= width - self.r):
            self.x = width - self.r
            self.xv *= -1
            self.randomizeColor()
        if (self.y <= self.r):
            self.y = self.r
            self.yv *= -1
            self.randomizeColor()
        if (self.y >= height - self.r):
            self.y = height - self.r
            self.yv *= -1
            self.randomizeColor()

    def simulate(self, height, width):
        self.updatePosition()
        self.bounce(height, width)

    def randomizePosition(self, height, width):
        self.y = random.randint(0, height)
        self.x = random.randint(0, width)

    def draw (self, window):
        #print "hello"
        #print self.p.x, " ", self.p.y, " ", self.r
        pygame.draw.circle(window, self.color, (int(self.x),int(self.y)),self.r)

