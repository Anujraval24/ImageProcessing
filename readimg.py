
# A Simple program to read an image using opencv functions
import cv2    # import opencv library as cv i.e. like a namespace
import numpy as np # import numercial python numpy as np

# load color image
Img = cv2.imread('C:\Users\anujr\Downloads\messi.png',0)
print Img.shape
print Img.size
print Img.dtype

px=np.array([0,0,0])    # create an 1-D empty array 
pix=Img[100,100]        # access pixel value  
print pix               # print the pixel value
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)    # create a window to display image 
cv2.imshow('Image',Img)                       # show the image on the window
cv2.waitKey(0)                                # wait for key press by user
cv2.destroyAllWindows()                         # Destroy all windows


