
#include <Stepper.h>

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution for motor
const int revolutionsToGo = 5; //desired number of revolutions
const int stepsToTravel = stepsPerRevolution * revolutionsToGo; //steps needed to travel desired number of revolutions 

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  // set the speed
  myStepper.setSpeed(115); //above 115rpm, likelihood of skipped steps increases
  // initialize the serial port:
  Serial.begin(9600);
}

void loop() {
  // step one revolution  in one direction:
  Serial.println("clockwise");
  myStepper.step(stepsToTravel);
  delay(500);

  // step one revolution in the other direction:
  Serial.println("counterclockwise");
  myStepper.step(-stepsToTravel);
  delay(500);
}
