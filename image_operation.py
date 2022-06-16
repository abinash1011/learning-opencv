from cv2 import destroyAllWindows
import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]
print(px)

img[55,55] = [255, 255, 255]
px = img[55,55]
print(px)


img[100:150, 100:150] = [255, 255, 255]

levi_face = img[400:700, 150:450]
img[0:300, 0:300] = levi_face
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()