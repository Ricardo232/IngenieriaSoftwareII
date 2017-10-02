import pygame as pg
import os
from settings import *


def mymap():
    clock = pg.time.Clock()
    TILE_WIDTH = 160
    TILE_HEIGHT = 80
    current_dir = os.path.dirname(__file__)
    spritesheet = pg.image.load(os.path.join(current_dir, "img\\Maps\\Act_1\\Town\\0.png")).convert()
    img1 = pg.Surface((160, 80))
    img1.blit(spritesheet, (0,0), (3 * TILE_WIDTH, 5 * TILE_HEIGHT, 160, 80))
    img1.set_colorkey((255, 0, 255))
    img2 = pg.Surface((160, 80))
    img2.blit(spritesheet, (0,0), (4 * TILE_WIDTH, 5 * TILE_HEIGHT, 160, 80))
    img2.set_colorkey((255, 0, 255))
    img3 = pg.Surface((160, 80))
    img3.blit(spritesheet, (0,0), (0 * TILE_WIDTH, 6 * TILE_HEIGHT, 160, 80))
    img3.set_colorkey((255, 0, 255))
    img4 = pg.Surface((160, 80))
    img4.blit(spritesheet, (0,0), (1 * TILE_WIDTH, 6 * TILE_HEIGHT, 160, 80))
    img4.set_colorkey((255, 0, 255))
    images = [img1, img2, img3, img4]
    posx = 0
    posy = 0
    current_map = pg.Surface((960, 680))
    for y in range(0, 680, 80):
        posy = y + TILE_HEIGHT/2
        for x in range(0, 960, 320):
            posx = x + TILE_WIDTH/2
            current_map.blit(img2, (x, y), (0, 0, 160, 80))
            current_map.blit(img3, (x + TILE_WIDTH, y), (0, 0, 160, 80))
            current_map.blit(img1, (posx, posy), (0, 0, 160, 80))
            current_map.blit(img4, (posx + TILE_WIDTH, posy), (0, 0, 160, 80))

    return current_map

    #screen.fill(WHITE)
    #screen.blit(current_map, (-80, -40), (0, 0, 960, 680))
    #pg.display.update()
