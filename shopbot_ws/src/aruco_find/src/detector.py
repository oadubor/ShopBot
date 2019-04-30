import cv2 
import cv2.aruco as aruco
import numpy as np
import glob
from rot import rotationMatrixToEulerAngles

 



def detector(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    dist = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    mtx = np.array([[618.367431640625,0.0,320.1849365234375],[0.0,618.33349609375,243.3548126220703],[0.0,0.0,1.0]])

    
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters = aruco.DetectorParameters_create()

    #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    font = cv2.FONT_HERSHEY_SIMPLEX #font for displaying text (below)
    yAngles = -1.0
    xDist = -1.0 

    if np.all(ids != None):
        rvec, tvec,_ = aruco.estimatePoseSingleMarkers(corners[0], 0.1, mtx, dist) #Estimate pose of each marker and return the values rvet and tvec---different from camera coefficients
        #(rvec-tvec).any() # get rid of that nasty numpy value array error
        
        roationMatrix = cv2.Rodrigues(rvec[0])[0]
        eulerAngles = rotationMatrixToEulerAngles(roationMatrix)

        yAngles = eulerAngles[1]
        xDist = tvec[0][0][0]
        

        aruco.drawAxis(image, mtx, dist, rvec[0], tvec[0], 0.1) #Draw Axis
        aruco.drawDetectedMarkers(image, corners) #Draw A square around the markers


        ###### DRAW ID #####
        cv2.putText(image, "Id: " + str(ids), (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

    return image, xDist, yAngles


