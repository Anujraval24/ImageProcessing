# A program to demonstrate thresholding (global)
import cv2               # import opnecv library
import numpy as np
from matplotlib import pyplot as plt

# read input gradient image from directory
Img = cv2.imread('C:\Users\anujr\Downloads\messi.png',0)
ret,th1 = cv2.threshold(Img,127,255,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(Img,127,255,cv2.THRESH_BINARY_INV)
ret,th3 = cv2.threshold(Img,127,255,cv2.THRESH_TRUNC)
ret,th4 = cv2.threshold(Img,127,255,cv2.THRESH_TOZERO)
ret,th5 = cv2.threshold(Img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [Img, th1, th2, th3, th4, th5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
