
# class for storing all triangles

from classes.triangle import Triangle

class TriangleList:
    def __init__(self):
        self.__tlist: list[Triangle] = []

    def append(self, triangle: Triangle):
        """Appends a given triangle to the list"""
        self.__tlist.append(triangle)
    
    def remove(self, triangle: Triangle):
        """Removes a given triangle from the list"""
        self.__tlist.remove(triangle)
    
    def clear(self):
        """Clears list"""
        self.__tlist.clear()

    def me(self):
        "Returns itself"
        return self.__tlist[:]
    
    def getPointInCircumcircles(self, point):
        "Returns all triangles where given point is in circumcircle"
        trianglelist = []

        for triangle in self.__tlist:
            if triangle.isPointInCircumcircle(point):
                trianglelist.append(triangle)
        
        return trianglelist
    
