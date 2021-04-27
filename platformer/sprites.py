#  - --- Sprite(s) --- -

# You can either use this as either:
# a file for one sprite, or all of your sprites.

# If you use only one file for sprites, move the file to the main folder

#  - - imports - -
import pygame as pg
import os
from settings import *
import random as r

vec = pg.math.Vector2
# Classes
class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def getImage(self, x, y, width, height):
        """ grab an image out of a larger spritesheet"""
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        return image
# Sprites
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.currentFrame = 0
        self.lastUpdate = 0
        self.loadImgs()
        self.image = self.standing_frames[0]
        # self.image.fill(DARKER_GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 50)
        self.pos = vec(40, HEIGHT - 50)
        self.ang = 10
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)



        self.keypressed = False

    def update(self):
        self.animate()
        # flow movement
        self.acc = vec(0, PLAYER_GRAV)
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
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0

        self.rect.midbottom = self.pos
        self.loopBorder()

    def loadImgs(self):
        self.standing_frames = [self.game.spritesheet.getImage(614, 1063, 120, 191),
                                self.game.spritesheet.getImage(690, 406, 120, 201)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)
        self.walk_frames_r = [self.game.spritesheet.getImage(678, 860, 120, 201),
                              self.game.spritesheet.getImage(692, 1458, 120, 207)]
        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))
        self.jumpFrame = self.game.spritesheet.getImage(382, 763, 150, 181)
        self.jumpFrame.set_colorkey(BLACK)
    def jump(self):
        # jump only if standing on something
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        if hits:
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

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        # walk animation
        if self.walking:
            if now - self.lastUpdate > 180:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self. vel.x > 0:
                    self.image = self.walk_frames_r[self.currentFrame]
                else:
                    self.image = self.walk_frames_l[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        # idle animation
        if not self.jumping and not self.walking:
            if now - self.lastUpdate > 350:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.standing_frames)
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        images = [self.game.spritesheet.getImage(0, 96, 380, 94),
                  self.game.spritesheet.getImage(382, 408, 200, 100)]
        self.image = r.choice(images)
        # self.image.fill(DARK_GREEN)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
