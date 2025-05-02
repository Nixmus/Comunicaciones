#include <WiFi.h>
#include <DNSServer.h>
#include <esp_wifi.h>
#include <tcpip_adapter.h>

// Configuración de red
const char* ssid = "ESP32-123456";           // Nombre de la red WiFi
const char* password = "12345678";       // Contraseña (mínimo 8 caracteres)
const int maxClientes = 20;              // Máximo número de clientes permitidos (default es 4)
const int canal = 1;                     // Canal WiFi (1-13)
const bool ocultarRed = false;           // No ocultar la red
const IPAddress ip(192, 168, 4, 1);      // IP estática para el AP

// Para DNS captivo (opcional)
DNSServer dnsServer;
const byte DNS_PORT = 53;

// Variables para monitoreo
unsigned long ultimoTiempo = 0;
const unsigned long intervalo = 5000;    // Intervalo de reporte en ms

void setup() {
  Serial.begin(115200);
  delay(1000);  // Espera para estabilización del monitor serial
  
  Serial.println("\n===========================");
  Serial.println("Iniciando Punto de Acceso WiFi...");
  
  // Configurar como AP
  WiFi.mode(WIFI_AP);                   // Modo Access Point explícito
  
  // Configurar el tiempo de inactividad para que no desconecte clientes
  // (0 significa que nunca se desconectan por inactividad)
  wifi_config_t conf;
  esp_wifi_get_config(WIFI_IF_AP, &conf);
  conf.ap.beacon_interval = 100;    // Intervalo de beacon más frecuente (default es 100)
  conf.ap.authmode = WIFI_AUTH_WPA2_PSK;  // Seguridad mejorada
  esp_wifi_set_config(WIFI_IF_AP, &conf);
  
  // Aumentar el poder de transmisión para mejorar el alcance
  esp_wifi_set_max_tx_power(82);  // El valor máximo es 82, representa 20.5 dBm
  
  // Configurar IP estática para el AP
  WiFi.softAPConfig(ip, ip, IPAddress(255, 255, 255, 0));
  
  // Iniciar AP con configuración expandida
  if (WiFi.softAP(ssid, password, canal, ocultarRed, maxClientes)) {
    Serial.println("¡AP iniciado correctamente!");
    Serial.print("Nombre de la red: ");
    Serial.println(ssid);
    Serial.print("IP del AP: ");
    Serial.println(WiFi.softAPIP());
    Serial.print("Máximo de clientes: ");
    Serial.println(maxClientes);
    
    // Configurar DNS captivo (opcional - redirige todas las solicitudes DNS al ESP32)
    dnsServer.start(DNS_PORT, "*", ip);
    
    // Obtener y mostrar la configuración del AP
    uint8_t mac[6];
    WiFi.softAPmacAddress(mac);
    Serial.print("MAC del AP: ");
    Serial.printf("%02X:%02X:%02X:%02X:%02X:%02X\n", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
    
  } else {
    Serial.println("ERROR: Fallo al iniciar el AP");
    // Reintentar automáticamente
    Serial.println("Reiniciando el ESP32...");
    ESP.restart();
  }
  
  Serial.println("===========================");
}

void loop() {
  // Manejo del DNS captivo (si se está usando)
  dnsServer.processNextRequest();
  
  // Gestión de clientes y conexiones WiFi
  gestionClientes();
  
  // Comprobación periódica de clientes
  unsigned long tiempoActual = millis();
  if (tiempoActual - ultimoTiempo >= intervalo) {
    ultimoTiempo = tiempoActual;
    
    // Mostrar información de clientes
    mostrarInfoClientes();
  }
}

void gestionClientes() {
  // Funcionalidad para mejorar la gestión de conexiones
  // Esta función se ejecuta frecuentemente para mantener las conexiones estables
  
  // Verificar si el AP sigue activo, reiniciarlo si es necesario
  if (WiFi.getMode() != WIFI_AP && WiFi.getMode() != WIFI_AP_STA) {
    Serial.println("AP desactivado inesperadamente. Reiniciando...");
    reiniciarAP();
  }
}

void mostrarInfoClientes() {
  // Número de estaciones (clientes) conectadas
  int numClientes = WiFi.softAPgetStationNum();
  
  Serial.print("Estado del AP: ");
  Serial.println(WiFi.getMode() == WIFI_AP || WiFi.getMode() == WIFI_AP_STA ? "Activo" : "Inactivo");
  
  Serial.print("Clientes conectados: ");
  Serial.println(numClientes);
  
  // Obtener y mostrar MAC de los clientes conectados
  wifi_sta_list_t stationList;
  tcpip_adapter_sta_list_t adapterList;
  
  if (esp_wifi_ap_get_sta_list(&stationList) == ESP_OK) {
    if (tcpip_adapter_get_sta_list(&stationList, &adapterList) == ESP_OK) {
      Serial.println("Lista de clientes conectados:");
      for (int i = 0; i < adapterList.num; i++) {
        tcpip_adapter_sta_info_t station = adapterList.sta[i];
        Serial.print("  Cliente ");
        Serial.print(i + 1);
        Serial.print(": MAC: ");
        Serial.print(String(station.mac[0], HEX) + ":" + 
                    String(station.mac[1], HEX) + ":" + 
                    String(station.mac[2], HEX) + ":" + 
                    String(station.mac[3], HEX) + ":" + 
                    String(station.mac[4], HEX) + ":" + 
                    String(station.mac[5], HEX));
        Serial.print(", IP: ");
        Serial.println(IPAddress(station.ip.addr).toString());
      }
    }
  }
  
  Serial.print("Memoria libre: ");
  Serial.print(ESP.getFreeHeap() / 1024);
  Serial.println(" KB");
  
  Serial.println("---------------------------");
}

void reiniciarAP() {
  Serial.println("Reiniciando punto de acceso WiFi...");
  WiFi.softAPdisconnect(true);
  delay(1000);
  
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(ip, ip, IPAddress(255, 255, 255, 0));
  
  if (WiFi.softAP(ssid, password, canal, ocultarRed, maxClientes)) {
    Serial.println("AP reiniciado correctamente");
  } else {
    Serial.println("Error al reiniciar AP. Reiniciando ESP32...");
    delay(3000);
    ESP.restart();
  }
}
