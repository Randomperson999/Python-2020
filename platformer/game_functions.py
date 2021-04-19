import pygame as pg
from settings import *
from sprites import *


def makePlatform(x, y, w, h):
    plat = (x, y, w, h)
    # print(str(plat))
    PLATFORM_LIST.append(plat)
    return plat

