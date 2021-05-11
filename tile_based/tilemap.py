import pygame as pg
from settings import *
class Map:
    def __init__(self, filename):
        self.mapData = []
        with open(filename, 'rt') as f:
            for line in f:
                self.mapData.append(line)
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
        pass