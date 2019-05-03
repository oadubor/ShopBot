#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float64
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
class posServer:
  def __init__(self):
    self.leftRpm = 0
    self.rightRpm = 0
    self.stepDone = 0

def grabObject(ObjectZ, DropZ):
    #rospy.sleep(2)
    pubVac.publish(1)
    #pubValve.publish(1)
    #rospy.sleep(2)
    #pubVac.publish(1)
    rospy.sleep(2)
    pubStep.publish(ObjectZ)
    rospy.sleep(30)
    pubStep.publish(DropZ)
    rospy.sleep(30)
    pubVac.publish(1)
    pubValve.publish(1)

def pos_callback(error):
    leftWheelVel = 0;
    rightWheelVel = 0;
    setpoint = .11;
    #rospy.loginfo("I'm in here after all and error.data is $d", error.data);
    correction = error.data-setpoint
    vel = int(1*correction*400)
    if error.data < -.5:
	vel = 0
    leftAngle = int(poser.leftRpm*150)
    rightAngle = int(poser.rightRpm*150)

    pubLeft.publish(vel)
    pubRight.publish(vel)
    if poser.stepDone == 0  and abs(correction) < .03 and vel < 20:
        grabObject(11000,-11000)
        poser.stepDone = 1

def ang_callback(error):
    if error. data > -.5:
    	poser.leftRpm = -error.data;
    	poser.rightRpm = error.data;
    #else:
    #	poser.leftRpm = 0;
    #	poser.rightRpm = 0;
    
# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global poser
    rospy.init_node('visualServo_node')
    poser = posServer()

    global pubLeft
    global pubRight
    global pubStep
    global pubVac
    global pubValve


    pubStep = rospy.Publisher('step', Int16)
    pubVac = rospy.Publisher('vac',Int16)
    pubValve = rospy.Publisher('valve',Int16)
    pubLeft = rospy.Publisher('leftVel', Int16)
    pubRight = rospy.Publisher('rightVel', Int16)
    #subscribed to joystick inputs on topic "joy"
    rospy.sleep(4)
    rospy.Subscriber("angleBox", Float64, ang_callback)
    rospy.Subscriber("posBox", Float64, pos_callback)
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    start()


            
