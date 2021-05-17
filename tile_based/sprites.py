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
    def __init__(self, game, x, y):
        self.groups = game.allSprites, game.playersGroup
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(DEEP_GREY)
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILE_SIZE
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.keypressed = False

    def getKeys(self):
        self.vel = vec(0, 0)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.vel.x = -PLYR_SPEED
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.vel.x = PLYR_SPEED
        if keystate[pg.K_UP] or keystate[pg.K_w]:
            self.vel.y = -PLYR_SPEED
        if keystate[pg.K_DOWN] or keystate[pg.K_s]:
            self.vel.y = PLYR_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def collideWalls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y
    def update(self):
        self.getKeys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collideWalls('x')
        self.rect.y = self.pos.y
        self.collideWalls('y')

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

