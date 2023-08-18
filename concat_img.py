from cv2 import destroyAllWindows
import numpy as np
import cv2

img = cv2.imread('iamge1.jpg')
img2 = cv2.imread('iamge2.jpg')

#add = cv2.add(img, img2)
print(img.shape)

# hori = np.concatenate((img, img2), axis=1)
# vert = np.concatenate((img, img2), axis=0)

# concatenated_image = np.hstack((img, img2, hori, vert))

# cv2.imshow('add', concatenated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()