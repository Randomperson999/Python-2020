# imports
import os

# folders

gameFolder = os.path.dirname(__file__)
imageFolder = os.path.join(gameFolder, "image")
sndFolder = os.path.join(gameFolder, "sound")

#colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SILVER = (170, 170, 170)
DARK_GREY = (50, 50, 50)
DEEP_GREY = (20, 20, 20)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

DARKISH_BLUE = (0, 0, 125)
DARK_BLUE = (0, 0, 80)
DEEP_BLUE = (0, 0, 30)
DARKISH_RED = (125, 0, 0)
DARK_RED = (80, 0, 0)
DEEP_RED = (30, 0, 0)
DARKEST_RED = (20, 0, 0)
PURPLE = (80, 0, 80)
DARK_PURPLE = (50, 0, 50)

GOLD = (180, 130, 0)
CORNFLOWER_BLUE = (100, 149, 237)
NEON_GREEN = (57, 255, 20)
BLUE_GREEN = (0, 100, 100)
# Game Values

HEIGHT = 768
WIDTH = 1024
FPS = 30
title = "Tile Based"
BG_COLOR = GOLD

TILE_SIZE = 32
GRID_WITH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE
# Player
PLYR_SPEED = 300

#
