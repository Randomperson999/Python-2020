# Caleb Keller
# 3/12/2021
# Asteroid like game
# Original shoot sound by: Jesús Lastra
# Original explosion from: WrathGames Studio [http://wrathgames.com/blog]
# Music by Jordan Trudgett (tgfcoder)
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
font_name = pg.font.match_font("arial")

powerUps_list = ["lightning", "shield"]
powerUps_chance = ["shield", "lightning", "shield", "shield", "shield"]
POWERUP_TIME = 7000

####################################################################

# initialize pygame and create window
####################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
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
powerFolder = path.join(imgs_folder, "powers")
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
        self.speedy = 0
        self.shootDelay = 200
        self.lastShot = pg.time.get_ticks()
        self.lives = 3
        self.hideTimer = pg.time.get_ticks()
        self.hidden = False
        self.powerLevel = 1
        self.powTimer = pg.time.get_ticks()
        self.invulnerableTimer = pg.time.get_ticks()
        self.invulnerable = False
        self.ships_num = 1

    def hide(self):
        # hide player temporarily
        self.lives -= 1
        self.powerLevel = 1
        self.hidden = True
        self.hideTimer = pg.time.get_ticks()
        self.invulnerableTimer = pg.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)
        self.invulnerable = True
        # print("invulnerable?")

    def update(self):
        # time out powerups
        if self.powerLevel >= 2 and pg.time.get_ticks() - self.powTimer > POWERUP_TIME:
            self.powerLevel -= 1

            self.powTimer = pg.time.get_ticks()
        # unhide if hidden
        if self.hidden and (pg.time.get_ticks() - self.hideTimer > 1000):
            self.hidden = False
            self.rect.bottom = (HEIGHT - (HEIGHT * .05))
            self.rect.centerx = (WIDTH/2)
            self.sheild = 100
            # print(str.format("invulnerable?: {}", self.invulnerable))

        if pg.time.get_ticks() - self.invulnerableTimer > 5000:
            self.invulnerable = False
        # print(str.format("invulnerable?: {}", self.invulnerable))

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # flow movement
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        if keystate[pg.K_w] or keystate[pg.K_UP]:
            if self.rect.y > 500:
                self.speedy = -5
        if keystate[pg.K_s] or keystate[pg.K_DOWN]:
            self.speedy = 5

        if keystate == pg.KEYUP:
            if pg.KEYUP == pg.K_LEFT or pg.K_a:
                self.speedx = 0
            if pg.KEYUP == pg.K_RIGHT or pg.K_d:
                self.speedx = 0
            if pg.KEYUP == pg.K_UP or pg.K_w:
                self.speedy = 0
            if pg.KEYUP == pg.K_DOWN or pg.s:
                self.speedy = 0

        if keystate[pg.K_SPACE]:
            self.shoot()
        self.wallBorder()
    def wallBorder(self):
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= HEIGHT:
            if not self.hidden:
                self.rect.bottom = HEIGHT
        # if self.rect.top <= 0:
        #     self.rect.top = 0
    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.lastShot > self.shootDelay and not self.hidden:
            shoot_snd.play()
            self.lastShot = now
            if self.powerLevel == 1:
                self.shootDelay = 200
            if self.powerLevel == 2:
                self.shootDelay = 150
            if self.powerLevel == 3 or self.powerLevel == 4:
                self.shootDelay = 100
            if self.powerLevel == 5:
                self.shootDelay = 50

            if self.ships_num == 1 or ships_num == 3:
                b = Bullet(self.rect.centerx, self.rect.top + 1)
                all_sprites.add(b)
                bullet_group.add(b)
            if self.ships_num == 2:
                b = Bullet(self.rect.centerx+20, self.rect.top + 1)
                all_sprites.add(b)
                bullet_group.add(b)

                b = Bullet(self.rect.centerx - 20, self.rect.top+12)
                all_sprites.add(b)
                bullet_group.add(b)
            if self.ships_num == 3:
                b = Bullet(self.rect.centerx + 40, self.rect.top+12)
                all_sprites.add(b)
                bullet_group.add(b)
                b = Bullet(self.rect.centerx - 40, self.rect.top + 12)
                all_sprites.add(b)
                bullet_group.add(b)
    def shieldUp(self, num):
        player.sheild += num
        if player.sheild >= 100:
            player.sheild = 100

    def gun_power_up(self):
        self.powerLevel += 1
        self.powTimer = pg.time.get_ticks()

    def newShip(self):
        oldcenter = self.rect.center
        self.ships_num += 1
        if self.ships_num > 3:
            self.ships_num = 3
        if self.ships_num == 2:
            self.image = playerImg2
            self.image = pg.transform.scale(self.image, (120, 93))
        if self.ships_num == 3:
            self.image = playerImg3
            self.image = pg.transform.scale(self.image, (160, 93))
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter
        self.radius = int(self.rect.width * .85 / 2)
    def oldShip(self):
        oldcenter = self.rect.center
        self.ships_num = 1
        self.image = playerImg
        self.image = pg.transform.scale(self.image, (80, 80))
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter
        self.radius = int(self.rect.width * .85 / 2)
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
        self.sizeChange = r.randint(60, 130)
        self.imageOrig = npcImg
        self.imageOrig = pg.transform.scale(self.imageOrig,
                                            (self.sizeChange, self.sizeChange))
        self.image = self.imageOrig.copy()
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.75 /2)
        # pg.draw.circle(self.image, c.RED, self.rect.center, self.radius)
        self.rect.centerx = ((WIDTH / 2)+r.randint(-100, 100))
        self.rect.top = (0)
        self.speedy = r.randint(1, 10)
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

    # def sizeChanging(self):
    #     self.sizeChange = r.randint(50, 150)
    #     return self.sizeChange

    def spawn(self):
        npc = NPC()
        npc_group.add(npc)
        all_sprites.add(npc)

    def screenWrap(self):
        if self.rect.right > WIDTH+10:
            # self.rect.left = -10
            # self.speedy = r.randint(1, 3)
            # self.speedx = r.randint(-3, 3)
            self.rect.top = 0
            self.rect.centerx = r.randint(2, 558)
            self.speedy = r.randint(1, 10)
            self.speedx = r.randint(-3, 3)
        if self.rect.left < -10:
            # self.rect.right = WIDTH+10
            # self.speedy = r.randint(1, 3)
            # self.speedx = r.randint(-3, 3)
            self.rect.top = 0
            self.rect.centerx = r.randint(2, 558)
            self.speedy = r.randint(1, 10)
            self.speedx = r.randint(-3, 3)
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.centerx = r.randint(2, 558)
            self.speedy = r.randint(1, 10)
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
        # self.explSize = NPC.sizeChanging(NPC)
        self.image = explosion_anim[self.size][0]
        # self.image = pg.transform.scale(self.image, (self.explSize, self.explSize))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.lastUpdate = pg.time.get_ticks()
        self.frameRate = 50

    def update(self):
        now = pg.time.get_ticks()
        if now - self.lastUpdate > self.frameRate:
            self.lastUpdate = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                # if self.size == "lg":
                    # self.image = pg.transform.scale(self.image, (self.explSize, self.explSize))
                self.rect = self.image.get_rect()
                self.rect.center = center


class Pow(pg.sprite.Sprite):
    def __init__(self, center):
        super(Pow, self).__init__()
        self.type = r.choice(powerUps_chance)
        self.image = pows_images[self.type]
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()



####################################################################
# game functions:
####################################################################


def drawText(surf, text, size, x, y, color=c.GREY):
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


def gameOver_screen():

    screen.blit(background, bgRect)
    drawText(screen, "sHmUp,", 64, WIDTH/2, HEIGHT/4)
    drawText(screen, "Arrow keys to move, Space to fire", 22,
             WIDTH/2, HEIGHT/2)
    drawText(screen, "Press any key to begin", 18, WIDTH/2, HEIGHT*3/4)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                # print("test")
            if event.type == pg.KEYUP:
                waiting = False


####################################################################




# load imgs
####################################################################
background = pg.image.load(path.join(bg_folder, "bg.png")).convert()
bgRect = background.get_rect()
playerImg = pg.image.load(path.join(player_imgs_folder, "player.png")).convert()
playerImg2 = pg.image.load(path.join(player_imgs_folder, "player2.png")).convert()
playerImg3 = pg.image.load(path.join(player_imgs_folder, "player3.png")).convert()
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
explosion_anim["xl"] = []


for i in range(9):
    fn = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(animationsFolder, fn)).convert()
    img.set_colorkey(c.BLACK)
    img_xl = pg.transform.scale(img, (150, 150))
    img_lg = pg.transform.scale(img, (100, 100))
    img_sm = pg.transform.scale(img, (40, 40))
    explosion_anim["sm"].append(img_sm)
    explosion_anim["lg"].append(img_lg)
    explosion_anim["xl"].append((img_xl))

bulletImg = pg.image.load(path.join(player_imgs_folder, "bullet.png")).convert()

pows_images = {}

for i in range(len(powerUps_list)):
    fn = "img{}.png".format(i)
    pows_images[powerUps_list[i]] = pg.image.load(path.join(powerFolder, fn)).convert()

####################################################################
# load sounds
####################################################################

shoot_snd = pg.mixer.Sound(path.join(sounds_folder, "shoot.wav"))
expl_sound = pg.mixer.Sound(path.join(sounds_folder, "explosion1.wav"))
music = pg.mixer.Sound(path.join(sounds_folder, "music.ogg"))

####################################################################




fails = 0
# Game Loop
###################
# game update Variables
########################################
playing = True
gameOver = True

########################################
################################################################
while playing:
    if gameOver:
        music.play()
        gameOver_screen()
        gameOver = False
        score = 0
        combo = 0
        # create Sprite groups
        ####################################################################
        all_sprites = pg.sprite.Group()
        players_group = pg.sprite.Group()
        npc_group = pg.sprite.Group()
        bullet_group = pg.sprite.Group()
        pows_group = pg.sprite.Group()
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
            gameOver = True

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
        if not player.invulnerable:
            player.sheild -= hit.radius*2
            if player.sheild <= 0:
                player.hide()
                combo = 0
                player.oldShip()
                if player.lives <= 0:
                    music.fadeout(10)
                    gameOver = True


        else:
            # print("invulnerable")
            pass




    # if bullet hits npc
    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True)
    for hit in hits:
        # score += 50 - hit.radius
        score += 10
        combo += 1
        # make a new ship if high enough points (starting at 5000)
        if combo == 1000:
            player.newShip()
            ships_num = 2
            # print(player.ships_num)
        elif combo == 10000:
            player.newShip()
            ships_num = 3
            # print(player.ships_num)
        if hit.radius >= 50:
            expl = Explosion(hit.rect.center, "xl")
        else:
            expl = Explosion(hit.rect.center, "lg")
        expl_sound.play()
        all_sprites.add(expl)
        npc.spawn()
        if r.random() > .97:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            pows_group.add(pow)
    hits = pg.sprite.spritecollide(player, pows_group, True)
    for hit in hits:
        if hit.type == "shield":
            num = r.randint(20, 100)
            player.shieldUp(num)
        elif hit.type == "lightning":
            player.gun_power_up()



    ##################################################
    # Render
    ##################################################
    screen.fill(c.BLACK)
    screen.blit(background, bgRect)
    all_sprites.draw(screen)
    # draw hud
    drawText(screen, "Score: "+str(score), 18, WIDTH/2, 10, c.DARK_RED)
    drawText(screen, "Combo: "+str(combo), 12, WIDTH/2, 30, c.KINDA_DARK_PURPLE)
    draw_bar(screen, 5, 10, player.sheild)
    drawLives(screen, WIDTH-100, 10, player.lives, playerMiniImage)
    pg.display.flip()

    ##################################################

pg.quit()
################################################################
#####################

