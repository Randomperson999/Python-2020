# imports
import os
import pygame as pg
vec = pg.math.Vector2
# folders


gameFolder = os.path.dirname(__file__)
imageFolder = os.path.join(gameFolder, "imgs")
sndFolder = os.path.join(gameFolder, "sound")
PLAYER_IMG = "manBlue_machine.png"
WALL_IMG = "tile_171.png"

SPRITESHEET = "spritesheet_tiles.png"
SPRITESHEET2 = "spritesheet_characters.png"
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

BRONZE = (176, 125, 10)

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

NICE_PURPLE = (69, 42, 69)
# Game Values

HEIGHT = 704
WIDTH = 992
FPS = 60
title = "Tile Based"
BG_COLOR = BRONZE

TILE_SIZE = 64
GRID_WITH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE

# Player
PLYR_HP = 100
PLYR_SPEED = 300
PLYR_ROT_SPEED = 250
PLYR_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(27, 10)

# Gun Settings:
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LV_TIME = 1300
BULLET_RATE = 200
KICKBACK = 100
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# Mob Settings
MOB_HP = 100
MOB_IMG = "zoimbie1_gun.png"
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_DAMAGE = 10
MOB_KNOCKBACK = 10

