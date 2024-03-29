# ---Sprite(s)---

# You can either use this as either:
# a file for one sprite, or all of your sprites.

# If you use only one file for sprites, move the file to the main folder

### imports ###
import pygame as pg
import os
from settings import *
vec = pg.math.Vector2
from tilemap import collide_hitRect
from random import uniform


def collideWalls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hitRect)
        if hits:
            if hits[0].rect.centerx > sprite.hitRect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hitRect.width / 2
            if hits[0].rect.centerx < sprite.hitRect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hitRect.width / 2
            sprite.vel.x = 0
            sprite.hitRect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hitRect)
        if hits:
            if hits[0].rect.centery > sprite.hitRect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hitRect.height / 2
            if hits[0].rect.centery < sprite.hitRect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hitRect.height / 2
            sprite.vel.y = 0
            sprite.hitRect.centery = sprite.pos.y

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

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites, game.playersGroup
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.playerImg
        self.rect = self.image.get_rect()
        self.hitRect = PLYR_HIT_RECT
        self.hitRect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILE_SIZE
        self.rot = 0
        self.rotSpeed = 0
        self.lastShot = 0
        self.hp = PLYR_HP

    def getKeys(self):
        self.rotSpeed = 0
        self.vel = vec(0, 0)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.rotSpeed = PLYR_ROT_SPEED
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.rotSpeed = -PLYR_ROT_SPEED
        if keystate[pg.K_UP] or keystate[pg.K_w]:
            self.vel = vec(PLYR_SPEED, 0).rotate(-self.rot)
        if keystate[pg.K_DOWN] or keystate[pg.K_s]:
            self.vel = vec(-PLYR_SPEED / 1.5, 0).rotate(-self.rot)
        if keystate[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.lastShot > BULLET_RATE:
                self.lastShot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.game, pos, dir)
                self.vel = vec(-KICKBACK, 0).rotate(-self.rot)

    def update(self):
        self.getKeys()
        self.rot = (self.rot + self.rotSpeed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.playerImg, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hitRect.centerx = self.pos.x
        collideWalls(self, self.game.walls, 'x')
        self.hitRect.centery = self.pos.y
        collideWalls(self, self.game.walls, 'y')
        self.rect.center = self.hitRect.center

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
        # self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image = game.wallImg
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x*TILE_SIZE
        self.rect.y = y*TILE_SIZE


class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mobImg
        self.rect = self.image.get_rect()
        self.hitRect = MOB_HIT_RECT.copy()
        self.hitRect.center = self.rect.center
        self.pos = vec(x, y) * TILE_SIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.hp = 100

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pg.transform.rotate(self.game.mobImg, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(MOB_SPEED, 0).rotate(-self.rot)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hitRect.centerx = self.pos.x
        collideWalls(self, self.game.walls, 'x')
        self.hitRect.centery = self.pos.y
        collideWalls(self, self.game.walls, 'y')
        self.rect.center = self.hitRect.center
        if self.hp <= 0:
            self.kill()

    def drawHealth(self):
        if self.hp > 60:
            col = GREEN
        elif self.hp > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.hp / MOB_HP)
        self.hpBar = pg.Rect(0, 0, width, 7)
        if self.hp < MOB_HP:
            pg.draw.rect(self.image, col, self.hpBar)


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.groups = game.allSprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bulletImg
        self.image = pg.transform.scale(self.image, (10, 10))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-GUN_SPREAD, GUN_SPREAD)
        self.vel = dir.rotate(spread) * BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > BULLET_LV_TIME:
            self.kill()
