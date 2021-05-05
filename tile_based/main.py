import pygame as pg
import random as r
import math as m
import os
from os import path
from settings import *
from sprites import *
import sys

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
        self.mapData = []
        with open(path.join(gameFolder, 'map.txt'), 'rt') as f:
            for line in f:
                self.mapData.append(line)

    def newGame(self):
        """starts a new game"""

        # create new groups

        self.allSprites = pg.sprite.Group()
        self.playersGroup = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        # game objects
        self.player = Player(self, 10, 10)

        for row, tiles in enumerate(self.mapData):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)


        # add objects to sprite groups
        self.run()

    def run(self):
        """runs the game"""
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
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
                if event.key == pg.K_ESCAPE:
                    self.quit()
                # if event.key == pg.K_LEFT:
                #     self.player.move(dx=-1)
                # if event.key == pg.K_LEFT or event.key == pg.K_a:
                #     self.player.move(dx=-1)
                # if event.key == pg.K_RIGHT or event.key == pg.K_d:
                #     self.player.move(dx=1)
                # if event.key == pg.K_UP or event.key == pg.K_w:
                #     self.player.move(dy=-1)
                # if event.key == pg.K_DOWN or event.key == pg.K_s:
                #     self.player.move(dy=1)

    def update(self):
        """Game Loop - Update"""
        self.allSprites.update()
    def drawGrid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, BLACK, (0, y), (WIDTH, y))
    def draw(self):
        """Game Loop - Draw"""
        self.screen.fill(BG_COLOR)
        self.drawGrid()
        self.allSprites.draw(self.screen)
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


