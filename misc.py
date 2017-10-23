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
        self.obs_x -= 20
        pygame.draw.rect(self.screen, colors['BLUE'], [self.obs_x, self.obs_y, self.obs_len, self.obs_len])

    def isGone(self):
        return self.obs_x < -self.obs_len


class Player:

    def __init__(self, play_x, play_y, play_len, screen):
        self.play_x = play_x
        self.play_y = play_y
        self.play_len = play_len
        self.screen = screen
        self.speed = 5
        self.jumpInProgress = False
        self.v = 7.5
        self.m = 2.5
        self.floor = play_y

    def draw(self):
        pygame.draw.rect(self.screen, colors['WHITE'], [self.play_x, self.play_y, self.play_len, self.play_len])

    def moveRight(self):
        if self.play_x < 200:
            self.play_x += self.speed

    def moveLeft(self):
        if self.play_x > 0:
            self.play_x -= self.speed

    def jump(self):
        self.jumpInProgress = True

    def update(self):
        if self.jumpInProgress:
            dy = self.m * self.v

            self.play_y -= dy
            self.v -= .75

            if self.play_y >= self.floor:
                self.play_y = self.floor
                self.jumpInProgress = False
                self.v = 7.5

    def isCollide(self, obs_x, obs_y, obs_len):
        obs_x0 = obs_x
        obs_x1 = obs_x + obs_len
        obs_y0 = obs_y
        obs_y1 = obs_y + obs_len
        play_x0 = self.play_x
        play_x1 = self.play_x + self.play_len
        play_y0 = self.play_y
        play_y1 = self.play_y + self.play_len
        if play_x0 in range(obs_x0, obs_x1) or play_x1 in range(obs_x0, obs_x1):
            if play_y0 in range(obs_y0, obs_y1) or play_y1 in range(obs_y0, obs_y1):
                return True
        return False


class StaminaBar:

    def __init__(self, screen):
        self.screen = screen
        self.bars = 100
        self.clock = pygame.time.Clock()
        self.prev_time = 0
        self.player_jump = False

    def draw(self):
        pygame.draw.rect(self.screen, colors['WHITE'], [20, 20, self.bars, 10])

    def decreaseBar(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.prev_time >= 100:
            self.bars -= 10
            self.prev_time = current_time

    def increaseBar(self):
        if self.bars < 100:
            current_time = pygame.time.get_ticks()
            if current_time - self.prev_time >= 250:
                self.bars += 1
                self.prev_time = current_time
