import pygame as pg
import random as r
import math as m
import os
from settings import *
from sprites import *
from game_functions import *


class Game(object):
    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)

    # def loadImg(self):
    #     self.playerImg = pg.image.load(os.path.join(imageFolder, "img.png")).convert
    def newGame(self):
        """starts a new game"""
        self.score = 0
        # create new groups

        self.allSprites = pg.sprite.Group()
        self.playersGroup = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        # game objects
        self.player = Player(self)

        p1 = makePlatform(0, HEIGHT - 20, WIDTH, 20)
        p2 = makePlatform(WIDTH/2 - 50, HEIGHT * 3/4, 100, 20)
        p3 = makePlatform(125, HEIGHT-350, 100, 20)
        p4 = makePlatform(255, HEIGHT-500, 80, 20)

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.allSprites.add(p)
            self.platforms.add(p)



        # add objects to sprite groups
        self.allSprites.add(self.player)
        self.playersGroup.add(self.player)
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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        """Game Loop - Update"""
        self.allSprites.update()
        # check if player hits platform - only if falling
        if self.player.vel.y >= 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top+1
                self.player.vel.y = 0
        # if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10
        # D I E
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.allSprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()

        if len(self.platforms) == 0:
            self.playing = False
        # spawn new platforms to keep same avg num

        while len(self.platforms) < 6:
            width = r.randrange(50, 100)
            p = Platform(r.randrange(0, WIDTH-width),
                         r.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.allSprites.add(p)

    def draw(self):
        """Game Loop - Draw"""
        self.screen.fill(BLACK)
        self.allSprites.draw(self.screen)
        self.drawText(str(self.score), 22, DARK_GREY, WIDTH/2, 15)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def drawText(self, txt, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(txt, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
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
