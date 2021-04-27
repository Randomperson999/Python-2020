import pygame as pg
import random as r
import math as m
import os
from os import path
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
        self.running = True
        self.playing = False
        self.loadData()

    # def loadImg(self):
    #     self.playerImg = pg.image.load(os.path.join(imageFolder, "img.png")).convert
    def loadData(self):
        """Loads high score, images, ect."""
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'imgs')
        # high score
        with open(path.join(self.dir, HS_FILE), "r") as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        # spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))



    def newGame(self):
        """starts a new game"""
        self.score = 0
        # create new groups

        self.allSprites = pg.sprite.Group()
        self.playersGroup = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        # game objects
        self.player = Player(self)

        p1 = makePlatform(0, HEIGHT - 50)
        p2 = makePlatform(WIDTH/2 - 50, HEIGHT * 3/4)
        p3 = makePlatform(125, HEIGHT-350)
        p4 = makePlatform(255, HEIGHT-500)

        for plat in PLATFORM_LIST:
            p = Platform(self, *plat)
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
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
    def update(self):
        """Game Loop - Update"""
        self.allSprites.update()
        # check if player hits platform - only if falling
        if self.player.vel.y >= 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.y < lowest.rect.bottom:
                    self.player.pos.y = lowest.rect.top+1
                    self.player.vel.y = 0
        # if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)
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
            p = Platform(self, r.randrange(0, WIDTH-width),
                         r.randrange(-75, -30))
            self.platforms.add(p)
            self.allSprites.add(p)

    def draw(self):
        """Game Loop - Draw"""
        self.screen.fill(BG_COLOR)
        self.allSprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.drawText(str(self.score), 22, DARKISH_GREY, WIDTH/2, 15)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def drawText(self, txt, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(txt, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    def startScreen(self):
        self.screen.fill(BG_COLOR)
        self.drawText(title, 48, BLACK, WIDTH / 2, HEIGHT / 4)
        self.drawText("Arrows to move space to jump", 22, BLACK, WIDTH / 2, HEIGHT / 2)
        self.drawText("Press any key to play (except escape).", 22, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
        self.drawText("High Score: " + str(self.highscore), 22, BLACK, WIDTH / 2, 15)
        pg.display.flip()
        self.waiting()

    def waiting(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    return
                if event.type == pg.KEYUP:
                    if event.key != pg.K_ESCAPE:
                        waiting = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                        return


    def gameOver(self):
        """Displays game over screen."""
        if not self.running:
            return
        self.screen.fill(BG_COLOR)
        self.drawText("GAME O V E R", 48, BLACK, WIDTH / 2, HEIGHT / 4)
        self.drawText("Score: " + str(self.score), 22, BLACK, WIDTH / 2, HEIGHT / 2)
        self.drawText("Press any key to play again", 22, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.drawText("New high score!", 22, BLACK, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.drawText("High Score: " + str(self.highscore), 22, BLACK, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.waiting()
    def options(self):
        pass


g = Game()
g.startScreen()


while g.running:
    g.newGame()
    g.gameOver()

pg.quit()
