import pygame as pg
import random as r
import math as m
import os
from settings import *
from sprites import *


class Game(object):
    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
    # def loadImg(self):
    #     self.playerImg = pg.image.load(os.path.join(imageFolder, "img.png")).convert
    def newGame(self):
        """starts a new game"""

        # create new groups

        self.allSprites = pg.sprite.Group()
        self.playersGroup = pg.sprite.Group()
        self.platforms = pg.sprite.Group
        # game objects
        self.player = Player()
        self.p1 = Platform(0, HEIGHT - 30, WIDTH, 20)


        # add objects to sprite groups
        self.allSprites.add(self.player)
        self.playersGroup.add(self.player)
        self.platforms.add(self.p1)
        self.allSprites.add(self.p1)
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
                if self.playing:
                    self.playing = False
                self.running = False
    def update(self):
        """Game Loop - Update"""
        self.allSprites.update()

    def draw(self):
        """Game Loop - Draw"""
        self.screen.fill(BLACK)
        self.allSprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

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
