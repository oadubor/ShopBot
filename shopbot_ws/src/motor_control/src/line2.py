#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
#from sensor_msgs.msg import Joy


# This ROS Node converts Joystick inputs from the joy node
# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Velocity commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

#def convertToInt(raw):
 #   result = -int(raw*200)
    #if result < 0:
    #    result -= 50
    #else:
    #    result += 50
  #  return result


def callback(error):
    leftWheelVel = 50
    rightWheelVel = 50

    if (error.data < 0):
	rightWheelVel = 90 #go right
    elif (error.data > 0):
	leftWheelVel = 90 #go left


#    Vac = data.buttons[0]
#    Valve = data.buttons[1]
#    up = data.buttons[2]
#    down = data.buttons[3]

#    global lastVac
#    global lastValve
#    global lastStepup
#    global lastStepdown

#    if Vac > .5 and lastVac < .5:
#       pubVac.publish(1)
#    lastVac = Vac

#    if Valve > .5 and lastValve < .5:
#       pubValve.publish(1)
#    lastValve = Valve

#    if up > .5 and lastStepup < .5:
#       pubStepup.publish(1)
#    lastStepup = up


#    if down > .5 and lastStepdown < .5
#       pubStepdown.publish(1)
#    lastStepdown = down

    pubLeft.publish((leftWheelVel))
    pubRight.publish((rightWheelVel))

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    rospy.init_node('teleop_node')
    global pubLeft
    global pubRight
#    global pubVac
#    global pubValve
#    global pubStepup
#    global pubStepdown



#    lastVac = 0
#    lastValve = 0
#    lastStepup = 0
#    lastStepdown = 0
    
    pubLeft = rospy.Publisher('leftVel', Int16)
    pubRight = rospy.Publisher('rightVel', Int16)
#    pubVac = rospy.Publisher('vac', Int16)
#    pubValve = rospy.Publisher('valve', Int16)
#    pubStepup = rospy.Publisher('stepup', Int16)
#    pubStepdown = rospy.Publisher('stepdown', Int16)

    # subscribed to joystick inputs on topic "joy"
#    rospy.Subscriber("joy", Joy, callback)
    rospy.Subscriber("error_value", Int16, callback)
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    start()


