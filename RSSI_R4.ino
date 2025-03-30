#include <WiFiS3.h>

const char* ssid = "WIFIALEJO";
const char* password = "NANANANA";
const int sampleInterval = 5000;
const int averageInterval = 60000;

void setup() {
  Serial.begin(115200); // Mayor velocidad para transmisión
  while (!Serial);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado!");
}

void loop() {
  static unsigned long lastSampleTime = 0;
  static unsigned long lastAverageTime = 0;
  static long sum = 0;
  static int sampleCount = 0;
  
  if (WiFi.status() != WL_CONNECTED) {
    handleConnectionFailure();
    return;
  }

  unsigned long currentTime = millis();
  
  // Toma muestra
  if (currentTime - lastSampleTime >= sampleInterval) {
    lastSampleTime = currentTime;
    long rssi = WiFi.RSSI();
    sum += rssi;
    sampleCount++;
    
    // Envía dato al PC
    Serial.print("DATA,");
    Serial.print(millis());
    Serial.print(",");
    Serial.println(rssi);
  }

  // Calcula promedio
  if (currentTime - lastAverageTime >= averageInterval) {
    lastAverageTime = currentTime;
    if (sampleCount > 0) {
      long average = sum / sampleCount;
      
      Serial.print("AVG,");
      Serial.print(millis());
      Serial.print(",");
      Serial.println(average);
      
      sum = 0;
      sampleCount = 0;
    }
  }
}
