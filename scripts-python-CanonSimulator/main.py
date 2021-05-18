'''
    Programming Exercise 10
    A graphical program for cannon ball launching simultion
'''

from graphics import *
from objects import *
from time import sleep
from objects *


def main():

    # set gui objects
    win = GraphWin("Cannon Sim", 400, 400)
    win.setCoords(0, 0, 10, 10)

    canPosBT = Button(win, Point(1.5, 9), 0.5, 2, "Pos")
    fireBT = Button(win, Point(1.5, 8), 0.5, 2, "Fire")
    quitBT = Button(win, Point(1.5, 7), 0.5, 2, "Quit")
    angle = Entry(Point(1.5, 5), 2)
    state = Text(Point(5.5, 9.2), "Ready")
    posPrompt = Text(Point(5, 7), "Click anywhere to position")

    # init simulated objects
    # tracker instance inside cannonBalltracker instance inside cannonBall
    cannon = Cannon()
    cannonBall = Projectile()
    target = Target()

    # draw gui
    state.draw(win)
    angle.draw(win)

    # get initial mouse click
    pt = win.getMouse()

    while not quitBT.clicked(pt):
        theta = eval(angle.getText())
        fAngle = Text(Point(1.5, 2), angle.getText())

        if fireBT.clicked(pt):
            cannon.fire()
            state.setText("Simulating")
            while (cannonBall.getBorders() != target.getBorders) or (cannonBall.getBorders() != window_Borders)

        elif canPosBT.clicked(pt):
            posPrompt.draw(win)
            pt = win.getMouse()
            # cannon.setPos(pt)
            pos.setText("curPos: {0:.2f},{1:.2f}".format(
                pt.getX(), pt.getY()))
            win.getMouse()
            posPrompt.undraw()

        pt = win.getMouse()
        fMsg.undraw()
        fAngle.undraw()

    win.close()


main()
