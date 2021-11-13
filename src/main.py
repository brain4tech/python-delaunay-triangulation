# import modules and libaries
import path_setup

path_setup.enable()

from classes.polygonpointlist import PolygonPointList
from classes.mouseclickorder import MouseClickOrder
from classes.mothertriangle import MotherTriangle
from classes.point import Point
from classes.pointlist import PointList
from classes.triangle import Triangle
from classes.trianglelist import TriangleList

from lib.misc import *
from lib.drawrectangleelements import *
from lib.rendertext import *
import constants.colors as color

import pygame as pg

# CONSTANTS FOR MAIN LOOP
WINDOW_NAME = "Delaunay-Triangulation Visualizer"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

CLEAR_CANVAS_COLOR = color.DARK_GRAY
POINT_RADIUS = 5
POINT_COLOR = color.MAGENTA
POINT_HIGHLIGHT_COLOR = color.GREEN
LINE_WIDTH = 1
LINE_COLOR = color.LIGHT_GRAY

MOUSE_INPUT_ORDER = MouseClickOrder(3, ["Primary", "Mouse Wheel", "Secondary"])

# PYGAME SETUP
pg.init()
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
mother_triangle_point_tag = "mother_triangle"
mother_triangle = MotherTriangle(WINDOW_WIDTH, WINDOW_HEIGHT, triangle_tag=mother_triangle_point_tag)

# VARS FOR LOOP
run_loop = True
highlighed_point, new_point, polygon_center = None, None, None
polygon_point_list = PolygonPointList()
sorted_polygon_point_list = []

# FUNCTIONS FOR LOOP
def updateText():
	# draw mouse button clicks to bottom-left
	renderText(text_plane, FONT, MOUSE_INPUT_ORDER.getClickOrderString(), color.GRAY, (10, WINDOW_HEIGHT - 25))
	renderText(text_plane, FONT, f"[{mouse_x}, {mouse_y}]", color.GRAY, (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25), True)
	renderText(text_plane, FONT, str(int(CLOCK.get_fps())), color.GRAY, (10, 10))

def setHighlightedPoint(point):
	global highlighed_point

	resetHighlighedPoint()
	highlighed_point = point
	highlighed_point.setColor(POINT_HIGHLIGHT_COLOR)

def resetHighlighedPoint():
	global highlighed_point

	if highlighed_point:
		highlighed_point.setColor(POINT_COLOR)
	
	highlighed_point = None


# MAIN LOOP
while run_loop:

	# clear planes
	WINDOW.fill(CLEAR_CANVAS_COLOR)
	circumcircle_plane.fill(addAlphaChannel(color.BLACK, 0))
	points_plane.fill(addAlphaChannel(color.BLACK, 0))
	lines_plane.fill(addAlphaChannel(color.BLACK, 0))
	text_plane.fill(addAlphaChannel(color.BLACK, 0))

	# handle window events and keypresses
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run_loop = False
		if event.type == pg.KEYDOWN:
			match event.key:
				case pg.K_ESCAPE:
					if highlighed_point:
						resetHighlighedPoint()
					else:
						run_loop = False

				case pg.K_F10:
					point_list.clear()
					triangle_list.clear()
					resetHighlighedPoint()
					WINDOW.fill(CLEAR_CANVAS_COLOR)

				case _:
					pass

	# handle mouse input
	mouse_x, mouse_y = pg.mouse.get_pos()
	mouse_click_action_id = MOUSE_INPUT_ORDER.handleMouseClickOrder(pg.mouse.get_pressed())

	match mouse_click_action_id:
		case 1:  # primary clicked, create point

			# reset color of selected point
			resetHighlighedPoint()

			# create new point
			new_point = Point(mouse_x, mouse_y, POINT_COLOR)

			# calculate triangulation
			# 1. no other triangle than mother triangle
			if len(triangle_list.me()) == 0:
				triangle_list.append(
					Triangle([mother_triangle.getPointA(), mother_triangle.getPointB(), new_point]))
				triangle_list.append(
					Triangle([mother_triangle.getPointB(), mother_triangle.getPointC(), new_point]))
				triangle_list.append(
					Triangle([mother_triangle.getPointC(), mother_triangle.getPointA(), new_point]))

			# 2. all other triangles
			else:

				polygon_point_list.clear()
				sorted_polygon_point_list.clear()

				# add all points of outer triangles to polygon point list ...
				for triangle in triangle_list.getPointInCircumcircles(new_point.me()):
					triangle_list.remove(triangle)
					polygon_point_list.append(triangle.getPointA())
					polygon_point_list.append(triangle.getPointB())
					polygon_point_list.append(triangle.getPointC())

				# ... sort them ...
				sorted_polygon_point_list, _ = polygon_point_list.sortPoints(new_point.me())

				# ... and create new triangles
				for i in range(len(sorted_polygon_point_list)):
					triangle_list.append(Triangle(
						[sorted_polygon_point_list[i],
						 sorted_polygon_point_list[0 if i == len(sorted_polygon_point_list) - 1 else i + 1],
						 new_point]))

			# 3. add new point to global point list
			point_list.append(new_point)

			# 4. highlight new point
			setHighlightedPoint(new_point)

		case 3:  # secondary clicked; mark point (and show details)
			nearest_point = point_list.getNearestPoint((mouse_x, mouse_y))
			click_detection_radius = POINT_RADIUS + 10

			if abs(nearest_point.x - mouse_x) <= click_detection_radius and abs(
					nearest_point.y - mouse_y) <= click_detection_radius:
				
				setHighlightedPoint(nearest_point)
		case _:
			pass

	# draw all triangles on plane
	for triangle in triangle_list.me():
		drawTriangleLines(lines_plane, triangle, LINE_COLOR, LINE_WIDTH, mother_triangle_point_tag)

	# draw all points on plane
	for point in point_list.me():
		pg.draw.circle(points_plane, point.color, point.me(), POINT_RADIUS)

	# update text on plane
	updateText()

	# draw planes on window
	WINDOW.blit(circumcircle_plane, (0, 0))
	WINDOW.blit(lines_plane, (0, 0))
	WINDOW.blit(points_plane, (0, 0))
	WINDOW.blit(text_plane, (0, 0))

	# display updates
	pg.display.update()
	CLOCK.tick(60)

print("Terminating...")
path_setup.disable()
