#include <math.h>
int analogCapteur = A0;

double Thermistor(int RawADC){
    double Temp;
     Temp = log(((10240000/RawADC) - 10000));
    Temp = 1 / (0.001129148 + (0.000234125 * Temp) + (0.0000000876741 * Temp * Temp * Temp));
    Temp = Temp - 273.15;           // Convert Kelvin to Celcius
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
