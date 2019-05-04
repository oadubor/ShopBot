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

    global lastError

    Kp = 0.05
    Kd = 0.3

    baseSpeed = 50.0   

    highPoint = 900.0 #830.0
    #lowPoint  = 590.0 #560.0 
    #setPoint = lowPoint + (highPoint - lowPoint)/2

    error = float(line_value.data)-highPoint

    if error > 0:
	Kp = .35

    corrSpeed = Kp * error + Kd * (error - lastError)
    lastError = error
	
    rightWheelVel = baseSpeed + corrSpeed
    leftWheelVel = baseSpeed - corrSpeed

#    if (error > 0):
#	rightWheelVel += corrSpeed
#	leftWheelVel -= corrSpeed*(2/3)
    #elif (error < 0): 
	#rightWheelVel += corrSpeed * (2/3)
	#leftWheelVel -= corrSpeed
    '''

    if (rightWheelVel > 200):
	rightWheelVel = 200
    if (leftWheelVel > 200):
	leftWheelVel = 200

    if (rightWheelVel < 0):
	rightWheelVel = 0
    if (leftWheelVel < 0):
	leftWheelVel = 0

    '''
    #corr_val = min(abs(error)/100,1) * (40)    
#    corr_val = (abs(error)/100) * 10.0 

#    rospy.loginfo("The corr_val is currently: %f", corr_val)

#    leftWheelVel = - (baseSpeed + corrSpeed)
#    rightWheelVel = - (baseSpeed - corrSpeed)

#    if (error < 0):
#	rightWheelVel = -50.0 - corr_val  #go right
#    elif (error > 0):
#	leftWheelVel = -50.0 - corr_val  #go left

    pubLeft.publish((-leftWheelVel))
    pubRight.publish((-rightWheelVel))

def shutdownProcess():
    pubLeft.publish(0)
    pubRight.publish(0)

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    rospy.init_node('teleop_node')
    global pubLeft
    global pubRight
    global lastError
    
    pubLeft = rospy.Publisher('leftVel', Int16)
    pubRight = rospy.Publisher('rightVel', Int16)
    lastError = 0.0

    # subscribed to joystick inputs on topic "joy"
#    rospy.Subscriber("joy", Joy, callback)
    rospy.Subscriber("line_value", Int16, callback)
    # starts the node
    rospy.on_shutdown(shutdownProcess)
    rospy.spin()


if __name__ == '__main__':
    start()


