
import cv2
import numpy as np


WINDOW_ID = "Delaunay-Triangulation Visualizer"
WINDOW_WIDTH = 1700
WINDOW_HEIGHT = 900

FONT = cv2.FONT_HERSHEY_SIMPLEX

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

BLACK_PLANE_RAW = np.full((WINDOW_HEIGHT, WINDOW_WIDTH, 3), COLOR_BLACK, dtype=np.uint8)

def returnNegativeColor(icolor):
    # print (icolor)
    
    color = tuple([(255-value) for value in icolor])

    return color

def mouseCallback(event, x, y, flags, param):
    global img
    
    match event:
        case cv2.EVENT_MOUSEMOVE:
            img = cv2.putText(BLACK_PLANE_RAW.copy(), f"{x} {y}", (10, WINDOW_HEIGHT - 10), FONT, 0.5, returnNegativeColor(BLACK_PLANE_RAW[0][0].tolist()))


img = BLACK_PLANE_RAW.copy()

# define window flags
cv2.namedWindow(WINDOW_ID, flags=cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback(WINDOW_ID, mouseCallback)

while True:

    cv2.imshow(WINDOW_ID, img)

    k = cv2.waitKey(1)

    # ESC pressed
    if k%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()
