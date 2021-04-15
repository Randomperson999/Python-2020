# ---Sprite(s)---

# You can either use this as either:
# a file for one sprite, or all of your sprites.

# If you use only one file for sprites, move the file to the main folder

### imports ###
import pygame as pg
import os
from settings import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.image = pg.Surface((25, 25))
        self.image.fill(DEEP_RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.ang = 10
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)



        self.keypressed = False

    def update(self):
        # flow movement
        self.acc = vec(0, 0.5)
        # self.speedY = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        # friction
        self.acc.x += self.vel.x * PLAYER_FRIC
        # motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.center = self.pos
        self.wallBorder()



    def toggle_pressed(self):
        self.keypressed = False

    def wallBorder(self):

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < 0:
            self.pos.y = 0

    def bounceBorder(self):

        if self.rect.right >= WIDTH - 1 or self.rect.left <= 0:
            self.speedX = -self.speedX
        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.speedY = -self.speedY
    def screenWrap(self):
        if self.rect.right > WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Platform, self).__init__()
        self.image = pg.Surface((w, h))
        self.image.fill(DARK_PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
