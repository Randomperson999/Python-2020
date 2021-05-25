# Art from Kenney (http://kenney.nl/assets/top-down-shooter)

import pygame as pg
import random as r
import math as m
import os
from os import path
from settings import *
from sprites import *
import sys
from tilemap import *

# HUD functions

def draw_playerHealth(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LEN = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LEN
    outlineRect = pg.Rect(x, y, BAR_LEN, BAR_HEIGHT)
    fillRect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fillRect)
    pg.draw.rect(surf, WHITE, outlineRect, 2)


class Game(object):
    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(250, 50)
        self.loadData()
    # def loadImg(self):
    #     self.playerImg = pg.image.load(os.path.join(imageFolder, "img.png")).convert

    def loadData(self):
        self.map = Map(path.join(gameFolder, 'map2.txt'))
        self.playerImg = pg.image.load(path.join(imageFolder, PLAYER_IMG)).convert_alpha()
        self.mobImg = pg.image.load(path.join(imageFolder, MOB_IMG)).convert_alpha()
        self.wallImg = pg.image.load(path.join(imageFolder, WALL_IMG)).convert_alpha()
        self.wallImg = pg.transform.scale(self.wallImg, (TILE_SIZE, TILE_SIZE))
        self.spritesheet1 = Spritesheet(os.path.join(imageFolder, SPRITESHEET))
        self.spritesheet2 = Spritesheet(os.path.join(imageFolder, SPRITESHEET2))
        self.bulletImg = pg.image.load(path.join(imageFolder, BULLET_IMG)).convert_alpha()

    def newGame(self):
        """starts a new game"""

        # create new groups

        self.allSprites = pg.sprite.Group()
        self.playersGroup = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()

        # game objects
        self.camera = Camera(self.map.width, self.map.height)

        for row, tiles in enumerate(self.map.mapData):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)


        # add objects to sprite groups
        self.run()

    def run(self):
        """runs the game"""
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    def events(self):
        """Game Loop - Events"""
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_x:
                    self.quit()

    def update(self):
        """Game Loop - Update"""
        self.allSprites.update()
        self.camera.update(self.player)
        # mobs hit player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hitRect)
        for hit in hits:
            self.player.hp -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.hp <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # bullets hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.hp -= BULLET_DAMAGE
            print(hit.hp)
            hit.vel = vec(0, 0)
    def drawGrid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, BLACK, (0, y), (WIDTH, y))
    def draw(self):
        """Game Loop - Draw"""
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BG_COLOR)
        # self.drawGrid()
        for sprite in self.allSprites:
            if isinstance(sprite, Mob):
                sprite.drawHealth()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pg.draw.rect(self.screen, WHITE, self.player.hitRect, 2)
        # HUD functions
        draw_playerHealth(self.screen, 10, 10, self.player.hp / PLYR_HP)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()
    def startScreen(self):
        pass

    def gameOver(self):
        pass

    def options(self):
        pass


g = Game()
g.startScreen()


while g.running:
    g.newGame()
    g.gameOver()

pg.quit()


