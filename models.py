import os, sys
import pygame

from config import *


class Obstacle:
    """A square obstacle, defined by its top left hand coordinate, length, and color.
    Also takes in screen as an argument to draw the obstacle."""
    def __init__(self, obs_x, obs_y, obs_len, screen, color):
        """Initialize the instance."""
        self.obs_x = obs_x              # top left hand x coordinate
        self.obs_y = obs_y              # top left hand y coordinate
        self.obs_len = obs_len          # side length
        self.screen = screen            # game screen
        self.color = color              # color of obstacle

    def __repr__(self):
        return 'Obstacle({}, {}, {}, {})'.format(self.obs_x, self.obs_y, self.obs_len, self.screen)

    def draw(self):
        """Draw osbstacle based on top left hand coordinate and length."""
        pygame.draw.rect(self.screen, colors[self.color], [self.obs_x, self.obs_y, self.obs_len, self.obs_len])

    def move_forward(self):
        """Update horizontal location of obstacle."""
        self.obs_x -= 20

    def is_gone(self):
        """Check if obstacle is completely off screen."""
        return self.obs_x < -self.obs_len


class Player:
    """A square player, defined by its top left hand coordinate and length.
    Also takes in screen as an argument to draw the player."""
    def __init__(self, play_x, play_y, play_len, screen):
        """Initialize the instance."""
        self.play_x = play_x            # top left hand x coordinate
        self.play_y = play_y            # top left hand y coordinate
        self.play_len = play_len        # side length
        self.screen = screen            # game screen
        self.speed = 10                  # right/left speed
        self.jumpInProgress = False     # initialize to False
        self.v = 7.5                    # "velocity" for jump
        self.m = 2.5                    # "mass" for jump
        self.floor = play_y             # location of player before jump, used for comparison

    def draw(self):
        """Draw player based on top left hand coordinate and length."""
        pygame.draw.rect(self.screen, colors['WHITE'], [self.play_x, self.play_y, self.play_len, self.play_len])

    def move_right(self):
        """Update horizontal location of player after moving right."""
        if self.play_x < 300:
            self.play_x += self.speed

    def move_left(self):
        """Update horizontal location of player after moving left."""
        if self.play_x > 0:
            self.play_x -= self.speed

    def jump(self):
        """Set jumping status."""
        self.jumpInProgress = True

    def update(self):
        """Update height of player during jump."""
        if self.jumpInProgress:
            # change in height = "mass" times "velocity"
            dy = self.m * self.v

            # subtract height by change in height
            self.play_y -= dy
            # decrease velocity
            self.v -= .75

            # stop jumping if player has landed
            if self.play_y >= self.floor:
                # prevent player from falling through the floor
                self.play_y = self.floor
                # no longer jumping
                self.jumpInProgress = False
                # reset velocity
                self.v = 7.5

    def is_collide(self, obs_x, obs_y, obs_len):
        """Check collision of player with obstacle."""
        # set coordinates for top left hand corner (0) and bottom right hand corner (1) of obstacle
        obs_x0 = obs_x
        obs_x1 = obs_x + obs_len
        obs_y0 = obs_y
        obs_y1 = obs_y + obs_len
        # and of player
        play_x0 = self.play_x
        play_x1 = self.play_x + self.play_len
        play_y0 = self.play_y
        play_y1 = self.play_y + self.play_len
        # check if player coordinates within obstacle coordinates
        if (obs_x0 <= play_x0 <= obs_x1 or obs_x0 <= play_x1 <= obs_x1) and (obs_y0 <= play_y0 < obs_y1 or obs_y0 < play_y1 <= obs_y1):
            return True


class StaminaBar:
    """A stamina bar, defined by its starting location and color.
    Also takes in screen as an argument to draw the stamina bar."""
    def __init__(self, screen, start, color):
        self.screen = screen            # game screen
        self.start = start              # starting location of stamina bar
        self.color = color              # color of stamina bar
        self.bars = 100                 # initialize number of health bars

    def draw(self):
        """Draw stamina bar based on color, starting location, and number of health bars."""
        pygame.draw.rect(self.screen, colors[self.color], [self.start, 20, self.bars, 10])

    def decrease_bar(self, num_bars):
        """Decrease health bar by num_bars."""
        self.bars -= num_bars

    def increase_bar(self, speed = 1):
        """Increase health bar continuously if number of bars is lower than 100."""
        if self.bars < 100:
            self.bars += 1 * speed
