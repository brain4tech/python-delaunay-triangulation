
# class for storing a triangle

from math import sqrt

from classes.point import Point

class Triangle:
    def __init__(self):
        self.__pa = None
        self.__pb = None
        self.__pc = None
        self.__ccenter = None
        self.__cradius = None
    
    def reset(self):
        """Resets all stored and calculated values"""
        self.__pa = None
        self.__pb = None
        self.__pc = None
        self.__ccenter = None
        self.__cradius = None
    
    def __calculateCCenter(self):
        """Calculates center point of triangle circumcircle"""
        # https://en.wikipedia.org/wiki/Circumscribed_circle#Circumcenter_coordinates

        d = 2*(self.__pa.x * (self.__pb.x + self.__pc.x) + self.__pb.x * (self.__pc.x + self.__pa.x) + self.__pc.x * (self.__pa.x + self.__pb.x))
        x = (self.__pa.x**2 + self.__pa.y**2)*(self.__pb.y + self.__pc.y) + (self.__pb.x**2 + self.__pb.y**2)*(self.__pc.y - self.__pa.y) + (self.__pc.x**2 + self.__pc.y**2)*(self.__pa.y - self.__pb.y)
        y = (self.__pa.x**2 + self.__pa.y**2)*(self.__pc.x + self.__pb.x) + (self.__pb.x**2 + self.__pb.y**2)*(self.__pa.x - self.__pc.x) + (self.__pc.x**2 + self.__pc.y**2)*(self.__pb.x - self.__pa.x)

        self.__ccenter = (x/d, y/d)

    def __calculateCRadius(self):
        """Calculates radius of triangle circumcircle"""
        self.__cradius = self.__calculateDistance(self.__ccenter, self.__pa.me())

    def __calculateDistance(self, pfrom, pto):
        """Returns distance from two given points"""
        difference_x = abs(pfrom[0] - pto[0])
        difference_y = abs(pfrom[1] - pto[1])

        return sqrt(difference_x**2 + difference_y**2)
    
    def __getSign(self, input):
        """Calculates sign of given number and returns True if > 0"""
        if input > 0:
            return True
        
        return False
    
    @staticmethod
    def calculateSlope(pA, pB):
        """Returns slope between two given points"""
        return (pB[1]-pA[1])/(pB[0]-pA[0])

    def setCornerPoints(self, points: list[Point]):
        """Sets and sorts given corner points of triangle in counterclockwise order"""

        sorted_points = points[:]
        sorted_points.sort()
        
        # sort list in counterclockwise order (how?)
        # A: left-most and top-most
        self.__pa = sorted_points[0]
        sorted_points.pop(0)

        # B, quick and dirty
        p2 = sorted_points[0]
        p3 = sorted_points[1]
        lower_point = None
        higher_point = None

        # check which point is lower
        if p2.y > p3.y:
            lower_point = p2
            higher_point = p3
        else:
            lower_point = p3
            higher_point = p2
        
        # calculate connection vector between points (to calculate sign)
        connection_lower = (lower_point.x - self.__pa.x, lower_point.y - self.__pa.y)
        connection_higher = (higher_point.x - self.__pa.x, higher_point.y - self.__pa.y)

        # get slope from A to higher and lower point
        slope_lower = abs(self.calculateSlope(self.__pa.me(), lower_point.me()))
        slope_higher = abs(self.calculateSlope(self.__pa.me(), higher_point.me()))
    
        # check if sign of lower point is positive ( = goes down)
        if self.__getSign(connection_lower[1]) == True:

            # check if connection vector signs are equal ( = same direction)
            if self.__getSign(connection_higher[1]) == self.__getSign(connection_lower[1]):
                
                # check if slope of higher point < slope of lower point
                if slope_higher < slope_lower:
                    self.__pb = lower_point
                    sorted_points.remove(lower_point)

                else:
                    self.__pb = higher_point
                    sorted_points.remove(higher_point)
            
            else:
                self.__pb = lower_point
                sorted_points.remove(lower_point)

        # check if sign of lower is zero or negative ( = goes down)
        elif self.__getSign(connection_lower[1]) == False:

            # check if connection vector signs are equal (to calculate sign)
            if self.__getSign(connection_higher[1]) == self.__getSign(connection_lower[1]):
                
                # check if slope of higher point > slope of lower point
                if slope_higher > slope_lower:
                    self.__pb = lower_point
                    sorted_points.remove(lower_point)

                else:
                    self.__pb = higher_point
                    sorted_points.remove(higher_point)
            
            else:
                self.__pb = lower_point
                sorted_points.remove(lower_point)

        else:
            self.__pb = lower_point
            sorted_points.remove(lower_point)

        # C: remaining point
        self.__pc = sorted_points[0]

        # calculate center and radius of circumcircle
        self.__calculateCCenter()
        self.__calculateCRadius()
    
    def getPointA(self):
        """Returns point A"""
        return self.__pa
    
    def getPointB(self):
        """Returns point B"""
        return self.__pb
    
    def getPointC(self):
        """Returns point C"""
        return self.__pc

    def isPointInCircumcircle(self, point):
        """Check if given point is within circumcircle of triangle"""
        if self.__calculateDistance(point, self.__ccenter) < self.__cradius:
            return True

        return False

    def me(self):
        """Returns itself in a readable data type (dict)"""
        return self.__toReadable()
    
    def __toReadable(self):
        """Converts own member variables into a readable data type (dict)"""
        return {'a': self.__pa, 'b': self.__pb, 'c': self.__pc, 'center': self.__ccenter, 'radius': self.__cradius}

    def __repr__(self):
        return str(self.__toReadable())
    
    def __str__(self):
        return str(self.__toReadable())