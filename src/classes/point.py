# class for representing one point

class Point:
    def __init__(self, x_, y_, color_):
        self.x = x_
        self.y = y_
        self.color = color_
    
    # unnecessary because variables are public, but use this for cleaner code
    def setX(self, new_x):
        self.x = new_x

    def setY(self, new_y):
        self.y = new_y
    
    def setColor(self, new_color):
        self.color = new_color

    def getPoint(self):
        return self.__repr__()

    def __repr__(self):
        return str((self.x, self.y))
    
    def __str__(self):
        return self.__repr__()
