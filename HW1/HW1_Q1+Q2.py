from PIL import Image
import numpy as np

path = 'C:/Users/TYDer/OneDrive/桌面/研究所/碩二下/影像處理/HW1/'
#Q1.
#Read the two images
image1 = Image.open(path + 'laptop_left.png')
image2 = Image.open(path + 'laptop_right.png')

image1_size = image1.size
image2_size = image2.size
image1_size;image2_size
#Define merged image and its size
new_image = Image.new('RGB',(image1_size[0]+image2_size[0], image1_size[1]))
#Paste two images to merged image
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save(path+'laptop.png',"PNG")
new_image.show()

#Q2
# 轉換成numpy array
im_array = np.array(new_image)

# 計算旋轉後的形狀
h, w = im_array.shape[:2]
angle = 15 #旋轉15度

new_h = int(w * np.abs(np.sin(np.radians(angle))) + h * np.abs(np.cos(np.radians(angle))))
new_w = int(h * np.abs(np.sin(np.radians(angle))) + w * np.abs(np.cos(np.radians(angle))))

# 建立一個新的numpy array，用於儲存旋轉後的影像 
rotated_array = np.zeros((new_h, new_w, 3), dtype=np.uint8)

# 計算旋轉前中心
center_x = w / 2
center_y = h / 2

# 計算旋轉後的中心點
rotated_center_x = new_w / 2
rotated_center_y = new_h / 2

# 進行旋轉
for i in range(new_h):
    for j in range(new_w):
        x = (j - rotated_center_x) * np.cos(np.radians(angle)) + (i - rotated_center_y) * np.sin(np.radians(angle)) +center_x
        y = -(j - rotated_center_x) * np.sin(np.radians(angle)) + (i - rotated_center_y) * np.cos(np.radians(angle)) +center_y

        x = int(x)
        y = int(y)
        if x >= 0 and y >= 0 and x < w and y < h:
            rotated_array[i, j] = im_array[y, x]

# 將numpy array轉換為PIL影像
rotated_im = Image.fromarray(rotated_array)
# 儲存影像
rotated_im.save(path + 'rotated_image.png')

rotated_im.show()   