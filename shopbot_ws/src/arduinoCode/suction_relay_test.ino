/* This code will test the relays to prove that they can control the 
 *  vaacum pump and the valve. The relays will alternate between on
 *  and off
 */
int vacuum_relay = 12;
int valve_relay = 13;
void setup() {
  Serial.begin(9600);
  pinMode(vacuum_relay, OUTPUT);
  pinMode(valve_relay, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(vacuum_relay, HIGH); //vacuum on
  Serial.println("vaacum on");
  delay(5000);
  digitalWrite(valve_relay, HIGH); //valve on
  Serial.println("valve on");
  delay(1000);
  digitalWrite(valve_relay, LOW); //trigger valve
  Serial.println("valve off");
  //delay(1000);
  digitalWrite(vacuum_relay, LOW); //vacuum off
  Serial.println("vaacum off");
  delay(2000); //keep vacuum off for 2 seconds
}
