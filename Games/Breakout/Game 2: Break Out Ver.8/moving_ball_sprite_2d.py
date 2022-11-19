##
## Author: Kristina Striegnitz
##
## Version: Fall 2011 
##
## Updates: John Rieffel, Fall 2022
##
## This file defines a ball class that can move in two dimensions and
## can bounce off other balls.

from hashlib import new
from pickle import FALSE
import pygame
import math

from vector import Vector
from ball_2d import Ball
from paddle import Paddle
from brick import Brick

class MovingBall (Ball):

    v = Vector(0.0, 0.0)

    speedlimit = 500

    def __init__ (self, x, y, r, m, color, xv, yv, up):

        Ball.__init__(self, x, y, r, m, color)

        self.v = Vector(float(xv),float(yv))
        self.up = up


    def simulate (self, dt, width, height, pad):
        self.move (dt)
        self.bounce_wall (width, height)
        self.bounce_paddle (pad)


    def move (self, dt):

        self.p = self.p + self.v


    def clamp_v (self):
        '''
        clamp max speed
        '''
        if self.v.length() > self.speedlimit:
            self.v.normalize()
            self.v = self.v * float(self.speedlimit)
            

    def bounce_wall (self, width, height):
        '''
        handle bounces and readjust to prevent penetration
        '''
        if self.p.x < self.r:
            self.p.x = self.r
            self.v.x *= -1
        elif self.p.x > width-self.r:
            self.p.x = width-self.r
            self.v.x *= -1
        if self.p.y < 0+self.r:
            self.p.y = self.r
            self.v.y *= -1
        elif self.p.y > height-self.r:
            #self.p.y = height-self.r
            #self.v.y *= -1
            self.up = False
    
    def bounce_paddle (self, pad):
        
        # Vectors from corners to ball
        vAE = Vector(self.p.x - pad.x,
         self.p.y - pad.y)
        vBE = Vector(self.p.x - (pad.x + pad.w),
         self.p.y - pad.y)
        vCE = Vector(self.p.x - pad.x,
         self.p.y - (pad.y + pad.h))
        vDE = Vector(self.p.x - (pad.x + pad.w),
         self.p.y - (pad.y + pad.h))

        # Vectors from corners to corners
        vAB = Vector(pad.w, 0)
        vBD = Vector(0, -pad.h)
        vDC = Vector(-pad.w, 0)
        vCA = Vector(0, pad.h)

        # Calculate ball distance to each wall (absolute value of corner-to-ball cross corner-to-corner divided by corner-to-corner)
        dAB = abs(vAE.cross(vAB)) / vAB.length()
        dBD = abs(vBE.cross(vBD)) / vBD.length()
        dDC = abs(vDE.cross(vDC)) / vDC.length()
        dCA = abs(vCE.cross(vCA)) / vCA.length()

        # Check distance and reverse velocity
        if dAB <= self.r:
            # - 10 and + 10 for accesibility (and cause corners are buggy)
            if self.p.x > pad.x - 10 and self.p.x < pad.x + pad.w + 10:
                self.p.y = pad.y - self.r
                self.v.y *= -1
        if dBD <= self.r:
            if self.p.y > pad.y and self.p.y < pad.y + pad.h:
                self.p.x = pad.x + pad.w + self.r
                self.v.x *= -1
        if dDC <= self.r:
            if self.p.x > pad.x and self.p.x < pad.x + pad.w:
                self.p.y = pad.y + pad.h + self.r
                self.v.y *= -1
        if dCA <= self.r:
            if self.p.y > pad.y and self.p.y < pad.y + pad.h:
                self.p.x = pad.x - self.r
                self.v.x *= -1

    # same code as bounce_paddle but destroys brick
    def bounce_brick (self, pad):
        
        # Vectors from corners to ball
        vAE = Vector(self.p.x - pad.x,
         self.p.y - pad.y)
        vBE = Vector(self.p.x - (pad.x + pad.w),
         self.p.y - pad.y)
        vCE = Vector(self.p.x - pad.x,
         self.p.y - (pad.y + pad.h))
        vDE = Vector(self.p.x - (pad.x + pad.w),
         self.p.y - (pad.y + pad.h))

        # Vectors from corners to corners
        vAB = Vector(pad.w, 0)
        vBD = Vector(0, -pad.h)
        vDC = Vector(-pad.w, 0)
        vCA = Vector(0, pad.h)

        # Calculate ball distance to each wall
        dAB = abs(vAE.cross(vAB)) / vAB.length()
        dBD = abs(vBE.cross(vBD)) / vBD.length()
        dDC = abs(vDE.cross(vDC)) / vDC.length()
        dCA = abs(vCE.cross(vCA)) / vCA.length()

        # Check distance and reverse velocity
        if dAB <= self.r:
            if self.p.x > pad.x and self.p.x < pad.x + pad.w:
                self.p.y = pad.y - self.r
                self.v.y *= -1
                return True
        if dBD <= self.r:
            if self.p.y > pad.y and self.p.y < pad.y + pad.h:
                self.p.x = pad.x + pad.w + self.r
                self.v.x *= -1
                return True
        if dDC <= self.r:
            if self.p.x > pad.x and self.p.x < pad.x + pad.w:
                self.p.y = pad.y + pad.h + self.r
                self.v.y *= -1
                return True
        if dCA <= self.r:
            if self.p.y > pad.y and self.p.y < pad.y + pad.h:
                self.p.x = pad.x - self.r
                self.v.x *= -1
                return True
        return False

    def collide (self, other): 
        """
        Checks whether two circles collide. If they do and are already
        intersecting, they get moved apart a bit. The return value is
        None, if there is no collision, and the vector pointing from
        the center of the first to the center of the second ball if
        there is a collision.
        """
        d = self.p - other.p
        #print d
        if d.length() < self.r + other.r:
            #print("collide:", self.p, other.p, self.p.minus(other.p))
            repair = float(self.r + other.r - d.length())
            d.normalize()
            #print self.p, other.p
            self.p = self.p + (repair*d)
            other.p = other.p + (-1*repair*d)
            #print repair, self.p, other.p
            return d
        else:
            return None

    def getResponse(self,other,normvector):
                    # new velocity is 
                    # v1_normal' = v1_normal*(m1-m2)+2*m2*v2_normal
                    #              ----------------------------      
                    #                   m1 + m2
        return Vector(0,0)

    def bounce (self, j, n):

        self.v = self.v + (n * (j / self.m))
        self.clamp_v ()

    def setVelocity(self,v):
        self.v = v
