import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("greenland_01a.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()
