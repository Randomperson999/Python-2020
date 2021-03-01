# Caleb Keller
# Pygame Starter Template
# 2/23/2021

import pygame
import random
import math
import colors as c

# classes
class Npc(pygame.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(c.DARK_PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # self.rect.bottomright = (0, 0)
        # self.speedX = random.randint(-10, 10)
        # self.speedY = random.randint(-10, 10)
        self.speedX = 5
        self.speedY = 5
        self.ang = 10
    def update(self):
        self.rect.y += self.speedY*2
        self.rect.x += self.speedX*2
        self.circle(10)
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
        self.speedX = 0
        self.speedY = 0
    def update(self):
        self.rect.y += self.speedY
        self.rect.x += self.speedX

# Constants
HEIGHT = 400
WIDTH = 400
FPS = 30
title = "Template"

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

    # process input
    for event in pygame.event.get():
        # grid movement
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         # player.speedX = -2
        #         player.rect.x -= 25
        #     if event.key == pygame.K_RIGHT:
        #         player.rect.x += 25
        #     if event.key == pygame.K_UP:
        #         player.rect.y -= 50
        #     if event.key == pygame.K_DOWN:
        #         player.rect.y += 50
        # flow movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedX = -5
            if event.key == pygame.K_RIGHT:
                player.speedX = 5
            if event.key == pygame.K_UP:
                player.speedY = -5
            if event.key == pygame.K_DOWN:
                player.speedY = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedX = 0
            if event.key == pygame.K_RIGHT:
                player.speedX = 0
            if event.key == pygame.K_UP:
                player.speedY = 0
            if event.key == pygame.K_DOWN:
                player.speedY = 0



        # check for window closing
        if event.type == pygame.QUIT:
            running = False
    # update events
    allSprites.update()
    # render all changes
    screen.fill(c.PURPLE)
    allSprites.draw(screen)

    pygame.display.flip()


