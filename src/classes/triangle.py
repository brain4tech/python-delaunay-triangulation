
# class for storing a triangle

from math import sqrt, atan2

from classes.point import Point

class Triangle:
    def __init__(self, points: list[Point]= None, id = None):
        self.__pa = None
        self.__pb = None
        self.__pc = None
        self.__ccenter = None
        self.__cradius = None

        self.__id = id

        if points:
            self.setCornerPoints(points)
    
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

        x = (self.__pa.x**2 + self.__pa.y**2)*(self.__pb.y - self.__pc.y) + (self.__pb.x**2 + self.__pb.y**2)*(self.__pc.y - self.__pa.y) + (self.__pc.x**2 + self.__pc.y**2)*(self.__pa.y - self.__pb.y)
        y = (self.__pa.x**2 + self.__pa.y**2)*(self.__pc.x - self.__pb.x) + (self.__pb.x**2 + self.__pb.y**2)*(self.__pa.x - self.__pc.x) + (self.__pc.x**2 + self.__pc.y**2)*(self.__pb.x - self.__pa.x)
        
        d = 2*(self.__pa.x * (self.__pb.y - self.__pc.y) + self.__pb.x * (self.__pc.y - self.__pa.y) + self.__pc.x * (self.__pa.y - self.__pb.y))
        
        self.__ccenter = (x/d, y/d)

    def __calculateCRadius(self):
        """Calculates radius of triangle circumcircle"""
        self.__cradius = self.__calculateDistance(self.__ccenter, self.__pa.me())

    def __calculateDistance(self, pfrom, pto):
        """Returns distance from two given points"""
        difference_x = pto[0] - pfrom[0]
        difference_y = pto[1] - pfrom[1]

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

        # calculate triangle center
        center = ((points[0].x + points[1].x + points[2].x)/3, (points[0].y + points[1].y + points[2].y)/3)

        angle_list = []
        for i in range(len(points)):
            angle_list.append(atan2(points[i].y - center[1], points[i].x - center[0]))
        
        # zip angles and plist for combined sorting
        combined_list = list(zip(angle_list, points[:]))
        combined_list.sort(reverse=True)

        self.__pa = combined_list[0][1]
        self.__pb = combined_list[1][1]
        self.__pc = combined_list[2][1]

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
    
    def getPoints(self):
        """Returns corner points"""
        return (self.__pa, self.__pb, self.__pc)
    
    def getCircumcircleCenter(self):
        """Returns center position of circumcircle"""
        return self.__ccenter

    def getCircumcircleRadius(self):
        """Returns radius of circumcircle"""
        return self.__cradius
    
    def Id(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def isPointInCircumcircle(self, point):
        """Check if given point is within circumcircle of triangle"""
        if self.__calculateDistance(point, self.__ccenter) < self.__cradius:
            return True

        return False

    def me(self):
        """Returns itself in a readable data type (dict)"""
        return self.__toReadable()
    
    def includesTag(self, tag):
        if self.__pa.Tag() == tag or self.__pb.Tag() == tag or self.__pc.Tag() == tag:
            return True
        
        return False
    
    def __toReadable(self):
        """Converts own member variables into a readable data type (dict)"""
        return {'a': self.__pa, 'b': self.__pb, 'c': self.__pc, 'center': self.__ccenter, 'radius': self.__cradius}

    def __repr__(self):
        return str(self.__toReadable())
    
    def __str__(self):
        return str(self.__toReadable())