#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String 
from std_msgs.msg import Float64
from std_msgs.msg import Int16 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from lineDetector import lineDetector



class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_line",Image)

    self.error = rospy.Publisher('lineError',Int16)
   
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/usb_cam1/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)


    image_line,lineError  = lineDetector(cv_image)

    #cv2.imshow("Image window", image_aruco)
    #cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(image_line, "mono8"))
      self.error.publish(lineError) 
      
    except CvBridgeError as e:
      print(e)

def main(args):

  rospy.init_node('image_converter', anonymous=True)
  ic = image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
