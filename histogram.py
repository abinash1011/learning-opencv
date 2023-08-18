import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("greenland_01a.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

b, g, r = cv2.split(img)

plt.figure()
plt.title('Blue Channel Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(cv2.calcHist([b], [0], None, [256], [0, 256]))
plt.xlim([0, 256])

plt.figure()
plt.title('Green Channel Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(cv2.calcHist([g], [0], None, [256], [0, 256]))
plt.xlim([0, 256])

plt.figure()
plt.title('Red Channel Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(cv2.calcHist([r], [0], None, [256], [0, 256]))
plt.xlim([0, 256])
plt.show()
