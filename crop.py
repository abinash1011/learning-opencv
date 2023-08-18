import cv2
import matplotlib.pyplot as plt

img = cv2.imread("greenland_01a.jpg")
height, width, _ = img.shape

new_width = int(width * 0.67) 
new_height = int(height * 0.67)
start_x = (width - new_width) // 2
start_y = (height - new_height) // 2

cropped_img = img[start_y:start_y + new_height, start_x:start_x + new_width]

cv2.imwrite("cropped.jpg", cropped_img)

