
import path_setup
path_setup.enable()

import sys
import pygame as pg
from pygame.locals import *
pg.init()

import constants.colors as color

WINDOW_NAME = "Delaunay-Triangulation Visualizer"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
CLEAR_CANVAS = color.BLACK

WINDOW = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pg.display.set_caption(WINDOW_NAME)

CLOCK = pg.time.Clock()

FONT = pg.freetype.Font('assets/fonts/Roboto/Roboto-Medium.ttf', size=12)

def returnNegativeColor(icolor):
    # print (icolor)
    
    color = tuple([(255-value) for value in icolor])

    return color

while True:

    # handle events
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            print ("Terminating...")
            sys.exit()

    mouseX, mouseY = pg.mouse.get_pos()

    # clear canvas
    WINDOW.fill(CLEAR_CANVAS)

    mouse_pos_text, _ = FONT.render(f"{mouseX} {mouseY}", returnNegativeColor(CLEAR_CANVAS))
    WINDOW.blit(mouse_pos_text, (10, WINDOW_HEIGHT-25))
    
    pg.display.update()
    CLOCK.tick(60)
