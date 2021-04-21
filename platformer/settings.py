# --- imports ---
import os

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

# --- Player Properties ---
PLAYER_ACC = 0.8
PLAYER_FRIC = -0.12
PLAYER_GRAV = 0.5
PLAYER_JUMP = 15

# --- Starting Platforms ---

# PLATFORM_LIST = [(0, HEIGHT - 20, WIDTH, 20),
#                  (WIDTH/2 - 50, HEIGHT * 3/4, 100, 20),
#                  (125, HEIGHT-350, 100, 20)]
PLATFORM_LIST = []

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

BG_COLOR = BLUE
