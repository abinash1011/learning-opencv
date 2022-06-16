from cv2 import destroyAllWindows
import numpy as np
import cv2

img = cv2.imread('iamge1.jpg')
img2 = cv2.imread('iamge2.jpg')

#add = cv2.add(img, img2)

weighted = cv2.addWeighted(img, 0.6, img2, 0.4, 4 )

cv2.imshow('add', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()