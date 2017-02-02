# This code demonstrates image addition (opencv add function and numpy add function)
# and image blending operations
# your code execution
import cv2   #import opencv library to use its functions
import numpy as np #like a namespace is assigned to numpy
e1 = cv2.getTickCount()
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
Img1_r=cv2.resize(Img1,s_inv)
print Img1_r.shape

# comparison of cv2.add function and numpy add function
x=np.uint8([250])
y=np.uint8([50])
sum_cv=cv2.add(x,y)
print 'opencv addition'
print sum_cv
sum_np=x+y
print 'numpy addition'
print sum_np

# comparison of  opencv add function and numpy add on image
cv_imgadd=cv2.add(Img,Img1_r)
nump_imgadd=Img+Img1_r


# image blending i.e image weighted addition
weig_add=cv2.addWeighted(Img,0.9,Img1_r,0.1,0)

cv2.imshow('Image1',Img)   # show image
cv2.imshow('Image2',Img1)   # show image
cv2.imshow('Image2 Resized',Img1_r)   # show image
cv2.imshow('Opencv image addition',cv_imgadd)   # show image
cv2.imshow('Numpy image addition',nump_imgadd)   # show image
cv2.imshow('Image blending',weig_add)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print 'Time take in seconds'
print time
cv2.waitKey(0)    
cv2.destroyAllWindows()   # destroy all windows



