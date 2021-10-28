
import path_setup
path_setup.enable()

from math import sqrt

import pygame as pg
from pygame.locals import *
pg.init()

import constants.colors as color

WINDOW_NAME = "Delaunay-Triangulation Visualizer"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
CLEAR_CANVAS = color.DARK_GRAY
POINTS_COLOR = color.MAGENTA

WINDOW = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pg.display.set_caption(WINDOW_NAME)

CLOCK = pg.time.Clock()

FONT = pg.freetype.Font('assets/fonts/Roboto/Roboto-Medium.ttf', size=12)

m_clicked = [False]*3
mouse_click_list = []
mouse_click_names = ["Primary", "Mouse Wheel", "Secundary"]

def handleMouseClicks(current, stored):

    for x in range(len(current)):
        if current[x] == True:
            if stored[x] == False:
                stored[x] = True
                # print (f"Mouse button #{x} clicked.")

                return x + 1, mouse_click_names[x]
        else:
            if stored[x] == True:
                stored[x] = False
                return 0 - (x+1), mouse_click_names[x]
    
    return False, ""

def mouseClickListToString():
    string = ""
    if mouse_click_list:
        string = "["
        for x in mouse_click_list:
            string = string + str(x)
            if x != mouse_click_list[-1]:
                string = string + ", "
        string = string + "]"
    
    return string

def returnNegativeColor(icolor):
    # print (icolor)
    
    color = tuple([(255-value) for value in icolor])

    return color

def substractColors(tuple1, tuple2, max_element = None):
    returnlist = []
    
    if not max_element:
        if len(tuple1) >= len(tuple2):
            max_element = len(tuple1)
        else:
            max_element = len(tuple2)
    

    try:
        for x in range(max_element):
            returnlist.append(sqrt((tuple1[x]-tuple2[x])**2))
    except Exception:
        raise ValueError(f"Could not calculate {tuple1[x]} - {tuple2[x]}.")
    
    return tuple(returnlist)

def addAlphaChannel(input_tuple, value=255):
    if value < 0 or value > 255:
        value = value%255
        
    input_list = list(input_tuple)
    input_list.append(value)
    
    return tuple(input_list)

background_plane = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
background_plane.fill(CLEAR_CANVAS)

text_plane = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pg.SRCALPHA)

points_plane = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
points_plane.set_colorkey(color.BLACK)
points_plane.set_alpha(255)

run = True
while run:

    # handle events
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            run = False

    mouseX, mouseY = pg.mouse.get_pos()

    m_clicked_id, m_clicked_name = handleMouseClicks(pg.mouse.get_pressed(), m_clicked)
    if m_clicked_id > 0:
        mouse_click_list.append(m_clicked_name)
    elif m_clicked_id < 0:
        mouse_click_list.remove(m_clicked_name)
    
    match m_clicked_id:
        case 1: # primary
            print ("Circle spawned")
            pg.draw.circle(points_plane, POINTS_COLOR, (mouseX, mouseY), 4)
        case _:
            pass


    # empty text-plane
    text_plane.fill(addAlphaChannel(color.BLACK, 0))

    # add mouse button clicks to bottom-left of text-plane
    mouse_click_text, mouse_click_rect = FONT.render(mouseClickListToString(), addAlphaChannel(substractColors(CLEAR_CANVAS, color.DARK_GRAY, 3)))
    text_plane.blit(mouse_click_text, (10 , WINDOW_HEIGHT-25))

    # add mouse position in bottom-right of text-plane
    mouse_pos_text, mouse_pos_rect = FONT.render(f"[{mouseX}, {mouseY}]", addAlphaChannel(color.GRAY))
    text_plane.blit(mouse_pos_text, (WINDOW_WIDTH-10 - mouse_pos_rect.width , WINDOW_HEIGHT-25))
    
    # add current fps in top-right of text-plane
    fps_text, fps_rect = FONT.render(str(int(CLOCK.get_fps())), addAlphaChannel(color.GRAY))
    text_plane.blit(fps_text, (10 , 10))

    #draw planes in right order
    WINDOW.blit(background_plane, (0, 0))
    WINDOW.blit(points_plane, (0, 0))
    WINDOW.blit(text_plane, (0, 0))

    pg.display.update()
    CLOCK.tick(60)

print ("Terminating...")
path_setup.disable()
