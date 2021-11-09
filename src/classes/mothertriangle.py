
from math import sqrt

from classes.triangle import Triangle
from classes.point import Point

class MotherTriangle(Triangle):
    def __init__(self, rectangle_width, rectangle_height, triangle_tag, resize_factor = 1):
        super().__init__()
        self.__rectangle_width_orig = rectangle_width
        self.__rectangle_height_orig = rectangle_height
        
        self.__resize_factor = resize_factor
        self.__rectangle_width = self.__rectangle_width_orig * self.__resize_factor
        self.__rectangle_height = self.__rectangle_height_orig * self.__resize_factor

        self.__side_length = self.__rectangle_width + 2 * self.__rectangle_height
        self.__triangle_height = sqrt(self.__side_length**2 - (self.__side_length/2)**2)

        super().setCornerPoints(self.__calculateMotherTrianglePoints(tag = triangle_tag))
    
    def __calculateMotherTrianglePoints(self, tag = None):
        temp_point_list = []

        temp_point_list.append(Point(self.__rectangle_width_orig/2 - self.__side_length/2, self.__rectangle_height_orig, tag=tag)) # bottom left
        temp_point_list.append(Point(self.__rectangle_width_orig/2 + self.__side_length/2, self.__rectangle_height_orig, tag=tag)) # bottom right
        temp_point_list.append(Point(self.__rectangle_width_orig/2, self.__rectangle_height_orig - self.__triangle_height, tag=tag)) # top
    
        return temp_point_list