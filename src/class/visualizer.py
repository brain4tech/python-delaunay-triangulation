# custom class for vizualizing stuff. Based on OpenCV2 (cv2).

import cv2
import numpy as np

class Visualizer:

    def __init__(self, id, flags=None, terminate_key = 27):

        self.__id = id
        self.__flags = flags
        self.__terminate_char = tuple(terminate_key)

        # render queue: specify order in which base-elements should be rendered
        self.__render_queue = []
    
    # GENERAL WINDOW BEHAVIOUR
    def setTerminateKey(self, key):
        """Define termination keys (int or tuple of ints). Each int must be =< 256."""

        if isinstance(key, int):
            if key > 256:
                raise ValueError(f"Passed integer not allowed to be greater than 256 .")
            self.__terminate_char = key,

        elif isinstance(key, tuple):
            for element in key:
                if isinstance(element, int):
                    if key > 256:
                        raise ValueError(f"Passed integer in tuple not allowed to be greater than 256 (currently: {element}).")

                    raise ValueError(f"One (or more) element in passed tuple is not an integer: {(f'{value} -> {type(value)}' for value in key)}")
            self.__terminate_char = key
        else: raise ValueError(f"Passed key(s) is not type int or tuple")

    def onMouseCallback(self, func):
        def wrapper(*args, **kwargs):
            pass
        
        pass

    # RENDER QUEUE BEHAVIOUR
    def appendToRenderQueue(self, item):
        """Appends a cv2-element to the render queue"""
        self.__render_queue.append(item)


    # ELEMENT CREATION BEHAVIOUR
    def createPlane(self, width, height, color):
        """Creates a mono-color plane with passed size."""
        pass

    def createText(self, text, posX, posY, font, size, color):
        """Creates a text-element at given position."""
        pass
