/*code to read vacuum pressure sensor via analog pin to ensure
 * proper seal on targeted item
 * */

float kpaToPsi = 0.145038; 
float offset = 0.9359; //offset for vacuum reading 

void setup() {
  Serial.begin(9600);
}

void loop() {
  float v_out = analogRead(A2); //read analog input at pin A1
  //float vac_pressure = ((v_out/v_supply - 0.92)/0.007652); //in kPa
  Serial.print("Vacuum Pressure: "); 
  Serial.print(-(v_out/10)*kpaToPsi - offset); //convert kPa to psi
  Serial.println(" PSI");
  delay(500);
}
