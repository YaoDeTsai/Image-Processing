import numpy as np
import cv2

path = 'C:/Users/TYDer/img_process_HW2/'

#Q1.1
# Read the image
imageQ1 = cv2.imread(path+'text-broken.tif', cv2.IMREAD_GRAYSCALE)

# Define kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Repeat dilation & erosion for several times
iterations = 3
for i in range(iterations):
    dilated_image = cv2.dilate(imageQ1, kernel, iterations=1)
    image = cv2.erode(dilated_image, kernel, iterations=1)
# Save
cv2.imwrite(path+'Q1.1_image.tif', image)

# Perfom repaired image
cv2.imshow('repaired_image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Save
cv2.imwrite(path+'Q1.1_image.tif', image)

#Q1.2
# Perfom the edge of the image
img_erosion = cv2.erode(image, kernel, iterations=1)
boundary = image-img_erosion

cv2.imshow('Boundaries', boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(path+'Q1.2_image.tif', boundary)