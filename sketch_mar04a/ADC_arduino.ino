#include <math.h>
int analogCapteur = A0;

double Thermistor(int RawADC){
    double Temp;
    Temp = RawADC / 15.5;
    return Temp;
}

void setup() {
//pinMode (analogCapteur, INPUT);
Serial.begin(9600);
}

void loop() {
float Analog;
int readVal = analogRead(analogCapteur);
double temp =  Thermistor(readVal);

Analog = analogRead(analogCapteur)*(5.0/1023.0); //valeur convertie en tension
int sensorValue= analogRead(analogCapteur); //valeur reélles du capteur

// Sortie vers l'interface série
    Serial.println(temp);
delay(1000);
}
