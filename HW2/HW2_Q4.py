import cv2
import matplotlib.pyplot as plt

path = 'C:/Users/TYDer/img_process_HW2/'

#Q4.
imageQ4 = cv2.imread(path+'aerialview-washedout.tif', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
hist = [0]*256
for i in range(imageQ4.shape[0]):
    for j in range(imageQ4.shape[1]):
        idx = imageQ4[i, j]
        hist[idx] += 1

# Find the median of the image
total_pixels = imageQ4.shape[0] * imageQ4.shape[1]
cum_pixels, median = 0 , 0
for i in range(256):
    cum_pixels += hist[i]
    if cum_pixels >= int(total_pixels / 2):
        median = i
        break

# Calculate cdf of two sub-histogranms
cdf_Q4 = [0]*256
for i in range(0, 256):
    if i<=median:
        cdf_Q4[i] = sum(hist[0:(i+1)])/sum(hist[0:(median+1)])
    else:
        cdf_Q4[i] = sum(hist[(median+1):(i+1)])/sum(hist[(median+1):])

# Perform HE for sub-histograms
subHE_image = [[0 for i in range(imageQ4.shape[1])] for i in range(imageQ4.shape[0])]
for i in range(imageQ4.shape[0]):
    for j in range(imageQ4.shape[1]):
        idx_Q4 = imageQ4[i, j]
        if idx_Q4 <= median:
            subHE_image[i][j] = int(cdf_Q4[idx_Q4] * median)
        else:
            subHE_image[i][j] = int(cdf_Q4[idx_Q4] * (255 - median) + median)


height, width = imageQ4.shape
fig = plt.figure(figsize=(width/100, height/100))
ax = fig.add_subplot(111)
ax.imshow(subHE_image, cmap='gray')
ax.axis('off')
fig.savefig(path+'Q4_image.tif', bbox_inches='tight', pad_inches=0)
plt.show()
