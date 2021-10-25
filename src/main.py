
import cv2
import numpy as np


WINDOW_ID = "Delaunay-Triangulation Visualizer"
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

BLACK_PLANE = np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH, 3), dtype=np.uint8)

# define window flags
cv2.namedWindow(WINDOW_ID, flags=cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_AUTOSIZE)

while True:

    cv2.imshow(WINDOW_ID, BLACK_PLANE)

    k = cv2.waitKey(1)

    # ESC pressed
    if k%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()
