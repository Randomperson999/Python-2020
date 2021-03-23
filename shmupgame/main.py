# Caleb Keller
# 3/12/2021
# Asteroid like game
# Original shoot sound by: Jesús Lastra
# Original explosion from: WrathGames Studio [http://wrathgames.com/blog]
# Art by creator
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




# ###############
# Game object classes
####################################################################


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.sheild = 100
        # self.image = pg.Surface((50, 40))
        # self.image.fill(c.DARK_PURPLE)
        self.image = playerImg
        self.image = pg.transform.scale(self.image, (80, 80))
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.85 /2)
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
        self.speedx = 0
        self.shootDelay = 200
        self.lastShot = pg.time.get_ticks()
        self.lives = 3
        self.hideTimer = pg.time.get_ticks()
        self.hidden = False

    def hide(self):
        # hide player temporarily
        self.lives -= 1
        self.hidden = True
        self.hideTimer = pg.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def update(self):
        # unhide if hidden
        if self.hidden and (pg.time.get_ticks() - self.hideTimer > 1000):
            self.hidden = False
            self.rect.bottom = (HEIGHT - (HEIGHT * .05))
            self.rect.centerx = (WIDTH/2)
            self.sheild = 100
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
        if keystate[pg.K_SPACE]:
            self.shoot()
        self.wallBorder()
    def wallBorder(self):

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        # if self.rect.bottom >= HEIGHT:
        #     self.rect.bottom = HEIGHT
        # if self.rect.top <= 0:
        #     self.rect.top = 0
    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.lastShot > self.shootDelay and not self.hidden:
            shoot_snd.play()
            self.lastShot = now
            b = Bullet(self.rect.centerx, self.rect.top + 1)
            all_sprites.add(b)
            bullet_group.add(b)



    def hurt(self):
        pass


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
        npcImg = r.choice(npcList)
        self.imageOrig = npcImg
        sizeChange = r.randint(20, 90)
        self.imageOrig = pg.transform.scale(self.imageOrig,
                                            (30+sizeChange, 30+sizeChange))
        self.image = self.imageOrig.copy()
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.75 /2)
        # pg.draw.circle(self.image, c.RED, self.rect.center, self.radius)
        self.rect.centerx = ((WIDTH / 2)+r.randint(-100, 100))
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
            self.image.set_colorkey(c.BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter

    def spawn(self):
        npc = NPC()
        npc_group.add(npc)
        all_sprites.add(npc)

    def screenWrap(self):
        if self.rect.right > WIDTH:
            self.rect.top = 0
            self.rect.centerx = r.randint(10, 550)
            self.speedy = r.randint(1, 3)
            self.speedx = r.randint(-3, 3)
        if self.rect.left < 0:
            self.rect.top = 0
            self.rect.centerx = r.randint(10, 550)
            self.speedy = r.randint(1, 3)
            self.speedx = r.randint(-3, 3)
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

class Explosion(pg.sprite.Sprite):
    def __init__(self, center, size):
        super(Explosion, self).__init__()
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.lastUpdate = pg.time.get_ticks()
        self.frameRate = 50

    def update(self):
        now = pg.time.get_ticks()
        if now - self.lastUpdate > self.frameRate:
            self.lastUpdate =  now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
####################################################################
# game functions:
####################################################################


def drawText(surf, text, size, x, y, color):
    font = pg.font.Font(font_name, size)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.midtop = (x, y)
    surf.blit(textSurface, textRect)


def draw_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    barLen = 100
    barHeight = 10
    fill = (pct/100)*barLen
    outlineRect = pg.Rect(x, y, barLen, barHeight)
    fillRect = pg.Rect(x, y, fill, barHeight)
    pg.draw.rect(surf, c.DARKISH_PURPLE, fillRect)
    pg.draw.rect(surf, c.DARK_RED, outlineRect, 2)

def drawLives(surf, x, y, lives, img):
    for i in range(lives):
        imgRect = img.get_rect()
        imgRect.x = x + 30 * i
        imgRect.y = y
        surf.blit(img, imgRect)



####################################################################
# Game Constants
####################################################################
HEIGHT = 700
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
background = pg.image.load(path.join(bg_folder, "bg.png")).convert()
bgRect = background.get_rect()
playerImg = pg.image.load(path.join(player_imgs_folder, "player.png")).convert()
playerMiniImage = pg.transform.scale(playerImg, (25, 19))
playerMiniImage.set_colorkey(c.BLACK)
asteroidImages = []
npcList = [pg.image.load(path.join(enemy_imgs_folder, "asteroid.png")).convert(),
           pg.image.load(path.join(enemy_imgs_folder, "asteroid2.png")).convert(),
           pg.image.load(path.join(enemy_imgs_folder, "asteroid3.png")).convert()]
animationsFolder = path.join(imgs_folder, "animations")
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
for i in range(9):
    fn = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(animationsFolder, fn)).convert()
    img.set_colorkey(c.BLACK)
    img_lg = pg.transform.scale(img, (100, 100))
    img_sm = pg.transform.scale(img, (40, 40))
    explosion_anim["sm"].append(img_sm)
    explosion_anim["lg"].append(img_lg)

bulletImg = pg.image.load(path.join(player_imgs_folder, "bullet.png")).convert()
####################################################################
# load sounds
####################################################################

shoot_snd = pg.mixer.Sound(path.join(sounds_folder, "shoot.wav"))
expl_sound = pg.mixer.Sound(path.join(sounds_folder, "explosion1.wav"))

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

fails = 0
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
            # if event.key == pg.K_SPACE:
            #     player.shoot()
            if event.key == pg.K_ESCAPE:
                playing = False
        if event.type == pg.QUIT:
            playing = False

    ##################################################
    # Updates
    ##################################################
    all_sprites.update()

    # if npc hits plyr
    # hits = pg.sprite.spritecollide(player, npc_group, True)
    hits = pg.sprite.spritecollide(player, npc_group, True, pg.sprite.collide_circle)

    for hit in hits:
        # playing = False
        npc.spawn()
        expl = Explosion(hit.rect.center, "lg")
        expl_sound.play()
        all_sprites.add(expl)
        player.sheild -= hit.radius*2
        if player.sheild <=0:
            death_expl = Explosion(player.rect.center, "lg")
            all_sprites.add(death_expl)
            player.hide()
            if player.lives <= 0:
                playing = False


    # if bullet hits npc
    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True)
    for hit in hits:
        # score += 50 - hit.radius
        score += 10
        expl = Explosion(hit.rect.center, "lg")
        expl_sound.play()
        all_sprites.add(expl)
        npc.spawn()



    ##################################################
    # Render
    ##################################################
    screen.fill(c.BLACK)
    screen.blit(background, bgRect)
    all_sprites.draw(screen)
    # draw hud
    drawText(screen, "Score: "+str(score), 18, WIDTH/2, 10, c.DARK_RED)
    draw_bar(screen, 5, 10, player.sheild)
    drawLives(screen, WIDTH-100, 10, player.lives, playerMiniImage)
    pg.display.flip()

    ##################################################

pg.quit()
################################################################
#####################

