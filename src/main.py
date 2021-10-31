
import path_setup
path_setup.enable()

import pygame as pg
from pygame.locals import *
pg.init()

from classes.pointlist import Point, PointList

from lib.misc import *
import constants.colors as color

WINDOW_NAME = "Delaunay-Triangulation Visualizer"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
CLEAR_CANVAS = color.DARK_GRAY
POINTS_COLOR = color.MAGENTA

WINDOW = pg.display.set_mode(WINDOW_SIZE)
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

# create planes with transparency
points_plane = pg.Surface(WINDOW_SIZE, pg.SRCALPHA)
text_plane = pg.Surface(WINDOW_SIZE, pg.SRCALPHA)

point_list = PointList()
point_list.generatePoints(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 30, padding=20)

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
            temp_point = Point(mouseX, mouseY)
            point_list.addPoint(temp_point)
            # pg.draw.circle(points_plane, addAlpha(color.MAGENTA),(temp_point.x, temp_point.y), 4)
        case _:
            pass


    text_plane.fill(addAlpha(color.BLACK, 0))
    points_plane.fill(addAlpha(color.BLACK, 0))

    for point in point_list.getPoints():
        pg.draw.circle(points_plane, addAlpha(color.MAGENTA),(point.x, point.y), 4)

    # draw mouse button clicks to bottom-left
    mouse_click_text, mouse_click_rect = FONT.render(mouseClickListToString(), addAlpha(substractColors(CLEAR_CANVAS, color.DARK_GRAY, 3)))
    text_plane.blit(mouse_click_text, (10 , WINDOW_HEIGHT-25))

    # draw mouse position in bottom-right
    mouse_pos_text, mouse_pos_rect = FONT.render(f"[{mouseX}, {mouseY}]", addAlpha(color.GRAY))
    text_plane.blit(mouse_pos_text, (WINDOW_WIDTH-10 - mouse_pos_rect.width , WINDOW_HEIGHT-25))
    
    # draw current fps in top-right of text-plane
    fps_text, fps_rect = FONT.render(str(int(CLOCK.get_fps())), addAlpha(color.GRAY))
    text_plane.blit(fps_text, (10 , 10))


    # clear canvas and draw planes
    WINDOW.fill(CLEAR_CANVAS)
    WINDOW.blit(points_plane, (0, 0))
    WINDOW.blit(text_plane, (0,0))

    pg.display.update()
    CLOCK.tick(60)

print ("Terminating...")
print (f"Pointlist: {point_list.getPoints()}")
print (f"Nearest Point to 500|500 is: {point_list.getNearestPoint(Point(500, 500))}")
path_setup.disable()
