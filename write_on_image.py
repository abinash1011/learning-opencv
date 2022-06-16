from cv2 import destroyAllWindows
import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'LEVI in OpenCV!', (50, 200), font, 2, (200,255,255), 3, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()