#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
#from sensor_msgs.msg import Joy


# This ROS Node converts Joystick inputs from the joy node
# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Velocity commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

# def convertToInt(raw):
#     result = -int(raw*200)
#     #if result < 0:
#     #    result -= 50
#     #else:
#     #    result += 50
#     return result

def callback(error):
    leftWheelVel = 100;
    rightWheelVel = 100;

    rospy.loginfo("I'm in here after all and error.data is $d", error.data);

    if (error.data < 0):
      leftWheelVel = 125;
    elif (error.data > 0):
      rightWheelVel = 125;

    pubLeft.publish((leftWheelVel))
    pubRight.publish((rightWheelVel))

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    rospy.init_node('line_following_node')
    global pubLeft
    global pubRight



    pubLeft = rospy.Publisher('leftVel', Int16)
    pubRight = rospy.Publisher('rightVel', Int16)

    # subscribed to joystick inputs on topic "joy"
    #rospy.Subscriber("joy", Joy, callback)
    rospy.Subscriber("error_val", Int64, callback)
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    start()


            
