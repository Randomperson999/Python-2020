print(" ---- Game by Caleb Keller using tutorial. --------")
print(" --- 'Yipee' song by Snabisch (opengameart.org) ---")
print(" --- 'Happy Tune' by Suncopika (opengameart.org) --")
print(" --- Death and boost sounds by HaelDB -------------\n ---(opengameartorg)-------------------------------")
print(" --- Art from Kenney.nl ---------------------------")
print("\tYou might want to turn the volume down...")
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
        # cloud imgs
        self.cloudImgs = []
        for i in range(1, 4):
            self.cloudImgs.append(pg.image.load(path.join(img_dir, 'cloud{}.png'.format(i))).convert())
        # load sounds
        self.snd_dir = path.join(self.dir, 'snd')
        self.jumpSound = pg.mixer.Sound(path.join(self.snd_dir, 'Jump40.wav'))
        self.music = pg.mixer.Sound(path.join(self.snd_dir, 'Yippee.ogg'))
        self.music2 = pg.mixer.Sound(path.join(self.snd_dir, 'Happy Tune.ogg'))
        self.boostSound = pg.mixer.Sound(path.join(self.snd_dir, '1yell4.wav'))
        self.dethSound = pg.mixer.Sound(path.join(self.snd_dir, '1yell1.wav'))


    def newGame(self):
        """starts a new game"""
        self.score = 0
        # create new groups
        self.allSprites = pg.sprite.LayeredUpdates()
        self.playersGroup = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.powerUps = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.clouds = pg.sprite.Group()

        # game objects
        self.player = Player(self)
        for plat in PLATFORM_LIST:
            Platform(self, *plat)

        self.mobTimer = 0


        # add objects to sprite groups
        for i in range(8):
            c = Cloud(self)
            c.rect.y += 500
        pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        self.run()

    def run(self):
        """runs the game"""
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(10)
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
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jumpCut()

    def update(self):
        """Game Loop - Update"""
        self.allSprites.update()
        # spawn a mob?
        now = pg.time.get_ticks()
        if now-self.mobTimer > 5000 + r.choice([-1000, -500, 0, 500, 1000]):
            self.mobTimer = now
            Mob(self)
        # hit mobs?
        mob_hits = pg.sprite.spritecollide(self.player, self.mobs, False, pg.sprite.collide_mask)
        if mob_hits:
            self.dethSound.play()
            self.playing = False
        # check if player hits platform - only if falling
        if self.player.vel.y >= 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right +10 and \
                        self.player.pos.x > lowest.rect.left -10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top+1
                        self.player.vel.y = 0
                        self.player.jumping = False
        # if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT/4:
            if r.randrange(100) < 10:
                Cloud(self)
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for cloud in self.clouds:
                cloud.rect.y += max(abs(self.player.vel.y / 2), 2)

            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10
            for mob in self.mobs:
                mob.rect.y += max(abs(self.player.vel.y), 2)
                if mob.rect.top >= HEIGHT:
                    mob.kill()
        # if player hist powerup
        pow_hits = pg.sprite.spritecollide(self.player, self.powerUps, True)
        for pow in pow_hits:
            if pow.type == 'boost':
                self.boostSound.play()
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False
        # D I E
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.allSprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                self.dethSound.play()
                if sprite.rect.bottom < 0:
                    sprite.kill()
        # add in to test if player is fallen off of screen:  and self.player.pos.y > 900
        if len(self.platforms) == 0:
            self.playing = False

        # spawn new platforms to keep same avg num
        if len(self.platforms) < 6 and self.playing:
            # print("placing platforms, "+str(len(self.platforms)))
            width = r.randrange(50, 100)
            spe = r.choice([40, 80, 120, 160])

            Platform(self, r.randrange(0, WIDTH-width),
                         r.randrange(-75, -30)-spe)

    def draw(self):
        """Game Loop - Draw"""
        self.screen.fill(BG_COLOR)
        self.allSprites.draw(self.screen)
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
        pg.mixer.music.load(path.join(self.snd_dir, 'Happy Tune.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BG_COLOR)
        self.drawText(title, 48, BLACK, WIDTH / 2, HEIGHT / 4)
        self.drawText("Arrows to move space to jump", 22, BLACK, WIDTH / 2, HEIGHT / 2)
        self.drawText("You might want to turn the volume down...", 22, BLACK, WIDTH / 2, HEIGHT / 2+50)
        self.drawText("Press any key to play (except escape).", 22, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
        self.drawText("High Score: " + str(self.highscore), 22, BLACK, WIDTH / 2, 15)
        pg.display.flip()
        self.waiting()
        pg.mixer.music.fadeout(10)

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
        pg.mixer.music.load(path.join(self.snd_dir, 'Happy Tune.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BG_COLOR)
        self.drawText("GAME O V E R", 48, BLACK, WIDTH / 2, HEIGHT / 4)
        self.drawText("Score: " + str(self.score), 22, BLACK, WIDTH / 2, HEIGHT / 2)
        self.drawText("Press any key to play again (except escape).", 22, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.drawText("New high score!", 22, BLACK, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.drawText("High Score: " + str(self.highscore), 22, BLACK, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.waiting()
        pg.mixer.music.fadeout(10)
    def options(self):
        pass


g = Game()
g.startScreen()


while g.running:
    g.newGame()
    g.gameOver()

pg.quit()
