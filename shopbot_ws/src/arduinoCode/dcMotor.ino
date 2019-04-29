/*
 * Carnegie Mellon University
 * Washbot Project
 * Hans Kumar and Henry Zhang
 * Motor controll using rosserial and joystick
 */
#include <ros.h>
#include <std_msgs/Int16.h>
#include <Arduino.h>

const int PWM0 = 9;
const int PWM1 = 10;
const int DIR0 = 7;
const int DIR1 = 8;
const int vacuum_relay = 12;
const int valve_relay = 13;


ros::NodeHandle nh;
int16_t rightVel = 0;
int16_t leftVel = 0;



void moveMotor(int motor, int dutyCycle, int direction){
  setMotorDirection(motor, direction);
  setMotorDutyCycle(motor, dutyCycle);
}

void setMotorDutyCycle(int motor, int dutyCycle){
  if(dutyCycle>=0 && dutyCycle<=255){
    if(motor==0){ analogWrite(PWM0, dutyCycle);}
    else if(motor==1){ analogWrite(PWM1, dutyCycle);}
  }
  else{
    Serial.println("Motor duty cycle out of range");
  }
}

void setMotorDirection(int motor, int direction){
  int outputPin;
  if(motor == 0){
    outputPin = DIR0;
  }
  else{
    outputPin = DIR1;
  }
  digitalWrite(outputPin, direction);
}


void getRightVelCallback(const std_msgs::Int16& vel_msg) {
  if (vel_msg.data > 0){
    moveMotor(1, abs(vel_msg.data), HIGH);
  }else{
    moveMotor(1, abs(vel_msg.data), LOW);
  }
}

void getLeftVelCallback(const std_msgs::Int16& vel_msg) {
  if (vel_msg.data > 0){
    moveMotor(0, abs(vel_msg.data), HIGH);
  }else{
    moveMotor(0, abs(vel_msg.data), LOW);
  }
}

void vacCallback(const std_msgs::Int16& vel_msg) {
    digitalWrite(vacuum_relay, 1-digitalRead(vacuum_relay));
}

void valveCallback(const std_msgs::Int16& vel_msg) {
    digitalWrite(valve_relay, 1-digitalRead(valve_relay));
}


ros::Subscriber<std_msgs::Int16> rightVelSub("rightVel", &getRightVelCallback);
ros::Subscriber<std_msgs::Int16> leftVelSub("leftVel", &getLeftVelCallback);
ros::Subscriber<std_msgs::Int16> vacSub("vac", &vacCallback);
ros::Subscriber<std_msgs::Int16> valveSub("valve", &valveCallback);

void setup() {
  // init node and subcribe
  pinMode(DIR0, OUTPUT);
  pinMode(DIR1, OUTPUT);
  pinMode(vacuum_relay, OUTPUT);
  pinMode(valve_relay, OUTPUT);
  nh.initNode();
  nh.subscribe(rightVelSub);
  nh.subscribe(leftVelSub);
  nh.subscribe(vacSub);
  nh.subscribe(valveSub);
}

void loop() {
  nh.spinOnce();
}
