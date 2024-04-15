import numpy as np
import cv2
import random

path = 'C:/Users/TYDer/img_process_HW3/'

#1(a)
# Read the image
baboon = cv2.imread(path+'baboon.bmp', cv2.IMREAD_GRAYSCALE)
peppers = cv2.imread(path+'peppers.bmp', cv2.IMREAD_GRAYSCALE)


def add_noise(img,prop):
    idx = random.sample(range(np.prod(img.shape)), int(np.prod(img.shape)*prop))
    
    img_reshape = np.copy(img)
    img_reshape = img_reshape.reshape(np.prod(img.shape))
    img_reshape[idx[:len(idx)//2]] = 0
    img_reshape[idx[(len(idx)//2):]] = 255
    noise_img = img_reshape.reshape(img.shape[0],img.shape[1])
    return(noise_img)

for i in [1,3,5,7,9]:
    cv2.imwrite(path+'Noise_baboo_'+str(i)+'.bmp', add_noise(baboon,i*0.1))

for i in [1,3,5,7,9]:
    cv2.imwrite(path+'Noise_peppers_'+str(i)+'.bmp', add_noise(peppers,i*0.1))

#cv2.imshow('Noise_baboon 10%',noise_baboon_1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#1(b)

def PSNR(original_image, denoised_image):
    mse = np.mean((original_image - denoised_image) ** 2)
    psnr = 10 * np.log10(255**2 / (mse))
    return psnr 


def apply_mean_filter(image):
    kernel = np.ones((5, 5), np.float32) / 25  # 5x5 mean filter kernel
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

def denoise_image1b(noisy_image):
    # Exclude noise pixels
    denoised_image = np.copy(noisy_image)
    denoised_image = denoised_image.astype(np.float32)

    for i in range(2, denoised_image.shape[0] - 2):
        for j in range(2, denoised_image.shape[1] - 2):
            if noisy_image[i, j] != 0 and noisy_image[i, j] != 255:
                filtered_patch = apply_mean_filter(noisy_image[i-2:i+3, j-2:j+3])
                denoised_image[i, j] = np.mean(filtered_patch)

    # Convert denoised image to uint8
    denoised_image = denoised_image.astype(np.uint8)

    return denoised_image


#PSNR
for i in [0.1,0.3,0.5,0.7,0.9]:
    noise_baboon = add_noise(baboon,i)
    print(f'Before_baboon {i}=',np.round(PSNR(baboon,noise_baboon),2))
    print(f'After_baboon {i}=',np.round(PSNR(baboon,denoise_image1b(noise_baboon)),2))

for i in [0.1,0.3,0.5,0.7,0.9]:
    noise_peppers = add_noise(peppers,i)
    print(f'Before_peppers {i}=',np.round(PSNR(peppers,noise_peppers),2))
    print(f'After_peppers {i}=',np.round(PSNR(peppers,denoise_image1b(noise_peppers)),2))



#1(c)
def denoise_image1c(noisy_image):
    # Exclude noise pixels
    denoised_image = np.copy(noisy_image)
    denoised_image = denoised_image.astype(np.float32)

    for i in range(2, denoised_image.shape[0] - 2):
            for j in range(2, denoised_image.shape[1] - 2):
                if noisy_image[i, j] != 0 and noisy_image[i, j] != 255:
                    patch = noisy_image[i-2:i+3, j-2:j+3]
                    denoised_pixel = cv2.GaussianBlur(patch, (5, 5), 2)
                    denoised_image[i, j] = denoised_pixel[2, 2]
    
    # Convert denoised image to uint8
    denoised_image = denoised_image.astype(np.uint8)

    return denoised_image


#PSNR
for i in [0.1,0.3,0.5,0.7,0.9]:
    noise_baboon = add_noise(baboon,i)
    print(f'Before_baboon {i}=',np.round(PSNR(baboon,noise_baboon),2))
    print(f'After_baboon {i}=',np.round(PSNR(baboon,denoise_image1c(noise_baboon)),2))

for i in [0.1,0.3,0.5,0.7,0.9]:
    noise_peppers = add_noise(peppers,i)
    print(f'Before_peppers {i}=',np.round(PSNR(peppers,noise_peppers),2))
    print(f'After_peppers {i}=',np.round(PSNR(peppers,denoise_image1c(noise_peppers)),2))



#1(d)

def adaptive_trimmed_median_filter(image):
    filtered_image = np.copy(image)
    kernel_size = 3
    kernel_radius = kernel_size // 2

    for i in range(kernel_radius, image.shape[0] - kernel_radius):
        for j in range(kernel_radius, image.shape[1] - kernel_radius):
            if image[i, j] != 0 and image[i, j] != 255:
                while kernel_size <= min(i, j, image.shape[0] - i - 1, image.shape[1] - j - 1):
                    window = image[i-kernel_radius:i+kernel_radius+1, j-kernel_radius:j+kernel_radius+1]
                    sorted_pixels = np.sort(window.flatten())

                    median = sorted_pixels[len(sorted_pixels) // 2]
                    max_val = sorted_pixels[-1]
                    min_val = sorted_pixels[0]

                    if image[i, j] > min_val and image[i, j] < max_val:
                        break

                    kernel_size += 2

                filtered_image[i, j] = median if 'median' in locals() else 0  # Assign median if it exists, otherwise assign 0

    return filtered_image

#PSNR
for i in [0.1,0.3,0.5,0.7,0.9]:
    noise_baboon = add_noise(baboon,i)
    print(f'Before_baboon {i}=',np.round(PSNR(baboon,noise_baboon),2))
    print(f'After_baboon {i}=',np.round(PSNR(baboon,adaptive_trimmed_median_filter(noise_baboon)),2))

for i in [0.1,0.3,0.5,0.7,0.9]:
    noise_peppers = add_noise(peppers,i)
    print(f'Before_peppers {i}=',np.round(PSNR(peppers,noise_peppers),2))
    print(f'After_peppers {i}=',np.round(PSNR(peppers,adaptive_trimmed_median_filter(noise_peppers)),2))


