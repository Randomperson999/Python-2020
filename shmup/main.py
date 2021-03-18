# Caleb Keller
# 3/12/2021
# Asteroid like game
import pygame as pg
import random as r
import math
import Colors as c
from os import *

# Game Constants
####################################################################
HEIGHT = 700
WIDTH = 600
FPS = 60


title = "Shmup"

####################################################################

# Folders
####################################################################
game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder, "images")
player_imgs_folder = path.join(imgs_folder, "player")
enemy_imgs_folder = path.join(imgs_folder, "enemy")
bg_folder = path.join(imgs_folder, "background")
scores_folder = path.join(game_folder, "scores")
sounds_folder = path.join(game_folder, "sounds")
####################################################################
# initialize pygame and create window
####################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
####################################################################

# Game object classes
####################################################################


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.image = pg.Surface((50, 40))
        # self.image.fill(c.DARK_PURPLE)
        self.image = playerImg
        self.image = pg.transform.scale(self.image, (90, 90))
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx

        # flow movement
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        if keystate == pg.KEYUP:
            if pg.KEYUP == pg.K_LEFT or pg.K_a:
                self.speedx = 0
            if pg.KEYUP == pg.K_RIGHT or pg.K_d:
                self.speedx = 0
        # if keystate[pg.K_SPACE]:
        #     self.shoot()
        self.wallBorder()
    def wallBorder(self):

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0
    def shoot(self):
        b = Bullet(self.rect.centerx, self.rect.top+1)
        all_sprites.add(b)
        bullet_group.add(b)


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        # self.image = pg.Surface((5, 10))
        # self.image.fill(c.PURPLE)
        self.image = bulletImg
        self.image = pg.transform.scale(self.image, (5, 10))
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10
    def update(self):
        self.rect.y += self.speed
        # kill the bullet when leaving screen
        if self.rect.bottom < 0:
            self.kill()
            # print("kill")


class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        # self.image = pg.Surface((25, 25))
        # self.image.fill(c.DARK_RED)
        self.image = mpcImg
        self.image = pg.transform.scale(self.image, (40, 40))
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.75 /2)
        # pg.draw.circle(self.image, c.RED, self.rect.center, self.radius)
        self.rect.centerx = ((WIDTH / 2)+r.randint(-100, 100))
        self.rect.top = (0)
        self.speedy = r.randint(1, 8)
        self.speedx = r.randint(-3, 3)
        self.ang = 0

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # self.circle(5)
        self.screenWrap()

    def spawn(self):
        npc = NPC()
        npc_group.add(npc)
        all_sprites.add(npc)

    def screenWrap(self):
        if self.rect.right > WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.centerx = r.randint(10, 550)
            self.speedy = r.randint(1, 3)
            self.speedx = r.randint(-3, 3)
        # if self.rect.top < 0:
        #     self.rect.top = 0
        #     self.rect.centerx = r.randint(10, 550)
        #     self.speedy = r.randint(2, 5)
        #     self.speedx = r.randint(-1, 1)
    def circle(self, n):
        rad = self.ang * math.pi / 180
        self.rect.centery = -math.sin(rad) * n + self.rect.centery
        self.rect.centerx = math.cos(rad) * n + self.rect.centerx
        self.ang += 1
    #     if self.speedy < 3:
    #         self.speedy = 5
    #     self.screenWrap()

####################################################################
# load imgs
####################################################################
# I haven't made these yet, so it won't work.
background = pg.image.load(path.join(bg_folder, "bg.png")).convert()
bgRect = background.get_rect()
playerImg = pg.image.load(path.join(player_imgs_folder, "player.png")).convert()
mpcImg = pg.image.load(path.join(enemy_imgs_folder, "asteroid.png")).convert()
bulletImg = pg.image.load(path.join(player_imgs_folder, "bullet.png")).convert()
####################################################################

# create Sprite groups
####################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
####################################################################

# create Game Objects
####################################################################
player = Player()
npc = NPC()
for i in range(5):
    npc = NPC()
    npc_group.add(npc)
bullet = Bullet(100, WIDTH/2)
####################################################################

# add objects to sprite groups
####################################################################
players_group.add(player)
bullet_group.add(bullet)
npc_group.add(npc)

for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)
for i in bullet_group:
    all_sprites.add(i)
####################################################################

fails = 0
# Game Loop
###################
# game update Variables
########################################
playing = True

########################################
################################################################
while playing:
    # timing
    ##################################################
    clock.tick(FPS)
    ##################################################

    # collecting Input
    ##################################################

    # Quiting the game when we hit the x
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()
            if event.key == pg.K_ESCAPE:
                playing = False
        if event.type == pg.QUIT:
            playing = False

    ##################################################
    # Updates
    ##################################################
    all_sprites.update()

    # if npc hits plyr
    hits = pg.sprite.spritecollide(player, npc_group, True)
    # hits = pg.sprite.spritecollide(player, npc_group, True, pg.sprite.collide_circle())

    if hits:
        # playing = False
        npc.spawn()
        fails += 1
        print("B A D : "+str(fails))
    # if bullet hits npc
    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True)
    for hit in hits:
        npc.spawn()
    ##################################################
    # Render
    ##################################################

    screen.fill(c.BLACK)
    screen.blit(background, bgRect)
    all_sprites.draw(screen)

    pg.display.flip()
    ##################################################

pg.quit()
################################################################
#####################

