import os, sys
import pygame
from random import randint

from misc import *


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

        # initialize stamina bar
        P1_stamina_bar = StaminaBar(self.screen,25,"WHITE")
        P2_stamina_bar = StaminaBar(self.screen,350,"RED")

        # initialize obstacle length, x and y coordinates
        obs_len = 25
        obs_x = self.width
        obs_y = self.height - obs_len
        obstical_height = self.height - obs_len
        # create list of obstacles with first obstacle
        new_obstical = False
        #Obstacle(obs_x, obs_y, obs_len, self.screen,'BLUE')
        obstacles = []
        player_obsticals = []



        # initialize time variables
        prev_time = 0
        obs_dt = 500

        # main event loop
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        new_obstical = True
                        obstical_height = obs_y
                    if event.key == pygame.K_x:
                        new_obstical = True
                        obstical_height = obs_y-25
                    if event.key == pygame.K_c:
                        new_obstical = True
                        obstical_height = obs_y-50

            # check keyboard
            pygame.key.set_repeat(500, 30)
            down = pygame.key
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP] and P1_stamina_bar.bars >= 25:
                player.jump()
                P1_stamina_bar.decreaseBarleft(15)
                P1_stamina_bar.draw()
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
            if (current_time - prev_time > obs_dt):
                #obstacles.append(Obstacle(obs_x, obs_y, obs_len, self.screen,'BLUE'))
                new_obstical = False
                prev_time = current_time
                obs_dt = randint(1000, 3000)
            if (new_obstical == True and P2_stamina_bar.bars >= 33):
                new_obstical = False
                P2_stamina_bar.decreaseBarleft(33)
                obstacles.append(Obstacle(obs_x, obstical_height, obs_len, self.screen,'RED'))

            # move each obstacle forward
            for obstacle in obstacles:
                obstacle.moveForward()
                # check for collision between player and obstacles
                if player.isCollide(obstacle.obs_x, obstacle.obs_y, obstacle.obs_len):
                    self.gameOver()
            # remove obstacle from list if off screen
            obstacles = [obstacle for obstacle in obstacles if not obstacle.isGone()]
            P1_stamina_bar.increaseBarleft()
            P1_stamina_bar.draw()
            P2_stamina_bar.increaseBarleft()
            P2_stamina_bar.increaseBarleft()

            P2_stamina_bar.draw()
            # update screen
            pygame.display.flip()
            self.clock.tick(30)


    def gameOver(self):
        # main event loop
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # check keyboard
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                self.mainLoop()

            gameover = pygame.image.load("gameover.png")
            gameover = pygame.transform.scale(gameover, (int(3*self.width/4), int(self.height/2)))
            self.screen.blit(gameover, (int(self.width/8), int(self.height/4)))

            pygame.display.flip()


if __name__ == "__main__":
    Game4Main().mainLoop()
