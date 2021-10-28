# some functions needed in main script

from math import sqrt

def returnNegativeColor(icolor):
    """Returns contrast color of given color value."""
    if icolor < 0 or icolor > 255:
        icolor = icolor%255

    return tuple([(255-value) for value in icolor])

def substractColors(tuple1, tuple2, max_element = None):
    """Subtracts to tuples and returns the result. Should be default in Python, but isn't."""
    
    if not max_element:
        if len(tuple1) >= len(tuple2):
            max_element = len(tuple1)
        else:
            max_element = len(tuple2)

    returnlist = []

    try:
        for x in range(max_element):
            returnlist.append(sqrt((tuple1[x]-tuple2[x])**2))
    except Exception:
        raise ValueError(f"Could not calculate {tuple1[x]} - {tuple2[x]}.")
    
    return tuple(returnlist)

def addAlpha(input_tuple, value=255):
    """Creates and sets a new alpha channel to passed tuple. New tuple is returned."""
    if value < 0 or value > 255:
        value = value%255
        
    input_list = list(input_tuple)
    input_list.append(value)
    
    return tuple(input_list)
