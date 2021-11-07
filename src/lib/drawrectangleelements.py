
import pygame as pg
from lib.misc import addAlpha


def drawTriangleLines(plane, triangle, line_color, line_thickness):
    pg.draw.line(plane, addAlpha(line_color), triangle.getPointA().me(), triangle.getPointB().me(), line_thickness)
    pg.draw.line(plane, addAlpha(line_color), triangle.getPointB().me(), triangle.getPointC().me(), line_thickness)
    pg.draw.line(plane, addAlpha(line_color), triangle.getPointC().me(), triangle.getPointA().me(), line_thickness)

def drawTrianglePoints(plane, triangle, point_radius):
    pg.draw.circle(plane, addAlpha(triangle.getPointA().color), triangle.getPointA().me(), point_radius)
    pg.draw.circle(plane, addAlpha(triangle.getPointB().color), triangle.getPointB().me(), point_radius)
    pg.draw.circle(plane, addAlpha(triangle.getPointC().color), triangle.getPointC().me(), point_radius)