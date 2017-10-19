import os, sys
import pygame


colors = {'BLACK': (0, 0, 0),
            'WHITE' : (255, 255, 255),
            'GREEN' : (0, 255, 0),
            'RED' : (255, 0, 0),
            'BLUE' : (0, 0, 255),
            }


class Obstacle:

    def __init__(self, obs_x, obs_y, obs_len, screen):
        self.obs_x = obs_x
        self.obs_y = obs_y
        self.obs_len = obs_len
        self.screen = screen

    def __repr__(self):
        return 'Obstacle({}, {}, {}, {})'.format(self.obs_x, self.obs_y, self.obs_len, self.screen)

    def moveForward(self):
        self.obs_x -= 2
        pygame.draw.rect(self.screen, colors['BLUE'], [self.obs_x, self.obs_y, self.obs_len, self.obs_len])

    def isGone(self):
        return self.obs_x < -self.obs_len


class Player:

    def __init__(self, play_x, play_y, play_len, screen):
        self.play_x = play_x
        self.play_y = play_y
        self.play_len = play_len
        self.screen = screen

#    def __repr__(self):
#        return 'Player({}, {}, {}, {})'.format(self.rect_x, self.rect_y, self.rect_side, self.screen)

def jump(ctime, startloc, height):
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
    play_y = ((a*(x - c)**2)+b)


    if (x == 0):
        over = True
    return [play_y, over]
        #pygame.draw.rect(self.screen, colors['BLUE'], [self.obs_x, self.obs_y, self.obs_len, self.obs_len])
