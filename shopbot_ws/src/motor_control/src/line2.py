#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
#from sensor_msgs.msg import Joy


# This ROS Node converts Joystick inputs from the joy node
# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Velocity commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed


def callback(line_value):
    
    setPoint = 820
    error = line_value.data - setPoint

    #corr_val = min(abs(error)/100,1) * (40)    
    corr_val = (abs(error)/100) * 40

    rospy.loginfo("The corr_val is currently: %f", corr_val)

    leftWheelVel = -50
    rightWheelVel = -50

    if (error < 0):
	rightWheelVel = -50 - corr_val  #go right
    elif (error > 0):
	leftWheelVel = -50 - corr_val  #go left

    pubLeft.publish((leftWheelVel))
    pubRight.publish((rightWheelVel))

def shutdownProcess():
    pubLeft.publish(0)
    pubRight.publish(0)

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    rospy.init_node('teleop_node')
    global pubLeft
    global pubRight
    
    pubLeft = rospy.Publisher('leftVel', Int16)
    pubRight = rospy.Publisher('rightVel', Int16)


    # subscribed to joystick inputs on topic "joy"
#    rospy.Subscriber("joy", Joy, callback)
    rospy.Subscriber("line_value", Int16, callback)
    # starts the node
    rospy.on_shutdown(shutdownProcess)
    rospy.spin()


if __name__ == '__main__':
    start()


