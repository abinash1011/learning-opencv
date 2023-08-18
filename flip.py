import cv2
import matplotlib.pyplot as plt

img = cv2.imread("greenland_01a.jpg")
flip_img_ver = cv2.flip(img, 0)
flip_img_hor = cv2.flip(img, 1)
flip_img_both = cv2.flip(img, -1)

plt.imshow(flip_img_ver)
plt.show()
plt.imshow(flip_img_hor)
plt.show()
plt.imshow(flip_img_both)
plt.show()