import cv2
import numpy as np

img = cv2.imread('VOCdevkit/VOC2007/SegmentationClass/104.png', cv2.IMREAD_GRAYSCALE)
img = np.where(img > 0, 1, 0)
shp = img.shape

img_pad = np.zeros([shp[0] + 4, shp[0] + 4])
img_pad[2:-2, 2:-2] = img
dir_array0 = np.zeros([shp[0], shp[1], 3])
dir_array1 = np.zeros([shp[0], shp[1], 3])
dir_array2 = np.zeros([shp[0], shp[1], 3])

for i in range(shp[0]):
    for j in range(shp[1]):
        if img[i, j] == 0:
            continue
        dir_array0[i, j, 0] = img_pad[i, j]
        dir_array0[i, j, 1] = img_pad[i, j + 2]
        dir_array0[i, j, 2] = img_pad[i, j + 4]
        dir_array1[i, j, 0] = img_pad[i + 2, j]
        dir_array1[i, j, 1] = img_pad[i + 2, j + 2]
        dir_array1[i, j, 2] = img_pad[i + 2, j + 4]
        dir_array2[i, j, 0] = img_pad[i + 4, j]
        dir_array2[i, j, 1] = img_pad[i + 4, j + 2]
        dir_array2[i, j, 2] = img_pad[i + 4, j + 4]

import matplotlib.pyplot as plt
plt.subplot(221)
plt.imshow(img)
plt.subplot((222))
plt.imshow(dir_array2[:,:,0])

plt.subplot((223))
plt.imshow(dir_array2[:,:,1])
plt.subplot((224))
plt.imshow(dir_array2[:,:,2])

plt.show()