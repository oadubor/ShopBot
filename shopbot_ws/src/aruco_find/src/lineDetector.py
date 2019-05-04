import cv2 
import cv2.aruco as aruco
import numpy as np
import glob
from rot import rotationMatrixToEulerAngles

 



def lineDetector(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh = cv2.threshold(blur,100,255,cv2.THRESH_BINARY)


        
    return thresh,1
