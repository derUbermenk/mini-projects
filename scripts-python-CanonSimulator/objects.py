'''
    Object classes are stored here
'''
from graphics import *
from math import *


class Projectile:
    '''
        Simulates the flight of simple projectiles near the earth’s
        surface, ignoring wind resistance. Tracking is done in two
        dimensions, height (y) and distance (x).
    '''

    def init__(self, angle, velocity, initPosition):
        """
            Create a projectile with given launch angle, initial
            velocity and height.
        """
        self.xpos = initPosition.getX
        self.ypos = initPosition.getY
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time=0.05):
        '''
            Update the state of this projectile to move it time seconds
            farther into its flight
        '''
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        '''Returns the y position (height) of this projectile.'''
        return self.ypos

    def getX(self):
        '''Returns the x position (distance) of this projectile.'''
        return self.xpos


class Button():

    '''

        A button is a labeled rectangle in a window.
        It is activated or deactivated with the activate()
        and deactivate() methods. The clicked(p) method
        returns true if the button is active and p is inside it.

    '''

    def __init__(self, win, center, height, width, label):
        '''
        creates a button object
        '''

        cOffx = width/2.0
        cOffy = height/2.0

        self.label = Text(center, label)
        self.xMin = center.getX() - cOffx
        self.yMin = center.getY() - cOffy
        self.xMax = center.getX() + cOffx
        self.yMax = center.getY() + cOffy

        # for actual button drawing in window

        p1 = Point(self.xMin, self.yMin)
        p2 = Point(self.xMax, self.yMax)

        self.active = False
        self.rect = Rectangle(p1, p2)
        self.rect.setOutline("black")
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label.draw(win)
        self.activate()

    def activate(self):
        self.active = True
        self.label.setFill("black")
        self.rect.setWidth(2)

    def deactivate(self):
        self.active = False
        self.rect.setWidth(1)

    def clicked(self, p):  # p is a point
        return (self.active and self.xMin <= p.getX() <= self.xMax
                and self.yMin <= p.getY() <= self.yMax)

    def getLabel(self):
        return self.label.getText()


class Cannon():
    '''
        Simulates the initial positioning and angles.
    '''

    def __init__(self, p, angle, win):
        '''
            where p is a point
            where angle is the launching angle
        '''
        self.win = win
        self.pos = p
        self.angle = angle

        # draw the cannon object
        # point of the center

        muzzle = Polygon()
        base = Circle()

    def updatePos(p):
        '''
            sets position via
            Point(x,y) p
        '''
        self.pos = p

    def updateAngle(angle):
        '''
            updates angle
        '''
        self.angle = angle

    def fire():
        '''
            fires cannon
            starts simulation
        '''
       return True

class Tracker(Projectile):
    '''
        Draws and tracks the current position of
        the projectile, a projectile subclass
    '''
    def __init__(self,angle,velocity,initPosition,win):
        super().__init__(self,angle,velocity,initPosition)
        self.radius = 0.6
        self.win = win
        ui = Circe(self.position,radius)
        ui.setFill("gray")
        ui.setOutline("gray")



    def moveTracker():
        '''
            Moves the tracker via changes in
            x and y
        '''
        ui.move(self.getChange())

    def isIntersect(target,winCoords,):
        '''
            function for checking if the borders of
            Tracker object is within window borders or
            does not intersect target borders
        '''
        # create a locus representation of the tracker objects borders

    def getChange():
        '''
            A helper function for calculating
            changes in x and y
            returns: dx, dy
        '''
        xInit,yInit = self.getX(), self.getY()
        self.update()
        xNow, yNow = self.getX(), self.getY()
        dx, dy = xNow - xInit, yNow - yInit
        return dx,dy

    def genLocus(xInterval):
        '''
            helper function for generating
            a locus of points for the tracker
            object
        '''
        from numpy import arange as ar

        xBMin = self.getX - self.radius
        xBMax = self.getX + self.radius
        self.xLocus = list(ar(xBMin,xBMax+xInterval,xInterval))
        self.yLocus = []

    def quadraticFunction(x):
        '''
            helper function for generating the y values
            for the locus
        '''
        b =
        minus0 =
        plus0 =


if __name__ == "__main__":
    print("foo")
