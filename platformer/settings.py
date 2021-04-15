# imports
import os

# folders

gameFolder = os.path.dirname(__file__)
imageFolder = os.path.join(gameFolder, "image")
sndFolder = os.path.join(gameFolder, "sound")
# Game Values

HEIGHT = 600
WIDTH = 480
FPS = 60
title = "Platformer"

#Player Properties
PLAYER_ACC = 0.8
PLAYER_FRIC = -0.12
#colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

DARK_RED = (80, 0, 0)
DEEP_RED = (30, 0, 0)
PURPLE = (80, 0, 80)
DARK_PURPLE = (50, 0, 50)