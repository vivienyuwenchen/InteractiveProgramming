import os, sys
import pygame

colors = {'BLACK': (0, 0, 0),
            'WHITE' : (255, 255, 255),
            'GREEN' : (0, 255, 0),
            'RED' : (255, 0, 0),
            'BLUE' : (0, 0, 255),
            }

class Obstacle:

    def __init__(self, rect_x, rect_y, rect_side, screen):
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.rect_side = rect_side
        self.screen = screen

    def moveForward(self):
        self.rect_x -= 2
        pygame.draw.rect(self.screen, colors['BLUE'], [self.rect_x, self.rect_y, self.rect_side, self.rect_side])

    def isGone(self):
        return self.rect_x < 0
