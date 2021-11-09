
# import modules and libaries
import path_setup
path_setup.enable()

from math import sqrt

import pygame as pg
from pygame.locals import *
pg.init()

from classes.polygonpointlist import PolygonPointList
from classes.mouseclickorder import MouseClickOrder
from classes.mothertriangle import MotherTriangle
from classes.pointlist import Point, PointList
from classes.trianglelist import Triangle, TriangleList

from lib.misc import *
from lib.drawrectangleelements import *
import constants.colors as color

# CONSTANTS FOR MAIN LOOP
WINDOW_NAME = "Delaunay-Triangulation Visualizer"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
CLEAR_CANVAS = color.DARK_GRAY
POINT_RADIUS = 5
POINT_COLOR = color.MAGENTA
POINT_COLOR_SELECTED = color.GREEN

MOUSE_INPUT = MouseClickOrder(3, ["Primary", "Mouse Wheel", "Secundary"])

DRAW_MOTHER_TRIANGLE_LINES = True

# PYGAME SETUP
WINDOW = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption(WINDOW_NAME)
CLOCK = pg.time.Clock()
FONT = pg.freetype.Font('assets/fonts/Roboto/Roboto-Medium.ttf', size=12)

# CREATE TRANSPARENT PLANES
points_plane = pg.Surface(WINDOW_SIZE, pg.SRCALPHA)
lines_plane = pg.Surface(WINDOW_SIZE, pg.SRCALPHA)
circumcircle_plane = pg.Surface(WINDOW_SIZE, pg.SRCALPHA)
text_plane = pg.Surface(WINDOW_SIZE, pg.SRCALPHA)

# INIT LISTS
point_list = PointList()
triangle_list = TriangleList()
mother_triangle_point_tag = "mt"
mother_triangle = MotherTriangle(WINDOW_WIDTH, WINDOW_HEIGHT, triangle_tag = mother_triangle_point_tag)
mother_triangle_list = TriangleList()

# VARS FOR LOOP
run = True
selected_point = None
new_point = None
polygon_center = None
draw_circumcribed_circles = False
circumcircle_list = []
temp_color = list(color.GREEN)
show_index = 0
polygon_point_list = PolygonPointList()
sorted_point_list = []

# MAI LOOP
while run:

    # clear planes
    circumcircle_plane.fill(addAlpha(color.BLACK, 0))
    points_plane.fill(addAlpha(color.BLACK, 0))
    lines_plane.fill(addAlpha(color.BLACK, 0))
    text_plane.fill(addAlpha(color.BLACK, 0))

    # handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if (event.type == pg.KEYDOWN):
            match event.key:
                case pg.K_ESCAPE:
                    if selected_point:
                        selected_point.setColor(POINT_COLOR)
                        selected_point = None
                    else:
                        run = False
                    
                case pg.K_DELETE:
                    if selected_point:
                        point_list.remove(selected_point)
                        selected_point = None

                case pg.K_F10:
                    point_list.clear()
                    triangle_list.clear()
                    mother_triangle_list.clear()
                    circumcircle_list.clear()
                
                case pg.K_F8:
                    if draw_circumcribed_circles:
                        draw_circumcribed_circles = False
                    else:
                        draw_circumcribed_circles = True
                
                case pg.K_F6:
                    show_index += 1

                case _:
                    pass
                        
    # handle mouse input display
    mouse_x, mouse_y = pg.mouse.get_pos()
    m_clicked_id = MOUSE_INPUT.handleMouseClickOrder(pg.mouse.get_pressed())
    
    match m_clicked_id:
        case 1: # primary, create point
            
            # reset color of selected point
            if selected_point:
                selected_point.setColor(POINT_COLOR)
                selected_point = None
            
            # create new point
            new_point = Point(mouse_x, mouse_y, POINT_COLOR)

            # (re)calculate triangulation
            if len(mother_triangle_list.me()) == 0: # no triangles yet
                mother_triangle_list.append(Triangle([mother_triangle.getPointA(), mother_triangle.getPointB(), new_point]))
                mother_triangle_list.append(Triangle([mother_triangle.getPointB(), mother_triangle.getPointC(), new_point]))
                mother_triangle_list.append(Triangle([mother_triangle.getPointC(), mother_triangle.getPointA(), new_point]))
                
            
            else:
                circumcircle_list.clear()
                polygon_point_list.clear()
                for triangle in mother_triangle_list.getPointInCircumcircles(new_point.me()):
                    circumcircle_list.append(triangle)
                    mother_triangle_list.remove(triangle)
                    polygon_point_list.append(triangle.getPointA())
                    polygon_point_list.append(triangle.getPointB())
                    polygon_point_list.append(triangle.getPointC())

                sorted_point_list.clear()
                sorted_point_list, polygon_center = polygon_point_list.sortPoints(new_point.me())
                
                for i in range(len(sorted_point_list)):
                    mother_triangle_list.append(Triangle([sorted_point_list[i], sorted_point_list[0 if i == len(sorted_point_list)-1 else i+1], new_point]))

            point_list.append(new_point)
        
        case 3: # secundary, mark point and show details
            nearest_point = point_list.getNearestPoint((mouse_x, mouse_y))
            clickradius = POINT_RADIUS + 10
            if abs(nearest_point.x - mouse_x) <= clickradius and abs(nearest_point.y - mouse_y) <= clickradius:
                if selected_point:
                    selected_point.setColor(POINT_COLOR)

                selected_point = nearest_point
                selected_point.setColor(POINT_COLOR_SELECTED)
        case _:
            pass

    for triangle in triangle_list.me():
        drawTriangleLines(lines_plane, triangle, color.WHITE, 3)
    
    if DRAW_MOTHER_TRIANGLE_LINES:
        drawTriangleLines(lines_plane, mother_triangle, color.RED, 3)
        if (len(mother_triangle_list.me())):
            if temp_color[2] + 2 > 255:
                temp_color[2] = 0
            else:
                temp_color[2] += 2
            
            for triangle in mother_triangle_list.me():
                drawTriangleLines(lines_plane, triangle, color.WHITE, 3, mother_triangle_point_tag)
                if draw_circumcribed_circles:
                    drawTriangleCircumcircleCenter(circumcircle_plane, triangle, color.YELLOW, 2)
                    drawTriangleCircumcircle(circumcircle_plane, triangle, color.AQUA, 3)
            
            for i in range(len(mother_triangle_list.me())):
                if i == show_index:
                    drawTriangleLines(lines_plane, mother_triangle_list.me()[i], temp_color, 3)
                    drawTrianglePoints(points_plane, mother_triangle_list.me()[i], 10)
                
            if show_index > len(mother_triangle_list.me())-1:
                show_index = 0



    if sorted_point_list:
        for point in sorted_point_list:
            pg.draw.circle(points_plane, color.MAGENTA, point.me(), 15)
    
    if new_point:
        pg.draw.circle(points_plane, color.YELLOW, new_point.me(), 15)
    if polygon_center:
        pg.draw.circle(points_plane, color.AQUA, polygon_center, 15)


    """for triangle in circumcircle_list:
        drawTriangleCircumcircleCenter(circumcircle_plane, triangle, color.BLUE, 2)
        drawTriangleCircumcircle(circumcircle_plane, triangle, color.AQUA, 5)"""

    # for point in point_list.me():
    #     pg.draw.circle(points_plane, addAlpha(point.color),(point.x, point.y), POINT_RADIUS)

    # draw text
    # draw mouse button clicks to bottom-left
    mouse_click_text, mouse_click_rect = FONT.render(MOUSE_INPUT.getClickOrderString(), addAlpha(substractColors(CLEAR_CANVAS, color.DARK_GRAY, 3)))
    text_plane.blit(mouse_click_text, (10 , WINDOW_HEIGHT-25))

    # draw mouse position in bottom-right
    mouse_pos_text, mouse_pos_rect = FONT.render(f"[{mouse_x}, {mouse_y}]", addAlpha(color.GRAY))
    text_plane.blit(mouse_pos_text, (WINDOW_WIDTH-10 - mouse_pos_rect.width , WINDOW_HEIGHT-25))
    
    # draw current fps in top-right of text-plane
    fps_text, fps_rect = FONT.render(str(int(CLOCK.get_fps())), addAlpha(color.GRAY))
    text_plane.blit(fps_text, (10 , 10))

    # clear canvas and draw planes
    WINDOW.fill(CLEAR_CANVAS)

    WINDOW.blit(circumcircle_plane, (0, 0))
    WINDOW.blit(lines_plane, (0, 0))
    WINDOW.blit(points_plane, (0, 0))
    WINDOW.blit(text_plane, (0,0))

    pg.display.update()
    CLOCK.tick(60)

print ("Terminating...")
path_setup.disable()
