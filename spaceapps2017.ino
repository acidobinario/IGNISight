

const int maxTemp = 28;
const int maxHum = 25;
const int maxVel = 0.005;
const int vel = A3;
int velocidad;
int alerta;

#define ONE_WIRE_BUS 3
#include <DHT.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <Adafruit_Sensor.h>

DHT dht(2, DHT11);
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  
  Serial.begin(9600);
  dht.begin();
  sensors.begin();
  pinMode(vel, INPUT);
}

void loop() {

  float h = dht.readHumidity();
  sensors.requestTemperatures();
  velocidad=analogRead(vel);
  if (h<=maxHum && sensors.getTempCByIndex(0)<=maxTemp && velocidad >= maxVel) {

    alerta="1";
    
    }
    else{alerta="0";}
  Serial.print(sensors.getTempCByIndex(0));
  Serial.print(" ");
  Serial.print(h);
  Serial.print(" "); 
  Serial.print(velocidad);
  Serial.print("");
  Serial.println(alerta);

}
