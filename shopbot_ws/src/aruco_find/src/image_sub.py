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
from detector import detector



class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.id_pub = rospy.Publisher('arcuoId',Int16)
    self.zPos_pub = rospy.Publisher('zPos',Float64)
    self.boxAngle_pub = rospy.Publisher("angleBox",Float64)
    self.boxPos_pub = rospy.Publisher("posBox",Float64)
    
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)


    image_aruco,pos,angle,zPos,idAruco = detector(cv_image)

    #cv2.imshow("Image window", image_aruco)
    #cv2.waitKey(3)

    try:
      #self.image_pub.publish(self.bridge.cv2_to_imgmsg(image_aruco, "bgr8"))
      self.boxAngle_pub.publish(angle)
      self.boxPos_pub.publish(pos)
      self.zPos_pub.publish(zPos)
      self.id_pub.publish(idAruco) 
      
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
