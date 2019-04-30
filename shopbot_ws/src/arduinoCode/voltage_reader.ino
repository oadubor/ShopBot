
int offset = 30; //voltage offset to account for sensor noise, tuned using power supply

void setup() {
  Serial.begin(9600);
}

void loop() {
  int volt = analogRead(A1); //read analog input at pin A1
  double voltage = map(volt, 0, 1023, 0, 2500) + offset; //map 0-1023 to 0-2500 mV & add correction offset 
  voltage /=100;
  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.println("V");
  delay(500);
}
