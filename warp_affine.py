import cv2
import numpy as np

img = cv2.imread("greenland_01a.jpg")

tx, ty = 50, 30

transformation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
rows, cols, _ = img.shape

transformed_image = cv2.warpAffine(img, transformation_matrix, (cols, rows))

angle_degrees = 45
center_x, center_y = cols / 2, rows / 2
rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle_degrees, 1)
rotated_image = cv2.warpAffine(img, rotation_matrix, (cols, rows))

m =  np.float32([[1, 0, -100], [-0.5, 1, ty],[0.001, 0.002,1]])
WPimg = cv2.warpPerspective(img, m, (cols, rows))


concatenated_image = np.hstack((img, transformed_image, rotated_image, WPimg))
cv2.imshow('both', concatenated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
