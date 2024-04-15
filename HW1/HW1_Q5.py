import numpy as np
import cv2
from scipy.fftpack import dct, idct
from skimage.measure import compare_psnr
from PIL import Image

#Q5(a)
path = 'C:/Users/TYDer/OneDrive/桌面/研究所/碩二下/影像處理/HW1/'

#Embed
# Load the images
graveler = Image.open(path + 'graveler.bmp')
lena = Image.open(path+'flipped_lena.bmp')
# Convert the images to float data type
graveler = np.float32(graveler)
lena = np.float32(lena)


# Embedding the watermark using DCT
alpha = 0.05
dct_lena = np.zeros_like(lena)

for i in range(3):
    watermark = alpha * dct(graveler[:, :, i], norm='ortho')
    dct_lena[:,:,i] = dct(lena[:, :, i], norm='ortho')
    dct_lena[100:(100+watermark.shape[0]), 460:(460+watermark.shape[1]),i] += watermark


# Inverse DCT to get the watermarked image
watermarked_lena = np.zeros_like(lena)
for i in range(3):
    watermarked_lena[:,:,i] = idct(dct_lena[:,:,i], norm='ortho')

watermarked_lena = np.clip(watermarked_lena, 0, 255)
watermarked_lena = np.uint8(watermarked_lena)

Image.fromarray(np.uint8(watermarked_lena)).show()


#Retrieve
lena = Image.open(path+'flipped_lena.bmp')
lena = np.float32(lena)


#extracted_watermark
extracted_watermark = np.zeros_like(graveler)

for i in range(3):
    extracted_watermark[:,:,i] = idct((1/alpha) * (dct(watermarked_lena[:,:,i])-dct(lena[:,:,i]))
                                      [100:(100+watermark.shape[0]), 460:(460+watermark.shape[1])])

extracted_watermark = np.clip(extracted_watermark, 0, 255)
extracted_watermark = np.uint8(extracted_watermark)

Image.fromarray(np.uint8(extracted_watermark)).show()