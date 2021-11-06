# class for storing all points and their triangles

from random import randint

from classes.point import Point

class PointList:
    def __init__(self):
        self.__plist: list[Point] = []

    def addPoint(self, point: Point):
        "Adds a new point to the PointList."
        self.__plist.append(point)
    
    def getPoints(self):
        """Returns all stored Points in a list."""
        return self.__plist
    
    def generatePoints(self, minX, maxX, minY, maxY, count, color = (0, 0, 0), padding = 0):
        for _ in range(count):
            self.addPoint(Point(randint(minX+padding, maxX-padding), randint(minY+padding, maxY-padding), color))
    
    # O(n)
    def getNearestPoint(self, point: Point or tuple) -> Point:
        """Returns the nearest point to a given tuple of Point."""

        nearest_point = (0,0)
        nearest_distance = [1000000, 1000000] # use unreachable high number for first comparison

        if isinstance(point, Point):
            for element in self.__plist:
                distance_x = abs(element.x - point.x)
                distance_y = abs(element.y - point.y)
                if distance_x < nearest_distance[0] and distance_y < nearest_distance[1]:
                    nearest_distance[0] = distance_x
                    nearest_distance[1] = distance_y
                    nearest_point = element


        elif isinstance(point, tuple):
                for element in self.__plist:
                    distance_x = abs(element.x - point[0])
                    distance_y = abs(element.y - point[1])
                    if distance_x < nearest_distance[0] and distance_y < nearest_distance[1]:
                        nearest_distance[0] = distance_x
                        nearest_distance[1] = distance_y
                        nearest_point = element
                
        else:
            raise ValueError("Unsupported parameter passed for 'point'")
        
        return nearest_point
    
    def removePoint(self, point: Point):
        self.__plist.remove(point)

if __name__ == '__main__':
    test_list = PointList()

    # test_list.addPoint(Point(23, 34))
    # test_list.addPoint(Point(2, 3))

    test_list.generatePoints(0, 400, 0, 200, 10)

    print(test_list.getPoints())