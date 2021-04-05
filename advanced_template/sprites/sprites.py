# ---Sprite(s)---

# You can either use this as either:
# a file for one sprite, or all of your sprites.

# If you use only one file for sprites, move the file to the main folder

### imports ###
import pygame
import os
import settings as s


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.Surface((25, 25))
        self.image.fill(s.DEEP_RED)
        self.rect = self.image.get_rect()
        self.rect.center = (s.WIDTH / 2, s.HEIGHT / 2)
        self.ang =10
        self.speedX = 0
        self.speedY = 0
        self.keypressed = False

    def update(self):
        # flow movement
        self.speedX = 0
        self.speedY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedX = -5
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedX = 5
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.speedY = -5
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.speedY = 5

        self.rect.y += self.speedY
        self.rect.x += self.speedX
        if self.speedX !=0:
            self.bounceBorder()

    def toggle_pressed(self):
        self.keypressed = False

    def wallBorder(self):

        if self.rect.right >= s.WIDTH:
            self.rect.right = s.WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= s.HEIGHT:
            self.rect.bottom = s.HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

    def bounceBorder(self):

        if self.rect.right >= s.WIDTH - 1 or self.rect.left <= 0:
            self.speedX = -self.speedX
        if self.rect.bottom >= s.HEIGHT or self.rect.top <= 0:
            self.speedY = -self.speedY
    def screenWrap(self):
        if self.rect.right > s.WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = s.WIDTH
        if self.rect.bottom > s.HEIGHT:
            self.rect.top = 0
        if self.rect.top < 0:
            self.rect.bottom = s.HEIGHT

