"""
Blockade is competitive arcade game. It has two players. Player 1 is a white
block that is continually moving forward. Player 2’s job is to stop Player 1 by
throwing obstacles in its way. Player 1 can avoid obstacles by jumping over or
ducking under them. Both players are limited by a stamina bar. Actions such
jumping or throwing obstacles depletes player’s stamina and if the stamina gets
too low players cannot perform actions. The game uses keyboard inputs as commands.

@author: Vivien Chen and Harrison Young
"""


import os, sys
import pygame
from random import randint

from models import *
from config import *


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
        self.oneplayer = True


    def start_menu(self):
        """Start screen for game."""
        while True:
            if pygame.QUIT in {event.type for event in pygame.event.get()}:
                sys.exit()

            # display start menu
            self.screen.fill(colors['BLACK'])
            # title
            font = pygame.font.SysFont("comicsansms", int(self.width/8))
            text = font.render("Blockade", True, colors['WHITE'])
            text_rect = text.get_rect(center=(self.width/2, self.height/3))
            self.screen.blit(text, text_rect)
            # instructions
            font = pygame.font.SysFont("comicsansms", int(self.width/30))
            text = font.render("Player 1: Arrow Keys, Player 2: ZXC", True, colors['WHITE'])
            text_rect = text.get_rect(center=(self.width/2, self.height/2))
            self.screen.blit(text, text_rect)
            # buttons
            self.button("One Player",self.width*1/8-20,self.height*3/4,colors['GREEN'],True,self.main_loop)
            self.button("Two Player",self.width*5/8-20,self.height*3/4,colors['RED'],False,self.main_loop)

            # update screen
            pygame.display.flip()


    def main_loop(self):
        """Main screen for game."""
        # start count
        count = 0

        # initialize player
        player = Player(PLAY_X, self.height-PLAY_LEN, PLAY_LEN, self.screen)

        # initialize stamina bars
        P1_stamina_bar = StaminaBar(self.screen, P1_STAMINA_BAR_OFFSET, 'WHITE')
        P2_stamina_bar = StaminaBar(self.screen, self.width - P2_STAMINA_BAR_OFFSET, 'RED')

        # initialize obstacle length, x and y coordinates
        OBS_X = self.width
        OBS_Y = self.height - OBS_LEN

        # create list of obstacles
        if self.oneplayer:
            obstacles = [Obstacle(OBS_X, OBS_Y, OBS_LEN, self.screen,'BLUE')]
        else:
            obstacles = []
            new_obstacle = False
            obstacle_height = OBS_Y

        # initialize time variables
        prev_time = 0
        obs_dt = 500

        # main event loop
        while True:
            count+=1
            # if pygame.QUIT in {event.type for event in pygame.event.get()}:
            #     sys.exit()
            # elif pygame.KEYDOWN in {event.type for event in pygame.event.get()}:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if not self.oneplayer:
                    # check keyboard for obstacle player
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_z:
                            new_obstacle = True
                            obstacle_height = OBS_Y-LEVEL_OFFSETS['ground']
                        if event.key == pygame.K_x:
                            new_obstacle = True
                            obstacle_height = OBS_Y-LEVEL_OFFSETS['first']
                        if event.key == pygame.K_c:
                            new_obstacle = True
                            obstacle_height = OBS_Y-LEVEL_OFFSETS['second']

            # check keyboard for main player
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP] and P1_stamina_bar.bars >= JUMP_COST:
                if player.play_y == (self.height - player.play_len):
                    P1_stamina_bar.decrease_bar(JUMP_COST)
                    player.jump()
                    P1_stamina_bar.draw()
            if pressed[pygame.K_LEFT]:
                player.move_left()
            if pressed[pygame.K_RIGHT]:
                player.move_right()

            # refresh screen
            self.screen.fill(colors['BLACK'])

            # update and draw player
            player.update()
            player.draw()

            # update current time
            current_time = pygame.time.get_ticks()

            if self.oneplayer:
                # generate obstacle at random time
                if (current_time - prev_time > obs_dt):
                    obstacles.append(Obstacle(OBS_X, OBS_Y, OBS_LEN, self.screen,'GREEN'))
                    prev_time = current_time
                    obs_dt = randint(250, 1000)
            if not self.oneplayer:
                # generate obstacle player's obstacle at appropriate height
                if (new_obstacle == True and P2_stamina_bar.bars >= OBSTACLE_COST):
                    new_obstacle = False
                    P2_stamina_bar.decrease_bar(OBSTACLE_COST)
                    obstacles.append(Obstacle(OBS_X, obstacle_height, OBS_LEN, self.screen,'RED'))

            # move each obstacle forward
            for obstacle in obstacles:
                obstacle.move_forward()
                obstacle.draw()
                # check for collision between player and obstacles
                if player.is_collide(obstacle.obs_x, obstacle.obs_y, obstacle.obs_len):
                    self.game_over(str(count))
            # remove obstacle from list if off screen
            obstacles = [obstacle for obstacle in obstacles if not obstacle.is_gone()]

            # update stamina bars
            P1_stamina_bar.increase_bar()
            P1_stamina_bar.draw()
            if not self.oneplayer:
                P2_stamina_bar.increase_bar(1.5)
                P2_stamina_bar.draw()

            # display score
            font = pygame.font.SysFont("comicsansms", int(self.width/8))
            text = font.render(str(count), True, colors['WHITE'])
            text_rect = text.get_rect(center=(self.width/2, self.height/8))
            self.screen.blit(text, text_rect)

            # update screen
            pygame.display.flip()
            self.clock.tick(30)


    def game_over(self, score):
        """Game over screen."""
        # main event loop
        while True:
            if pygame.QUIT in {event.type for event in pygame.event.get()}:
                sys.exit()

            # check keyboard for space key to restart game
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                self.main_loop()
            if pressed[pygame.K_v]:
                self.start_menu()

            # display game over screen
            self.screen.fill(colors['BLACK'])
            font = pygame.font.SysFont("comicsansms", int(self.width/16))
            text = font.render("Score: " + str(score), True, colors['WHITE'])
            text_rect = text.get_rect(center=(self.width/2, self.height*1/3))
            self.screen.blit(text,text_rect)
            text = font.render("Press Space Bar to play again", True, colors['WHITE'])
            text_rect = text.get_rect(center=(self.width/2, self.height*1/2))
            self.screen.blit(text,text_rect)
            text = font.render("Press V to go to home screen", True, colors['WHITE'])
            text_rect = text.get_rect(center=(self.width/2, self.height*2/3))
            self.screen.blit(text,text_rect)

            # update screen
            pygame.display.flip()


    def button(self, msg, x, y, color, oneplayer, action=None):
        "Button for start screen."
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        font = pygame.font.SysFont("comicsansms", int(self.width/20))
        text = font.render(msg, True, colors['WHITE'])
        w = self.width/3
        h = self.width/12

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.screen, color, (x,y,w,h))

            if click[0] == 1 and action != None:
                self.oneplayer = oneplayer
                action()
        else:
            pygame.draw.rect(self.screen, colors['BLACK'], (x,y,w,h))

        self.screen.blit(text,[x+20,y])


if __name__ == "__main__":
    Game4Main().start_menu()
