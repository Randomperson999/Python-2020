# Caleb Keller
# Pygame Starter Template
# 2/23/2021

import pygame
import random
import colors as c

# classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(c.DARK_RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speedX = 5
        self.speedY = 0

    def update(self):
        self.rect.y += self.speedY*2
        self.rect.x += self.speedX*2

        # screen wrapping
        # if self.rect.right > WIDTH:
        #     self.rect.left = 0
        # if self.rect.left < 0:
        #     self.rect.right = WIDTH
        # if self.rect.bottom > HEIGHT:
        #     self.rect.top = 0
        # if self.rect.top < 0:
        #     self.rect.bottom = HEIGHT

        if self.rect.right > WIDTH:
            self.rect.bottom = HEIGHT
            self.rect.x = WIDTH/2
            self.speedX = 0
            self.speedY = -5
        if self.rect.left < 0:
            self.rect.top = 0
            self.rect.x = WIDTH/2
            self.speedX = 0
            self.speedY = 5
        if self.rect.bottom > HEIGHT:
            self.rect.left = 0
            self.rect.y = HEIGHT/2
            self.speedX = 5
            self.speedY = 0
        if self.rect.top < 0:
            self.rect.right = WIDTH
            self.rect.y = HEIGHT/2
            self.speedX = -5
            self.speedY = 0


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
player = Player()

# add objects to sprite groups
allSprites.add(player)


# game loop
running = True
while running:
    # keep track of running at the right speed
    clock.tick(FPS)

    # process input
    for event in pygame.event.get():
        # check for window closing
        if event.type == pygame.QUIT:
            running = False
    # update events
    allSprites.update()
    # render all changes
    screen.fill(c.DARK_PURPLE)
    allSprites.draw(screen)

    pygame.display.flip()


