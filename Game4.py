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
        self.score = 0


    def mainLoop(self):
        """Main screen for game."""
        # initialize player
        count = 0
        play_len = 25
        play_x = 100
        play_y = self.height - play_len
        player = Player(play_x, play_y, play_len, self.screen)

        # initialize stamina bars
        P1_stamina_bar = StaminaBar(self.screen,25,"WHITE")
        P2_stamina_bar = StaminaBar(self.screen,350,"RED")

        # initialize obstacle length, x and y coordinates
        obs_len = 25
        obs_x = self.width
        obs_y = self.height - obs_len
        obstical_height = self.height - obs_len

        # create list of obstacles
        obstacles = []
        new_obstical = False
        # uncomment and place line below in [] of obstacles = [] to generate random obstacles:
        # Obstacle(obs_x, obs_y, obs_len, self.screen,'BLUE')


        # initialize time variables
        prev_time = 0
        obs_dt = 500

        # main event loop
        while 1:
            count+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # check keyboard for obstacle player
                if event.type == pygame.KEYDOWN:
                    # z to create obstacle at ground level
                    if event.key == pygame.K_z:
                        new_obstical = True
                        obstical_height = obs_y
                    # x to create obstacle at second level
                    if event.key == pygame.K_x:
                        new_obstical = True
                        obstical_height = obs_y-25
                    # c to create obstacle at third level
                    if event.key == pygame.K_c:
                        new_obstical = True
                        obstical_height = obs_y-50

            # check keyboard for main player
            pressed = pygame.key.get_pressed()
            # up to jump
            if pressed[pygame.K_UP] and P1_stamina_bar.bars >= player.jumpcost:
                if  player.play_y == (360 - player.play_len):
                    P1_stamina_bar.decreaseBarleft(player.jumpcost)
                    player.jump()
                    P1_stamina_bar.draw()
            # left to move left
            if pressed[pygame.K_LEFT]:
                player.moveLeft()
            # right to move right
            if pressed[pygame.K_RIGHT]:
                player.moveRight()

            # refresh screen
            self.screen.fill(colors['BLACK'])

            # update and draw player
            player.update()
            player.draw()

            # update current time
            current_time = pygame.time.get_ticks()

            # generate obstacle at random time
            if (current_time - prev_time > obs_dt):
                # uncomment below to generate random obstacles:
                # obstacles.append(Obstacle(obs_x, obs_y, obs_len, self.screen,'BLUE'))
                new_obstical = False
                prev_time = current_time
                obs_dt = randint(1000, 3000)
            # generate obstacle player's obstacle at appropriate height
            if (new_obstical == True and P2_stamina_bar.bars >= 33):
                new_obstical = False
                P2_stamina_bar.decreaseBarleft(33)
                obstacles.append(Obstacle(obs_x, obstical_height, obs_len, self.screen,'RED'))

            # move each obstacle forward
            for obstacle in obstacles:
                obstacle.moveForward()
                # check for collision between player and obstacles
                if player.isCollide(obstacle.obs_x, obstacle.obs_y, obstacle.obs_len):
                    self.gameOver(str(count))
            # remove obstacle from list if off screen
            obstacles = [obstacle for obstacle in obstacles if not obstacle.isGone()]

            # update stamina bars
            P1_stamina_bar.increaseBarleft()
            P2_stamina_bar.increaseBarleft(1.5)
            P1_stamina_bar.draw()
            P2_stamina_bar.draw()

            # display score
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render(str(count), True, (255,255,255))
            self.screen.blit(text,[200,10])

            # update screen
            pygame.display.flip()
            self.clock.tick(30)


    def gameOver(self,score):
        """Game over screen."""
        # main event loop
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # check keyboard for space key to restart game
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                self.mainLoop()

            # display game over screen
            self.screen.fill(colors['BLACK'])
            font = pygame.font.SysFont("comicsansms", 28)
            text = font.render("Player 1 recived a score of " + str(score), True, (255,255,255))
            self.screen.blit(text,[50,140])
            text = font.render("Press Space Bar to play again", True, (255,255,255))
            self.screen.blit(text,[50,178])

            # update screen
            pygame.display.flip()


if __name__ == "__main__":
    Game4Main().mainLoop()
