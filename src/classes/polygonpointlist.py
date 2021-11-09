
from math import atan2

class PolygonPointList:
    def __init__(self):
        self.__plist = []
        self.__ordered_plist = []
        self.__center = None
    
    def append(self, point):
        
        # prevent duplicates
        for point_set in set(self.__plist):
            if point.me() == point_set.me():
                print ("duplicate found, remove point from PolygonPointList", point.me())
                return
        
        self.__plist.append(point)
    
    def clear(self):
        self.__plist.clear()
    
    def me(self):
        return self.__plist
    
    def __calcCenterPoint(self):

        a_loop = 0
        x_loop = 0
        y_loop = 0

        i_plus_one = 0

        for i in range(len(self.__plist)):
            if i == len(self.__plist) - 1:
                i_plus_one = 0
            else:
                i_plus_one = i + 1
            
            a_loop = a_loop + (self.__plist[i].x*self.__plist[i_plus_one].y - self.__plist[i_plus_one].x*self.__plist[i].y)
            x_loop = x_loop + (self.__plist[i].x + self.__plist[i_plus_one].x)*(self.__plist[i].x*self.__plist[i_plus_one].y - self.__plist[i_plus_one].x*self.__plist[i].y)
            y_loop = y_loop + (self.__plist[i].y + self.__plist[i_plus_one].y)*(self.__plist[i].x*self.__plist[i_plus_one].y - self.__plist[i_plus_one].x*self.__plist[i].y)

        a = 1/2 * a_loop
        x = x_loop / (6*a)
        y = y_loop / (6*a)

        self.__center = (x, y)



    def sortPoints(self, center_point = None, point_list = None):
        
        if point_list:
            self.clear()
            self.__plist = point_list[:]
        
        self.__ordered_plist = []

        if center_point:
            self.__center = center_point
        else:
            self.__calcCenterPoint()

        # calculate angle to center for all points
        # https://math.stackexchange.com/questions/707673/find-angle-in-degrees-from-one-point-to-another-in-2d-space/2587852
        angle_list = []
        for i in range(len(self.__plist)):
            angle_list.append(atan2(self.__plist[i].y - self.__center[1], self.__plist[i].x - self.__center[0]))
        
        # zip angles and plist for combined sorting
        combined_list = list(zip(angle_list, self.__plist[:]))
        combined_list.sort()

        for pack in combined_list:
            self.__ordered_plist.append(pack[1])

        return self.__ordered_plist[:], self.__center
    