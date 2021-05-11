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
        image = pg.transform.scale(image, (width // 3, height // 3))
        return image
# Sprites
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
        if abs(self.vel.y) < 0.1:
            self.vel.y = 0
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

    def jumpCut(self):
        if self.jumping:
            if self.vel.y < -.1:
                self.vel.y = -.1

    def jump(self):
        # jump only if standing on something
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        if hits and not self.jumping:
            lowest = hits[0]
            for hit in hits:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            if self.pos.y < lowest.rect.centery:
                self.jumping = True
                self.vel.y = -PLAYER_JUMP
                self.game.jumpSound.play()

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
        if self.jumping:
            self.image = self.jumpFrame
            bottom = self.rect.bottom
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        self.mask = pg.mask.from_surface(self.image)

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLATFORM_LYR
        self.groups = game.allSprites, game.platforms
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        images = [self.game.spritesheet.getImage(0, 96, 380, 94),
                  self.game.spritesheet.getImage(382, 408, 200, 100),
                  self.game.spritesheet.getImage(0, 288, 380, 94),
                  self.game.spritesheet.getImage(213, 1662, 201, 100)]
        self.image = r.choice(images)
        # self.image.fill(DARK_GREEN)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if r.randrange(100) < POW_SPAWN_PCT:
            PwrUp(self.game, self)


class PwrUp(pg.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = POWER_LAYER
        self.groups = game.allSprites, game.powerUps
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = r.choice(["boost"])
        self.image = self.game.spritesheet.getImage(820, 1805, 71, 70)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()


class Mob(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = MOB_LYR
        self.groups = game.allSprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.imageUp = self.game.spritesheet.getImage(692, 1667, 120, 132)
        self.imageUp.set_colorkey(BLACK)
        self.imageDown = self.game.spritesheet.getImage(698, 1801, 120, 128)
        self.imageDown.set_colorkey(BLACK)
        self.image = self.imageUp
        self.rect = self.image.get_rect()
        self.rect.centerx = r.choice([-100, WIDTH+100])
        self.vx = r.randrange(1, 4)
        if self.rect.centerx > WIDTH:
            self.vx *= -1
        self.rect.y = r.randrange(HEIGHT / 2)
        self.vy = 0
        self.dy = 0.5

    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy > 3 or self.vy < -3:
            self.dy *= -1
        center = self.rect.center
        if self.dy < 0:
            self.image = self.imageUp
        else:
            self.image = self.imageDown
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.center = center
        self.rect.y += self.vy
        if self.rect.left > WIDTH+100 or self.rect.right < -100:
            self.kill()


class Cloud(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = CLOUD_LAYER
        self.groups = game.allSprites, game.clouds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = r.choice(game.cloudImgs)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        scale = r.randrange(50, 101) / 100
        self.image = pg.transform.scale(self.image, (int(self.rect.width * scale),
                                                     int(self.rect.height * scale)))

        self.rect.x = r.randrange(WIDTH - self.rect.width)
        self.rect.y = r.randrange(-500, -50)

    def update(self):
        if self.rect.top > HEIGHT * 2:
            self.kill()
