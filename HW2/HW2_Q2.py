import numpy as np
import cv2

path = 'C:/Users/TYDer/img_process_HW2/'
#Q2

# Read the image
imageQ2 = cv2.imread(path+'einstein-low-contrast.tif', cv2.IMREAD_GRAYSCALE)

# Perform linear stretching
stretched_image = (imageQ2 - np.min(imageQ2)) * (255.0 / (np.max(imageQ2) - np.min(imageQ2)))

# Convert the stretched image to uint8 data type
stretched_image = stretched_image.astype(np.uint8)

# Display the stretched image
cv2.imshow('Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(path+'Q2_image.tif', stretched_image)