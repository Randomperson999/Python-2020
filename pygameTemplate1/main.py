# Caleb Keller
# Pygame Starter Template
# 2/23/2021

import pygame
import random
import math
import os
import colors as c

# setup folder assets
gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder, "imgs")
sndFolder = os.path.join(gameFolder, "snds")

# load in game imgs
# playerImg = pygame.image.load((os.path.join(imgFolder, "Capture.png"))).convert()

# Constants
HEIGHT = 400
WIDTH = 400
FPS = 30
title = "Template"

mouse_bttn_held = False

# classes
class Npc(pygame.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(c.DARK_PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # self.rect.bottomright = (0, 0)
        self.speedX = random.randint(-10, 10)
        self.speedY = random.randint(-10, 10)
        # self.speedX = 10
        # self.speedY = 10
        self.ang = 10
    def update(self):
        self.rect.y += self.speedY*2
        self.rect.x += self.speedX*2
        self.circle(20)
        # other movement
        # if self.rect.right >= WIDTH:
        #     self.speedX = 0
        #     self.speedY = -5
        # if self.rect.right >= WIDTH and self.rect.topright[1] < 0:
        #     self.speedX = -5
        #     self.speedY = 0
        # if self.rect.left < 0 and self.rect.topleft[1] <= 0:
        #     self.speedX = 0
        #     self.speedY = 5
        # if self.rect.left <= 0 and self.rect.bottomleft[1] > HEIGHT:
        #     self.speedX = 5
        #     self.speedY = 0
        # if self.rect.right > WIDTH and self.rect.bottomright[1] >= HEIGHT:
        #     self.speedX = 0
        #     self.speedY = -5

        # movement1
        # if self.rect.centerx >= (WIDTH/2) and self.ang < 360:
        #     self.circle(8)
        #     self.rect.center = (WIDTH/2, HEIGHT/2)
        #     self.speedX = 3
        #     self.speedY = -3
        # if self.rect.bottomleft[0] > WIDTH and self.rect.bottomleft[1] <= 0:
        #     self.rect.bottomright = (0, 0)
        #     self.speedX = 3
        #     self.speedY = 3

        # screen wrapping
        # if self.rect.right > WIDTH:
        #     self.rect.left = 0
        # if self.rect.left < 0:
        #     self.rect.right = WIDTH
        # if self.rect.bottom > HEIGHT:
        #     self.rect.top = 0
        # if self.rect.top < 0:
        #     self.rect.bottom = HEIGHT
        #

        # screen wrapping 3
        if self.rect.right >= WIDTH-1 or self.rect.left <= 0:
            self.speedX = -self.speedX
        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.speedY = -self.speedY

    def circle(self, n):
        rad = self.ang * math.pi / 180
        self.rect.centery = -math.sin(rad) * n + self.rect.centery
        self.rect.centerx = math.cos(rad) * n + self.rect.centerx
        self.ang += 5
        if self.rect.right >= WIDTH-1:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.Surface((25, 50))
        self.image.fill(c.DEEP_RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.ang =10
        self.speedX = 0
        self.speedY = 0
        self.keypressed = False

    def update(self):
        # move with mouse
        mousex, mousey = pygame.mouse.get_pos()

        if mouse_bttn_held:
            self.rect.center = pygame.mouse.get_pos()


        # flow movement
        # self.speedX = 0
        # self.speedY = 0
        # keystate = pygame.key.get_pressed()
        # if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
        #     self.speedX = -5
        # if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
        #     self.speedX = 5
        # if keystate[pygame.K_UP] or keystate[pygame.K_w]:
        #     self.speedY = -5
        # if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
        #     self.speedY = 5

        self.rect.y += self.speedY
        self.rect.x += self.speedX
        if self.speedX !=0:
            self.circle(60)

        # grid
        # keystate = pygame.key.get_pressed()
        # if (keystate[pygame.K_LEFT] or keystate[pygame.K_a]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx -= 25
        # if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
        #     self.keypressed = True
        #     self.rect.centerx += 25
        # if keystate[pygame.K_UP] or keystate[pygame.K_w]:
        #     self.keypressed = True
        #     self.rect.centery -= 25
        # if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
        #     self.keypressed = True
        #     self.rect.centery += 25
        # keyrelease = pygame.KEYUP
        # if keyrelease == pygame.K_LEFT:
        #     self.keypressed = False
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #         self.toggle_pressed()
        #     if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #         self.toggle_pressed()
        #     if event.key == pygame.K_UP or event.key == pygame.K_w:
        #         self.toggle_pressed()
        #     if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        #         self.toggle_pressed()

        self.bounceBorder()
    def circle(self, n):
        rad = self.ang * math.pi / 180
        self.rect.centery = -math.sin(rad) * n + self.rect.centery
        self.rect.centerx = math.cos(rad) * n + self.rect.centerx
        self.ang += 5
        if self.rect.right >= WIDTH-1:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

    def toggle_pressed(self):
        self.keypressed = False
    def wallBorder(self):

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

    def bounceBorder(self):

        if self.rect.right >= WIDTH - 1 or self.rect.left <= 0:
            self.speedX = -self.speedX
        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.speedY = -self.speedY
    def screenWrap(self):
        if self.rect.right > WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT


def spw_new_player(x, y):
    newplayer = Player()
    newplayer.rect.center = (x, y)
    newplayer.speedX = random.randint(-20, 20)
    newplayer.speedY = random.randint(-20, 20)
    allSprites.add(newplayer)
    playersGroup.add(newplayer)
# initialize pygame and create window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(title)
clock = pygame.time.Clock()


# sprite groups
allSprites = pygame.sprite.Group()
playersGroup = pygame.sprite.Group()
mobsGroup = pygame.sprite.Group()
# game objects
npc = Npc()
player = Player()

# add objects to sprite groups
allSprites.add(npc)
mobsGroup.add(npc)
allSprites.add(player)
playersGroup.add(player)



# game loop
running = True
while running:
    # keep track of running at the right speed
    clock.tick(FPS)
    mousex, mousey = pygame.mouse.get_pos()

    # process input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and player.rect.collidepoint(pygame.mouse.get_pos()):
            mouse_bttn_held = True

            # print(str.format("({0}, {1})", mousex, mousey))

        if event.type == pygame.MOUSEBUTTONUP and mouse_bttn_held == True:
            mouse_bttn_held = False
            for i in range(10):
                spw_new_player(mousex, mousey)

        # check for window closing
        if event.type == pygame.QUIT:
            running = False
    # update events
    allSprites.update()
    # render all changes
    screen.fill(c.PURPLE)
    allSprites.draw(screen)

    pygame.display.flip()


