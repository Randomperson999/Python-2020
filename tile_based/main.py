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


    def newGame(self):
        """starts a new game"""

        # create new groups

        self.allSprites = pg.sprite.Group()
        self.playersGroup = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()

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
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pg.draw.rect(self.screen, WHITE, self.player.hitRect, 2)
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


