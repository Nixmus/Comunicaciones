#include <WiFiS3.h>

// Configuración WiFi
const char* ssid = "WIFIALEJO";
const char* password = "NANANANA";

// Parámetros de medición
const float x1 = 1.0;     // 1 metro
const float RSSI1 = -39.0;       // RSSI a 1 metro
const float n = 1;        // Factor de atenuación
const unsigned long SAMPLE_TIME = 5000; // 10 segundos de muestreo

// Variables de estado
long rssi = 0;
float distance = 0, exponente;
unsigned long lastMeasurement = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);  // Espera a que se inicialice el puerto serial

  Serial.print("Conectando a ");
  Serial.println(ssid);

  const unsigned long TIMEOUT_MS = 20000; // 20 segundos
  unsigned long startTime = millis();
  WiFi.begin(ssid, password);
  
  // Espera hasta que se conecte o se agote el tiempo
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    
    // Verifica si se ha agotado el tiempo de espera
    if (millis() - startTime > TIMEOUT_MS) {
      Serial.println("\nError: Tiempo de conexión agotado!");
      handleConnectionFailure();
      return; // Sale del setup si no se puede conectar
    }
  }
  
  // Si llegamos aquí, la conexión fue exitosa
  Serial.println("\nWiFi conectado exitosamente!");
  Serial.print("Dirección IP asignada: ");
  Serial.println(WiFi.localIP());
  Serial.print("Potencia inicial de la señal: ");
  Serial.print(WiFi.RSSI());
  Serial.println(" dBm");
}

void loop() {

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("¡Se perdió la conexión WiFi!");
    handleConnectionFailure();
    delay(10000); // Espera 10 segundos antes de reintentar
    return;
  }

  if (millis() - lastMeasurement >= SAMPLE_TIME) {
    lastMeasurement = millis();
    
    // Tomar muestras y promediar
    long sum = 0;
    int samples = 0;
    unsigned long start = millis();
    
    while (millis() - start < SAMPLE_TIME) {
      sum += WiFi.RSSI();
      samples++;
      delay(50); // Pequeña pausa entre muestras
    }
    
    rssi = sum / samples;
    calculateDistance();
    printResults();
  }
}

void calculateDistance() {
  exponente = (RSSI1 - rssi) / (10.0 * n);
  distance = x1 * pow(10.0, exponente);
}

void printResults() {
  Serial.print("\nRSSI promedio: ");
  Serial.print(rssi);
  Serial.print(" dBm | Muestras: ");
  Serial.println((SAMPLE_TIME / 50) + 1); // Estimación de muestras
  
  if (rssi >= -50) Serial.println("Excelente señal");
  else if (rssi >= -60) Serial.println("Buena señal");
  else if (rssi >= -70) Serial.println("Señal moderada");
  else Serial.println("Señal débil");
  
  Serial.print("Distancia estimada: ");
  Serial.print(distance);
  Serial.println(" metros");
}

void handleConnectionFailure() {
  Serial.println("\n--- Diagnóstico de conexión ---");
  Serial.print("Estado actual de WiFi: ");
  
  switch(WiFi.status()) {
    case WL_NO_SHIELD:
      Serial.println("WiFi no disponible (¿módulo no detectado?)");
      break;
    case WL_IDLE_STATUS:
      Serial.println("En proceso de conexión");
      break;
    case WL_NO_SSID_AVAIL:
      Serial.println("Red no encontrada (¿SSID incorrecto?)");
      break;
    case WL_SCAN_COMPLETED:
      Serial.println("Escaneo completado");
      break;
    case WL_CONNECTED:
      Serial.println("Conectado (esto no debería aparecer como error)");
      break;
    case WL_CONNECT_FAILED:
      Serial.println("Fallo en la conexión (¿contraseña incorrecta?)");
      break;
    case WL_CONNECTION_LOST:
      Serial.println("Conexión perdida");
      break;
    case WL_DISCONNECTED:
      Serial.println("Desconectado");
      break;
    default:
      Serial.println("Estado desconocido");
  }
  
  Serial.println("Reintentando conexión...");
  WiFi.begin(ssid, password); // Intenta reconectar
}
