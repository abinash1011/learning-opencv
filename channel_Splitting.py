import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("greenland_01a.jpg")
b, g, r = cv2.split(img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b_1 = cv2.merge([b,blank,blank])
g_1 = cv2.merge([blank,g,blank])
r_1 = cv2.merge([blank,blank,r])

bgr = cv2.merge([b,g,r])

cv2.imshow('img', img)
cv2.imshow('Blue Channel', b_1)
cv2.imshow('Green Channel', g_1)
cv2.imshow('Red Channel', r_1)
cv2.imshow('bgr', bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
