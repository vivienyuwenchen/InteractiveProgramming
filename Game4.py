import os, sys
import pygame
from random import randint
from misc import Obstacle, Player, colors, jump


class Game4Main:
    """The Main Game4 Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=600,height=480):
        # initialize pygame
        pygame.init()
        # set window size
        self.width = width
        self.height = height
        # create screen
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        # initialize clock
        self.clock = pygame.time.Clock()


    def mainLoop(self):
        done = False

        # initialize player
        jumping = False
        frames = 0
        startjump = 0
        x_min = 0
        x_max = 200
        play_len = 25
        play_x = 100
        play_y = self.height - play_len

        # initialize obstacle length, x and y coordinates
        obs_len = 25
        obs_x = self.width
        obs_y = self.height - obs_len
        # create list of obstacles with first obstacle
        obstacles = [Obstacle(obs_x, obs_y, obs_len, self.screen)]

        # initialize time variables
        prev_time = 0
        obs_dt = 500

        # main event loop
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # keyboard stuff
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                if frames - startjump > 20:
                    jumping = True
                    startjump = frames
            if pressed[pygame.K_LEFT]:
                if play_x > x_min:
                    play_x -= 5
            if pressed[pygame.K_RIGHT]:
                if play_x < x_max:
                    play_x += 5

            # refresh screen
            self.screen.fill(colors['BLACK'])
            #pygame.draw.rect(self.screen, colors['RED'], [0,self.height-(self.height/5),self.width,self.height/5])

            jumpclock = frames%21
            jumpover = False

            if jumping == True:
                play_y = jump(frames-startjump+1,self.height-125, self.height)[0]
                jumpover = jump(frames-startjump+1,self.height-125, self.height)[1]
            if jumpover == True:
                jumping = False

            pygame.draw.rect(self.screen, colors['WHITE'], [play_x,play_y,play_len,play_len])

            # update current time
            current_time = pygame.time.get_ticks()

            # generate obstacle at random time
            if current_time - prev_time > obs_dt:
                obstacles.append(Obstacle(obs_x, obs_y, obs_len, self.screen))
                prev_time = current_time
                obs_dt = randint(500, 2000)

            # move each obstacle forward
            for obstacle in obstacles:
                obstacle.moveForward()

            # remove obstacle from list if off screen
            obstacles = [obstacle for obstacle in obstacles if not obstacle.isGone()]

#            if player.isDead():
#                pygame.image.load("game_over.png")

            # update screen
            pygame.display.flip()
            frames+=1
            self.clock.tick(60)


if __name__ == "__main__":
    Game4Main().mainLoop()
