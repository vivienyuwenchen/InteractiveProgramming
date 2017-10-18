import os, sys
import pygame
from random import randint
from misc import Obstacle, colors


class Game4Main:
    """The Main Game4 Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=360,height=240):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))

        self.clock = pygame.time.Clock()


    def mainLoop(self):
        done = False

        rect_side = 10
        rect_x = self.width
        rect_y = self.height - rect_side

        prev_time = 0
        obstacles = [Obstacle(rect_x, rect_y, rect_side, self.screen)]
        delta = 500

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.screen.fill(colors['BLACK'])

            current_time = pygame.time.get_ticks()

            if current_time - prev_time > delta:
                obstacles.append(Obstacle(rect_x, rect_y, rect_side, self.screen))
                prev_time = current_time
                delta = randint(500, 3000)

            for obstacle in obstacles:
                obstacle.moveForward()

            obstacles = [obstacle for obstacle in obstacles if not obstacle.isGone()]
            #print(obstacles)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    MainWindow = Game4Main()
    MainWindow.mainLoop()
