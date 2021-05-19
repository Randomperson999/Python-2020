import pygame as pg
from settings import *
class Map:
    def __init__(self, filename):
        self.mapData = []
        with open(filename, 'rt') as f:
            for line in f:
                self.mapData.append(line.strip())
        self.tilewidth = len(self.mapData[0])
        self.tileheight = len(self.mapData)
        self.width = self.tilewidth * TILE_SIZE
        self.height = self.tileheight * TILE_SIZE
class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width-WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
def collide_hitRect(one, two):
    return one.hitRect.colliderect(two.rect)


