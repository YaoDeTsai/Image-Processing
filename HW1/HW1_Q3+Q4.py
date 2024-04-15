from PIL import Image
import numpy as np
import copy

path = 'C:/Users/TYDer/OneDrive/桌面/研究所/碩二下/影像處理/HW1/'
#Q3.

# Open the input BMP file
# Read in the original image from a BMP file
with open(path+"lena.bmp", "rb") as infile:
    # Read the header and extract relevant information
    header = infile.read(54)
    width = int.from_bytes(header[18:22], byteorder="little")
    height = int.from_bytes(header[22:26], byteorder="little")
    bpp = int.from_bytes(header[28:30], byteorder="little")

    # Read in the pixel data and convert it to a 2D array
    pixel_data = infile.read()
    image= [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            offset = i * width * 3 + j * 3
            blue = int.from_bytes(pixel_data[offset:offset+1], byteorder="little")
            green = int.from_bytes(pixel_data[offset+1:offset+2], byteorder="little")
            red = int.from_bytes(pixel_data[offset+2:offset+3], byteorder="little")
            image[height-1-i][j] = (red, green, blue)

# Create a new 2D array to store the resized image
resized_lena = [[0 for _ in range(1024)] for _ in range(1024)]

# Compute the scale factor for resizing
x_scale = width / 1024
y_scale = height / 1024

image[100][100]
# Loop over each pixel in the new image and compute its value using bilinear interpolation
for i in range(1024):
    for j in range(1024):
        # Compute the corresponding location in the original image
        x = i * x_scale
        y = j * y_scale

        # Compute the four neighboring pixel locations and their corresponding weights
        x1 = int(x)
        x2 = min(x1 + 1, width - 1)
        y1 = int(y)
        y2 = min(y1 + 1, height - 1)

        dx = x - x1
        dy = y - y1
        w1 = (1 - dx) * (1 - dy)
        w2 = dx * (1 - dy)
        w3 = (1 - dx) * dy
        w4 = dx * dy

        # Compute the weighted average of the four neighboring pixels
        p1 = image[y1][x1]
        p2 = image[y1][x2]
        p3 = image[y2][x1]
        p4 = image[y2][x2]
        new_pixel = [sum(x) for x in zip(
            [w1 * x for x in p1], 
            [w2 * x for x in p2], 
            [w3 * x for x in p3], 
            [w4 * x for x in p4]
        )]

        # Assign the new pixel value to the corresponding location in the new image array
        resized_lena[j][i] = new_pixel


# Assuming that new_image is a numpy array containing the resized image data

# Convert the numpy array to a PIL Image object
resized = Image.fromarray(np.uint8(resized_lena))

# Save the image to a file
#resized.save(path+"resized_lena.bmp")

#Q4.
graveler = Image.open(path + 'graveler.bmp')
graveler_size = graveler.size

overlay_lena = copy.deepcopy(resized_lena)
graveler = list(np.array(graveler))

for i in range(graveler_size[1]):
    for j in range(graveler_size[0]):
        if tuple(graveler[i][j])!=(255, 255, 255):
            overlay_lena[i][j] = graveler[i][j]
overlay = Image.fromarray(np.uint8(overlay_lena))
overlay.show()
# Save the image to a file
#overlay.save(path+"overlay_lena.bmp")


#####################################################################
with open(path+"graveler.bmp", "rb") as infile:
    # Read the header and extract relevant information
    header = infile.read(54)
    width = int.from_bytes(header[18:22], byteorder="little")
    height = int.from_bytes(header[22:26], byteorder="little")
    bpp = int.from_bytes(header[28:30], byteorder="little")

    # Read in the pixel data and convert it to a 2D array
    pixel_data = infile.read()
    graveler= [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            offset = i * width * 3 + j * 3
            blue = int.from_bytes(pixel_data[offset:offset+1], byteorder="little")
            green = int.from_bytes(pixel_data[offset+1:offset+2], byteorder="little")
            red = int.from_bytes(pixel_data[offset+2:offset+3], byteorder="little")
            graveler[height-1-i][j] = (red, green, blue)