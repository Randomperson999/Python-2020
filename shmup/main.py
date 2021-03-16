import pygame as pg
import random as r
import math
import Colors as c
from os import *





# ###############
# Game object classes
####################################################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 40))
        self.image.fill(c.DARK_PURPLE)
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
        self.image = pg.Surface((5, 10))
        self.image.fill(c.PURPLE)
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
        self.imageOrig = pg.Surface((25, 25))
        self.imageOrig.fill(c.DARK_RED)
        self.image = self.imageOrig.copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.top = (0)
        self.speedy = r.randint(1, 8)
        self.speedx = r.randint(-3, 3)
        self.ang = 0
        self.rot = 0
        self.rotSpeed = r.randint(-8, 8)
        self.lastUpdate = pg.time.get_ticks()

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # self.circle(5)
        self.screenWrap()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.lastUpdate > 60:
            self.lastUpdate = now
            # do the rotation
            self.rot = (self.rot+self.rotSpeed) % 360
            newImage = pg.transform.rotate(self.imageOrig, self.rot)
            oldCenter = self.rect.center
            self.image = newImage
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter

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
            self.speedy = r.randint(2, 5)
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
# game functions:
####################################################################
def drawText(surf, text, size, x, y, color):
    font = pg.font.Font(font_name, size)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.midtop = (x, y)
    surf.blit(textSurface, textRect)
####################################################################
# Game Constants
####################################################################
HEIGHT = 900
WIDTH = 600
FPS = 60


title = "Shmup"
font_name = pg.font.match_font("arial")

####################################################################

# initialize pygame and create window
####################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
####################################################################

# load imgs
####################################################################

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
for i in range(10):
    npc = NPC()
    npc_group.add(npc)
####################################################################

# add objects to sprite groups
####################################################################
players_group.add(player)
npc_group.add(npc)

for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)
for i in bullet_group:
    all_sprites.add(i)
####################################################################


# Game Loop
###################
# game update Variables
########################################
playing = True
score = 0
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
                player.shoot( )
            if event.key == pg.K_ESCAPE:
                playing = False
        if event.type == pg.QUIT:
            playing = False

    ##################################################
    # Updates
    ##################################################
    all_sprites.update()

    # if npc hits plyr
    hits = pg.sprite.spritecollide(player, npc_group, False)
    if hits:
        playing = False
        npc.spawn()
    # if bullet hits npc
    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True)
    for hit in hits:
        # score += 50 - hit.radius
        score += 10
        npc.spawn()


    ##################################################
    # Render
    ##################################################

    screen.fill(c.BLACK)
    all_sprites.draw(screen)
    # draw hud
    drawText(screen, "Score: "+str(score), 18, WIDTH/2, 10, c.DARK_RED)
    pg.display.flip()

    ##################################################

pg.quit()
################################################################
#####################

