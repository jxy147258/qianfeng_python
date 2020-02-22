# -*- coding: utf-8 -*-
#图像融合
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')

img_mix = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img_mix', img_mix)

cv2.waitKey(0)
cv2.destroyAllWindows()

#==========彩色图片转灰度图片=====
#from PIL import Image
#im = Image.open('lena.png')
##im.show()
#L = im.convert('L')
#L.show()
#L.save('new_lena.png')
