#include <WiFiS3.h>

// Configura tus credenciales de red
const char* ssid = "WIFIALEJO";     // Reemplaza con el nombre de tu hotspot
const char* password = "NANANANA";      // Reemplaza con tu contraseña

// Tiempo máximo de espera para conexión (milisegundos)
const unsigned long TIMEOUT_MS = 20000; // 20 segundos

void setup() {
  Serial.begin(9600);
  while (!Serial);  // Espera a que se inicialice el puerto serial

  Serial.print("Conectando a ");
  Serial.println(ssid);
  
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
  // Verifica continuamente el estado de la conexión
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("¡Se perdió la conexión WiFi!");
    handleConnectionFailure();
    delay(10000); // Espera 10 segundos antes de reintentar
    return;
  }
  
  // Si está conectado, muestra la potencia de la señal
  long rssi = WiFi.RSSI();
  
  Serial.print("Potencia de la señal: ");
  Serial.print(rssi);
  Serial.println(" dBm");
  
  // Interpretación de la potencia
  if (rssi >= -50) {
    Serial.println("Excelente señal");
  } else if (rssi >= -60) {
    Serial.println("Buena señal");
  } else if (rssi >= -70) {
    Serial.println("Señal moderada");
  } else {
    Serial.println("Señal débil - considere acercarse al router");
  }
  
  delay(5000);  // Espera 5 segundos antes de la próxima medición
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
