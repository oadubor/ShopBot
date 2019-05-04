import cv2 
import cv2.aruco as aruco
import numpy as np
import glob
from rot import rotationMatrixToEulerAngles

 



def lineDetector(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(13,13),0)
    ret,thresh = cv2.threshold(blur,220,255,cv2.THRESH_BINARY)
    M = cv2.moments(thresh)
    # calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    
    return thresh,cX
