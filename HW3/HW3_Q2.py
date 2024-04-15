import numpy as np
import cv2
import random

path = 'C:/Users/TYDer/img_process_HW3/'

peppers = cv2.imread(path+'peppers.bmp', cv2.IMREAD_GRAYSCALE)
peppers_4 = cv2.imread(path+'peppers_0.04.bmp', cv2.IMREAD_GRAYSCALE)


#Q2(a)
def sobel_filter(image):
    # Define the Sobel kernels
    sobel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])

    # Apply the Sobel filters
    gradient_x = cv2.filter2D(image, cv2.CV_64F, sobel_x)
    gradient_y = cv2.filter2D(image, cv2.CV_64F, sobel_y)

    # Calculate gradient magnitude
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    # Normalize gradient magnitude to 0-255
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return gradient_magnitude


cv2.imwrite(path+'Sobel_peppers.bmp', sobel_filter(peppers))
cv2.imwrite(path+'Sobel_peppers_0.04.bmp', sobel_filter(peppers_4))



#Q2(b)
def function2b(image):
    smoothed_image = cv2.GaussianBlur(image, (5, 5), 1)
    laplacian = cv2.Laplacian(smoothed_image, cv2.CV_64F)
    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    return(laplacian)

cv2.imwrite(path+'Gaussian_Lapcian_peppers.bmp', function2b(peppers))
cv2.imwrite(path+'Gaussian_Lapcian_peppers_0.04.bmp', function2b(peppers_4))



cv2.imshow('Noisy Image', function2b(peppers))
cv2.waitKey(0)
cv2.destroyAllWindows()
