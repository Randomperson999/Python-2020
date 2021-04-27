import pygame as pg
from settings import *
from sprites import *


def makePlatform(x, y):
    plat = (x, y)
    print(str(plat))
    PLATFORM_LIST.append(plat)
    return plat

