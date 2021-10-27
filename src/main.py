
import path_setup
path_setup.enable()

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


    # clear canvas
    WINDOW.fill(CLEAR_CANVAS)

    # display mouse button clicks
    mouse_click_text, mouse_click_rect = FONT.render(mouseClickListToString(), color.DARK_GRAY)
    WINDOW.blit(mouse_click_text, (10 , WINDOW_HEIGHT-25))

    # display mouse position in bottom-right
    mouse_pos_text, mouse_pos_rect = FONT.render(f"[{mouseX}, {mouseY}]", color.GRAY)
    WINDOW.blit(mouse_pos_text, (WINDOW_WIDTH-10 - mouse_pos_rect.width , WINDOW_HEIGHT-25))
    
    pg.display.update()
    CLOCK.tick(60)

print ("Terminating...")
path_setup.disable()
