import pygame
from pygame.locals import *
import time
from sys import exit
pygame.init()
def jump(ctime, startloc):
    """
    Changes the y position up one frame
    #for i in range(21):

        #print(jump(i,0)[1])
    """
    over = False
    h = 100
    t = 20
    b = startloc
    c = t/2
    a =  h/((t/2)**2)
    x = (ctime%20)
    recty = (a*(x - c)**2)+b


    if (x == 0):
        over = True
    return [recty, over]
