# class for representing one point

class Point:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_
    
    # unnecessary because variables are public, but use this for cleaner code
    def setX(self, new_x):
        self.x = new_x

    def setY(self, new_y):
        self.y = new_y

    def getPoint(self):
        return self.__call__()

    def __call__(self):
        return (self.x, self.y)

    def __repr__(self):
        return str(self.__call__())
    
    def __str__(self):
        return str(self.__call__())
