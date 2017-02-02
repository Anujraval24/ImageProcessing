# A Simple program to track multi color object. Here in example blue and skin color is taken
import cv2    # import opencv library as cv i.e. like a namespace
import numpy as np # import numercial python numpy as np

# define a video capture object 0 is generally the inbuilt web cam in case of laptop
grab=cv2.VideoCapture(0)

while(1):

    # grab frame from object created
    _,frame=grab.read(0)          # capture frame from video object
    b,g,r=cv2.split(frame)          # split image into its channels
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define range of yellow color in image
    #hig_yel=np.array([255,255,0])
    #low_yel=np.array([128,128,0])
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    maskb = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    resb = cv2.bitwise_and(frame,frame, mask= maskb)
    lower_green = np.array([0,50,0])
    upper_green = np.array([100,255,100])

    # Threshold the HSV image to get only blue colors
    maskg = cv2.inRange(frame, lower_green, upper_green)

    # Bitwise-AND mask and original image
    resg = cv2.bitwise_and(frame,frame, mask= maskg)
    res=cv2.bitwise_or(resg,resb)

    # Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(frame, low_yel, hig_yel)

    cv2.imshow('Mask',maskb)
    cv2.imshow('Result',res)
    #cv2.imshow('Blue',b)
    #cv2.imshow('Green',g)
    #cv2.imshow('Red',r)
    cv2.imshow('frame',frame)     # Show image on frame
    k=cv2.waitKey(5) & 0xFF       # detect for key press
    if k == 27:                 # if key press is esc i.e. 27 break
        break

cv2.destroyAllWindows()         # destroy all windows
    

