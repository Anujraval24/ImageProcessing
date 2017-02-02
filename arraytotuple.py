import cv2   #import opencv library to use its functions
import numpy as np #like a namespace is assigned to numpy

# read the image from path
Img=cv2.imread('C:\Users\anujr\Downloads\messi.png',0)
Img1=cv2.imread('C:\Users\anujr\Downloads\messi1.png',0)
s=Img.shape
s1=Img1.shape
#s_inv=(s(2),s(1))
#print s_inv
s_inv=np.flipud(s)
def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

s_inv=totuple(s_inv)
print s_inv
