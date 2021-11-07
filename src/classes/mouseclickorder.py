
# class for handling mouse click order

class MouseClickOrder:
    def __init__(self, input_type_count, input_type_names):
        self.__count = input_type_count
        self.click_names = []

        for i in range(self.__count):
            self.click_names.append(input_type_names[i])
        
        self.__clicked = [False] * 3
        self.__click_order = []
        self.__last_input_id = 0
    
    def handleMouseClickOrder (self, new_input):
        for x in range(self.__count):
            if new_input[x] == True:
                if self.__clicked[x] == False:
                    self.__clicked[x] = True
                    self.__last_input_id = x + 1
                    self.__click_order.append(self.click_names[x])
            else:
                if self.__clicked[x] == True:
                    self.__clicked[x] = False
                    self.__last_input_id = (x + 1) * -1
                    self.__click_order.remove(self.click_names[x])
        
        return self.__last_input_id
    
    def getClickOrderString(self):
        string = ""
        if self.__click_order:
            string = "["
            for x in self.__click_order:
                string = string + str(x)
                if x != self.__click_order[-1]:
                    string = string + ", "
            string = string + "]"
        
        return string
    