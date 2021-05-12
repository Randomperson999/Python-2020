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
    def __init__(self, game):
        self._layer = PLAYER_LYR
        self.groups = game.allSprites, game.playersGroup
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.jumping = False
        self.currentFrame = 0
        self.lastUpdate = 0
        # self.image.fill(DARKER_GREY)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE*2))
        self.image.fill(DEEP_GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 50)
        self.pos = vec(80, HEIGHT - 50)
        self.ang = 10
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)



        self.keypressed = False

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
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
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        if abs(self.vel.y) < 0.1:
            self.vel.y = 0
        if pg.sprite.spritecollideany(self, self.game.blocks):
            self.vel.x = -self.vel.x
            self.vel.y = -self.vel.y
        self.rect.midbottom = self.pos

        self.loopBorder()

    def jumpCut(self):
        if self.jumping:
            if self.vel.y < -.1:
                self.vel.y = -.1

    def jump(self):
        # jump only if standing on something
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self, self.game.blocks, False)
        self.rect.x -= 2
        if hits and not self.jumping:
            lowest = hits[0]
            for hit in hits:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            if self.pos.y < lowest.rect.centery:
                self.jumping = True
                self.vel.y = -PLAYER_JUMP

    def toggle_pressed(self):
        self.keypressed = False

    def wallBorder(self):

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        # if self.pos.y > HEIGHT:
        #     self.pos.y = HEIGHT
        # if self.pos.y < 0:
        #     self.pos.y = 0

    def loopBorder(self):

        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2
        # if self.pos.y > HEIGHT:
        #     self.pos.y = HEIGHT
        # if self.pos.y < 0:
        #     self.pos.y = 0

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



class Block(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites, game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(SILVER)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x*TILE_SIZE
        self.rect.y = y*TILE_SIZE


