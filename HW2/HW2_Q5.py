import cv2
import numpy as np

path = 'C:/Users/TYDer/img_process_HW2/'

#Q5.
imageQ5 = cv2.imread(path+'einstein-low-contrast.tif', cv2.IMREAD_GRAYSCALE)

# Calculate 2D (weighted) histograms h_x(l,k) & H_x(l,k)
x_1 = np.min(imageQ5) ; x_K = np.max(imageQ5) 
weight_hist,hist = np.zeros((256,256)), np.zeros((256,256))
for l in range(256):
    idx = np.where(imageQ5==l)
    for k in range(256):
        weight = np.abs(l-k+1)/(x_K-x_1+1)
        for p, y in zip(*idx):
            if (p < 3 | (p + 3> imageQ5.shape[0]))|(y < 3 | (y + 3> imageQ5.shape[1])):
                continue
            else:
                hist[l,k] += (imageQ5[p-3:p+3+1,y-3:y+3+1]==k).sum()
                weight_hist[l,k] = weight * hist[l,k]

# Calculate H_x(l,k)
H_x = np.zeros_like(weight_hist)
sum_H_x=0
for l in range(256):
    for k in range(256):
        sum_H_x+= weight_hist[l,k]
H_x = weight_hist/sum_H_x

# Calculate CDF_x(m)
CDF_x = [0]*256
for m in range(256):
    for i in range(m):
        for j in range(m):
            CDF_x[m] +=H_x[i,j]

# Calculate H_u(l,k) and CDF_u(m)
CDF_u = [0]*256
hist_u = np.full((256,256),1/256**2)
for m in range(256):
    for i in range(m+1):
        for j in range(m+1):
            CDF_u[m] += hist_u[i,j]

# Calculate transformation function T(l)
T_l = [0]*256
for l in range(256):
    T_l[l] = np.abs(np.array(CDF_x[l])-CDF_u).argmin()

# Imple 2D-HE by using function T(l)
HE2D_image = np.zeros_like(imageQ5)
for l in range(256):
    idx = np.where(imageQ5==l)
    HE2D_image[idx[0],idx[1]] = T_l[l]

# Display the HE image
cv2.imshow('2DHE_image', HE2D_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(path+'Q5_image.tif', HE2D_image)
