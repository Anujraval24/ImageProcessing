#import opencv library as cv2
#import numerical python (numpy) as np
import cv2
import numpy as np

# create object 0 for image capture
capture=cv2.VideoCapture(0)

while(1):

    # grab frame from object capture continuously
    _, frame= capture.read()

    # convert from BGR space to HSV space
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # show the grabbed image and hsv image
    cv2.imshow('frame',frame)
    cv2.imshow('HSV',hsv)
     k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
    
