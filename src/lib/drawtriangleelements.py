import pygame as pg
from lib.misc import addAlphaChannel

import constants.colors as color


def drawTriangleLines(plane, triangle, line_color, line_thickness, exclude_tag=None, reverse_tag = False):
	"Draws (all) lines of given triangle."
	
	if exclude_tag:
	
		if not reverse_tag:
			if triangle.getPointA().Tag() != exclude_tag and triangle.getPointB().Tag() != exclude_tag:
				pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointA().me(), triangle.getPointB().me(),
					line_thickness)

			if triangle.getPointB().Tag() != exclude_tag and triangle.getPointC().Tag() != exclude_tag:
				pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointB().me(), triangle.getPointC().me(),
							line_thickness)

			if triangle.getPointC().Tag() != exclude_tag and triangle.getPointA().Tag() != exclude_tag:
				pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointC().me(), triangle.getPointA().me(),
							line_thickness)
		else:
			if triangle.getPointA().Tag() == exclude_tag or triangle.getPointB().Tag() == exclude_tag:
				pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointA().me(), triangle.getPointB().me(),
					line_thickness)

			if triangle.getPointB().Tag() == exclude_tag or triangle.getPointC().Tag() == exclude_tag:
				pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointB().me(), triangle.getPointC().me(),
							line_thickness)

			if triangle.getPointC().Tag() == exclude_tag or triangle.getPointA().Tag() == exclude_tag:
				pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointC().me(), triangle.getPointA().me(),
							line_thickness)



	else:
		pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointA().me(), triangle.getPointB().me(),
	             line_thickness)
		pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointB().me(), triangle.getPointC().me(),
			             line_thickness)
		pg.draw.line(plane, addAlphaChannel(line_color), triangle.getPointC().me(), triangle.getPointA().me(),
			             line_thickness)


def drawTrianglePoints(plane, triangle, point_radius, exclude_tag=None):
	"""Draws all points if given triangle to passed plane"""
	if exclude_tag:
		for point in triangle.getPoints():
			if point.Tag() == exclude_tag:
				return

	pg.draw.circle(plane, addAlphaChannel(triangle.getPointA().color), triangle.getPointA().me(), point_radius)
	pg.draw.circle(plane, addAlphaChannel(triangle.getPointC().color), triangle.getPointB().me(), point_radius)
	pg.draw.circle(plane, addAlphaChannel(triangle.getPointD().color), triangle.getPointC().me(), point_radius)


def drawTriangleCircumcircle(plane, triangle, line_color, line_thickness):
	"""Draws circumcircle of given triangle to passed plane"""
	pg.draw.circle(plane, addAlphaChannel(line_color), triangle.getCircumcircleCenter(),
	               triangle.getCircumcircleRadius(), line_thickness)


def drawTriangleCircumcircleCenter(plane, triangle, point_color, point_radius):
	"""Draws centre of circumcircle of given triangle to passed plane"""
	pg.draw.circle(plane, addAlphaChannel(point_color), triangle.getCircumcircleCenter(), point_radius)
