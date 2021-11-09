
import pygame as pg
from lib.misc import addAlpha

import constants.colors as color

def drawTriangleLines(plane, triangle, line_color, line_thickness, exclude_tag = None):
    if exclude_tag:
        for point in triangle.getPoints():
            if point.Tag() == exclude_tag:
                return
    
    pg.draw.line(plane, addAlpha(line_color), triangle.getPointA().me(), triangle.getPointB().me(), line_thickness)
    pg.draw.line(plane, addAlpha(line_color), triangle.getPointB().me(), triangle.getPointC().me(), line_thickness)
    pg.draw.line(plane, addAlpha(line_color), triangle.getPointC().me(), triangle.getPointA().me(), line_thickness)

def drawTrianglePoints(plane, triangle, point_radius, exclude_tag = None):
    if exclude_tag:
        for point in triangle.getPoints():
            if point.Tag() == exclude_tag:
                return
    
    pg.draw.circle(plane, addAlpha(color.RED), triangle.getPointA().me(), point_radius)
    pg.draw.circle(plane, addAlpha(color.GREEN), triangle.getPointB().me(), point_radius)
    pg.draw.circle(plane, addAlpha(color.BLUE), triangle.getPointC().me(), point_radius)

def drawTriangleCircumcircle(plane, triangle, line_color, line_thickness):
    pg.draw.circle(plane, addAlpha(line_color), triangle.getCircumcircleCenter(), triangle.getCircumcircleRadius(), line_thickness)

def drawTriangleCircumcircleCenter(plane, triangle, point_color, point_radius):
    pg.draw.circle(plane, addAlpha(point_color), triangle.getCircumcircleCenter(), point_radius)