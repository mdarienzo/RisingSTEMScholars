#include "AS726X.h"

AS726X sensor;

void setup() {
  Wire.begin();
  Serial.begin(115200);

  sensor.begin();
}

void loop() {
  sensor.takeMeasurementsWithBulb();
  //Prints all measurements
  if (sensor.getVersion() == SENSORTYPE_AS7262)
  {
    //Visible readings
    Serial.print("np.array([");
    Serial.print(sensor.getCalibratedViolet(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedBlue(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedGreen(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedYellow(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedOrange(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedRed(), 2);
    Serial.print("])");
  }
  else if (sensor.getVersion() == SENSORTYPE_AS7263)
  {
    //Near IR readings
    Serial.print("np.array([");
    Serial.print(sensor.getCalibratedR(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedS(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedT(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedU(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedV(), 2);
    Serial.print(", ");
    Serial.print(sensor.getCalibratedW(), 2);
    Serial.print("])");
   }

  Serial.println();
}
