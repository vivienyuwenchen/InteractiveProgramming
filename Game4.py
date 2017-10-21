import os, sys
import pygame
from random import randint
from misc import Obstacle, Player, colors, jump


class Game4Main:
    """The Main Game4 Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=480,height=360):
        # initialize pygame
        pygame.init()
        # set window size
        self.width = width
        self.height = height
        # create screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        # create clock
        self.clock = pygame.time.Clock()


    def mainLoop(self):
        # initialize player
        play_len = 25
        play_x = 100
        play_y = self.height - play_len
        player = Player(play_x, play_y, play_len, self.screen)

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
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # check keyboard
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                player.jump()
            if pressed[pygame.K_LEFT]:
                player.moveLeft()
            if pressed[pygame.K_RIGHT]:
                player.moveRight()

            # refresh screen
            self.screen.fill(colors['BLACK'])
            #pygame.draw.rect(self.screen, colors['RED'], [0,self.height-(self.height/5),self.width,self.height/5])

            player.update()
            player.draw()

            # update current time
            current_time = pygame.time.get_ticks()

            # generate obstacle at random time
            if current_time - prev_time > obs_dt:
                obstacles.append(Obstacle(obs_x, obs_y, obs_len, self.screen))
                prev_time = current_time
                obs_dt = randint(1000, 3000)

            # move each obstacle forward
            for obstacle in obstacles:
                obstacle.moveForward()
                # check for collision between player and obstacles
                if player.isCollide(obstacle.obs_x, obstacle.obs_y, obstacle.obs_len):
                    self.gameOver()
            # remove obstacle from list if off screen
            obstacles = [obstacle for obstacle in obstacles if not obstacle.isGone()]

            # update screen
            pygame.display.flip()
            self.clock.tick(60)


    def gameOver(self):
        # main event loop
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # check keyboard
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                self.mainLoop()

            gameover = pygame.image.load("gameover.png")
            gameover = pygame.transform.scale(gameover, (int(3*self.width/4), int(self.height/2)))
            self.screen.blit(gameover, (int(self.width/8), int(self.height/4)))

            pygame.display.flip()


if __name__ == "__main__":
    Game4Main().mainLoop()
