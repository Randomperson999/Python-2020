# --- imports ---
import os
import random as r
# --- folders ---

gameFolder = os.path.dirname(__file__)
imageFolder = os.path.join(gameFolder, "image")
sndFolder = os.path.join(gameFolder, "sound")

# --- Game Values ---

HEIGHT = 600
WIDTH = 480
FPS = 60
title = "Platformer"
FONT_NAME = "arial"

HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# --- Player Properties ---
PLAYER_ACC = 0.8
PLAYER_FRIC = -0.12
PLAYER_GRAV = 0.5
PLAYER_JUMP = 24

# --- Starting Platforms ---

PLATFORM_LIST = [(0, HEIGHT - 50),
                 (WIDTH/2 - 50, HEIGHT * 3/4),
                 (125, HEIGHT-350),
                 (255, HEIGHT-500)]


# --- colors ---

BLACK = (0, 0, 0)
GREY = (125, 125, 125)
DARKISH_GREY = (80, 80, 80)
DARK_GREY = (50, 0, 50)
DARKER_GREY = (10, 10, 10)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

DARK_GREEN = (0, 40, 0)
DARK_BLUE = (0, 0, 40)
DARK_RED = (80, 0, 0)
DEEP_RED = (30, 0, 0)
PURPLE = (80, 0, 80)
DARK_PURPLE = (40, 0, 40)

BG_COLOR = (0, 0, 80)

# G A M E Properties

BOOST_POWER = 45
POW_SPAWN_PCT = 1

MOB_FREQ = 5000

PLAYER_LYR = 2
PLATFORM_LYR = 1
POWER_LAYER = 1
MOB_LYR = 2
CLOUD_LAYER = 0

