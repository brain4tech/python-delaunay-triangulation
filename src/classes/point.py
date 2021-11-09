# class for representing one point

class Point:
    def __init__(self, x_, y_, color_ = (0, 0, 0), tag = None):
        self.x = x_
        self.y = y_
        self.color = color_

        self.__tag = tag
    
    # unnecessary because variables are public, but use this for cleaner code
    def setX(self, new_x):
        self.x = new_x

    def setY(self, new_y):
        self.y = new_y
    
    def setColor(self, new_color):
        self.color = new_color

    def me(self):
        return self.__toReadable()
    
    def Tag(self):
        return self.__tag
    
    def __toReadable(self):
        return (self.x, self.y)

    def __repr__(self):
        return str(self.__toReadable())
    
    def __str__(self):
        return str(self.__toReadable())

    def __lt__(self, other):
        if self.x < other.x:
            return True
        if self.x == other.x:
            if self.y < other.y:
                return True
        
        return False
