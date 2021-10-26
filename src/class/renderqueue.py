# class for render qeueu

import cv2

class RenderQueue(list):
    pass

class RenderQueueItem:
    def __init__(self, function, params):
        self.__function = function
        self.__params = params