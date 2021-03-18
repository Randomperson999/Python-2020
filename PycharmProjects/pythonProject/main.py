import pygame as pg
import random as r
import math as m
from os import *

# Game object classes
#------------------------------

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = (HEIGHT-(HEIGHT*.05))
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx


class Npc(pg.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pg.Surface((25,25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.top = (0)
        self.speedy = 0

    def update(self):
        self.rect.y += self.speedy
#------------------------------

# Constant
HEIGHT = 650
WIDTH = 500
FPS = 60
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Others

title = "Asteroid Thing"

# initialize pygame and create window

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()

# load imgs

#------------------------------

# create sprite groups
#------------------------------
allSprites = pg.sprite.Group()
playersGroup = pg.sprite.Group()
npcGroup = pg.sprite.Group()
#------------------------------

# create Game Objects
#------------------------------
player = Player()
npc = Npc()
#------------------------------

# add objects tp sprite groups
#------------------------------
playersGroup.add(player)
npcGroup.add(npc)

for i in playersGroup:
    allSprites.add(i)

for i in npcGroup:
    allSprites.add(i)
#------------------------------

# Game Loop

#----------

# game update variables
playing = True
#----------

#--------------------
while playing:
    # timing
    # --------------------
    clock.tick(FPS)
    # --------------------

    # collecting Input
    # --------------------
    # quitting game when closed
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
        if event.type == pg.QUIT:
            playing = False
    # --------------------

    #updates
    # --------------------
    allSprites.update()
    # --------------------

    # render
    # --------------------
    screen.fill(BLACK)
    allSprites.draw(screen)

    pg.display.flip()
    # --------------------







pg.quit()


