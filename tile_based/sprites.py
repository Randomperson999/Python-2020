# ---Sprite(s)---

# You can either use this as either:
# a file for one sprite, or all of your sprites.

# If you use only one file for sprites, move the file to the main folder

### imports ###
import pygame as pg
import os
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites, game.playersGroup
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(DEEP_GREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.ang = 10
        # self.speedX = 0
        # self.speedY = 0
        self.keypressed = False

    def move(self, dx=0, dy=0):
        if not self.collideWalls(dx, dy):
            self.x += dx
            self.y += dy
    def collideWalls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    def update(self):
        # flow movement
        # self.speedX = 0
        # self.speedY = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.move(dx=-1)
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.move(dx=1)
        if keystate[pg.K_UP] or keystate[pg.K_w]:
            self.move(dy=-1)
        if keystate[pg.K_DOWN] or keystate[pg.K_s]:
            self.move(dy=1)
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE
        # self.loopBorder()

    def toggle_pressed(self):
        self.keypressed = False

    def wallBorder(self):

        if self.rect.right >= WIDTH+1:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= HEIGHT+1:
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

    def bounceBorder(self):

        if self.rect.right >= WIDTH - 1 or self.rect.left <= 0:
            self.speedX = -self.speedX
        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.speedY = -self.speedY

    def loopBorder(self):
        if self.rect.right > WIDTH+32:
            self.rect.left = 0
        if self.rect.left < -32:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT+32:
            self.rect.top = 0
        if self.rect.top < -32:
            self.rect.bottom = HEIGHT

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(SILVER)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x*TILE_SIZE
        self.rect.y = y*TILE_SIZE

