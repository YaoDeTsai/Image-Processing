import numpy as np
import cv2

path = 'C:/Users/TYDer/img_process_HW2/'

# Read
imageQ3 = cv2.imread(path+'einstein-low-contrast.tif', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
hist = np.zeros(256, dtype=int)

for i in range(imageQ3.shape[0]):
    for j in range(imageQ3.shape[1]):
        idx = imageQ3[i, j]
        hist[idx] += 1

# Calculate the CDF
cdf = [0]*256
for i in range(0,256):
    cdf[i] = sum(hist[0:(i+1)])/(imageQ3.shape[0] * imageQ3.shape[1])

# HE
HE_image = np.zeros_like(imageQ3)
for i in range(imageQ3.shape[0]):
    for j in range(imageQ3.shape[1]):
        idx_eq = imageQ3[i, j]
        HE_image[i, j] = int(cdf[idx_eq] * 255)

# Display HE image
cv2.imshow('Equalized Image', HE_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(path+'Q3_image.tif', HE_image)