/*
 * Código para ESP32 con MPU6050 y Punto de Acceso WiFi
 * Combina lectura de sensor MPU6050 y creación de AP WiFi
 * Permite monitorear datos de movimiento a través de una conexión WiFi
 */

#include <Wire.h>
#include <WiFi.h>
#include <DNSServer.h>
#include <esp_wifi.h>
#include <WebServer.h>
#include <ArduinoJson.h>

// Configuración de red
const char* ssid = "ESP32-MPU6050";
const char* password = "12345678";
const int maxClientes = 20;
const int canal = 1;
const bool ocultarRed = false;
const IPAddress ip(192, 168, 4, 1);

// DNS cautivo
DNSServer dnsServer;
const byte DNS_PORT = 53;

// Servidor web HTTP
WebServer server(80);

// Variables de monitoreo WiFi
unsigned long ultimoTiempoWiFi = 0;
const unsigned long intervaloWiFi = 5000;  // 5 segundos

// Variables para MPU6050
// Variables para almacenar datos del sensor
int16_t ax, ay, az;
int16_t gx, gy, gz;

// Variables para cálculos
float accelX, accelY, accelZ;
float gyroX, gyroY, gyroZ;

// Variables para calcular velocidad
float velocidadX = 0;
float velocidadY = 0;
float velocidadZ = 0;

// Variables para calcular ángulos
float anguloX = 0;
float anguloY = 0;
float anguloZ = 0;

// Factores de conversión
const float accelFactor = 16384.0; // Para ±2g (1g = 9.8 m/s²)
const float gyroFactor = 131.0;    // Para ±250°/s

// Variables para tiempo MPU6050
unsigned long tiempoActualMPU = 0;
unsigned long tiempoPrevioMPU = 0;
float deltaT = 0;

// Variables para compartir datos del sensor
unsigned long ultimoTiempoSensor = 0;
const unsigned long intervaloSensor = 100;  // 100ms para actualizar lecturas del sensor

// ========= SETUP =========
void setup() {
  // Iniciar comunicación serial
  Serial.begin(115200);
  delay(1000);
  Serial.println("\n===========================");
  Serial.println("Iniciando ESP32 con MPU6050 y AP WiFi...");
  
  // Iniciar comunicación I2C para MPU6050
  Wire.begin();
  
  Serial.println("Inicializando MPU6050...");
  
  // Inicializar MPU6050
  Wire.beginTransmission(0x68); // Dirección I2C del MPU6050
  Wire.write(0x6B);             // Registro PWR_MGMT_1
  Wire.write(0);                // Inicializar - salir del modo sleep
  Wire.endTransmission(true);
  
  // Configurar el giroscopio (FS_SEL = 0)
  Wire.beginTransmission(0x68);
  Wire.write(0x1B);  // Registro GYRO_CONFIG
  Wire.write(0x00);  // Rango ±250°/s
  Wire.endTransmission(true);
  
  // Configurar el acelerómetro (AFS_SEL = 0)
  Wire.beginTransmission(0x68);
  Wire.write(0x1C);  // Registro ACCEL_CONFIG
  Wire.write(0x00);  // Rango ±2g
  Wire.endTransmission(true);
  
  Serial.println("MPU6050 inicializado correctamente!");
  
  // Iniciar tiempo para MPU6050
  tiempoPrevioMPU = millis();

  // Configurar como AP WiFi
  WiFi.mode(WIFI_AP);

  // Ajustes avanzados del AP
  wifi_config_t conf;
  esp_wifi_get_config(WIFI_IF_AP, &conf);
  conf.ap.beacon_interval = 100;
  conf.ap.authmode = WIFI_AUTH_WPA2_PSK;
  esp_wifi_set_config(WIFI_IF_AP, &conf);
  esp_wifi_set_max_tx_power(82);

  WiFi.softAPConfig(ip, ip, IPAddress(255, 255, 255, 0));

  if (WiFi.softAP(ssid, password, canal, ocultarRed, maxClientes)) {
    Serial.println("¡AP WiFi iniciado correctamente!");
    Serial.print("IP del AP: ");
    Serial.println(WiFi.softAPIP());
    dnsServer.start(DNS_PORT, "*", ip);

    uint8_t mac[6];
    WiFi.softAPmacAddress(mac);
    Serial.printf("MAC del AP: %02X:%02X:%02X:%02X:%02X:%02X\n",
                  mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
  } else {
    Serial.println("ERROR: Fallo al iniciar el AP. Reiniciando...");
    ESP.restart();
  }

  // Configurar servidor web
  server.on("/", HTTP_GET, handleRoot);
  server.on("/datos", HTTP_GET, handleDatos);
  server.on("/rssi", HTTP_POST, handleRSSI);
  server.begin();
  Serial.println("Servidor HTTP iniciado");
  Serial.println("===========================");
}

// ========= LOOP =========
void loop() {
  // Procesar solicitudes DNS y HTTP
  dnsServer.processNextRequest();
  server.handleClient();

  // Gestionar clientes WiFi
  gestionClientes();

  // Mostrar info de clientes cada cierto tiempo
  unsigned long tiempoActual = millis();
  if (tiempoActual - ultimoTiempoWiFi >= intervaloWiFi) {
    ultimoTiempoWiFi = tiempoActual;
    mostrarInfoClientes();
  }

  // Actualizar datos del sensor MPU6050
  if (tiempoActual - ultimoTiempoSensor >= intervaloSensor) {
    ultimoTiempoSensor = tiempoActual;
    actualizarMPU6050();
  }
}

// ========= Funciones MPU6050 =========
void actualizarMPU6050() {
  // Obtener tiempo actual para cálculos del sensor
  tiempoActualMPU = millis();
  deltaT = (tiempoActualMPU - tiempoPrevioMPU) / 1000.0; // Convertir a segundos
  tiempoPrevioMPU = tiempoActualMPU;
  
  // Leer datos del acelerómetro y giroscopio
  Wire.beginTransmission(0x68);
  Wire.write(0x3B);  // Registro ACCEL_XOUT_H
  Wire.endTransmission(false);
  Wire.requestFrom(0x68, 14, true);  // Solicitar 14 bytes
  
  // Leer datos del acelerómetro
  ax = Wire.read() << 8 | Wire.read();  // ACCEL_XOUT_H y ACCEL_XOUT_L
  ay = Wire.read() << 8 | Wire.read();  // ACCEL_YOUT_H y ACCEL_YOUT_L
  az = Wire.read() << 8 | Wire.read();  // ACCEL_ZOUT_H y ACCEL_ZOUT_L
  
  // Saltar registro de temperatura (2 bytes)
  Wire.read(); Wire.read();
  
  // Leer datos del giroscopio
  gx = Wire.read() << 8 | Wire.read();  // GYRO_XOUT_H y GYRO_XOUT_L
  gy = Wire.read() << 8 | Wire.read();  // GYRO_YOUT_H y GYRO_YOUT_L
  gz = Wire.read() << 8 | Wire.read();  // GYRO_ZOUT_H y GYRO_ZOUT_L
  
  // Convertir a unidades utilizables
  accelX = ax / accelFactor * 9.8;  // Convertir a m/s²
  accelY = ay / accelFactor * 9.8;  // Convertir a m/s²
  accelZ = az / accelFactor * 9.8;  // Convertir a m/s²
  
  gyroX = gx / gyroFactor;  // Convertir a °/s
  gyroY = gy / gyroFactor;  // Convertir a °/s
  gyroZ = gz / gyroFactor;  // Convertir a °/s
  
  // Calcular velocidad mediante integración de la aceleración
  velocidadX += accelX * deltaT;
  velocidadY += accelY * deltaT;
  velocidadZ += accelZ * deltaT;
  
  // Calcular ángulos usando el acelerómetro
  // Fórmulas basadas en trigonometría
  float accelAngleX = atan2(accelY, sqrt(accelX * accelX + accelZ * accelZ)) * 180.0 / PI;
  float accelAngleY = atan2(-accelX, sqrt(accelY * accelY + accelZ * accelZ)) * 180.0 / PI;
  
  // Calcular ángulos usando el giroscopio e integración
  anguloX += gyroX * deltaT;
  anguloY += gyroY * deltaT;
  anguloZ += gyroZ * deltaT;
  
  // Aplicar filtro complementario para combinar datos del acelerómetro y giroscopio
  // El filtro usa 98% del giroscopio y 2% del acelerómetro para X e Y
  anguloX = 0.98 * anguloX + 0.02 * accelAngleX;
  anguloY = 0.98 * anguloY + 0.02 * accelAngleY;
  
  // Opcional: implementar detección de movimiento nulo para resetear velocidad
  // Esto ayuda a evitar la deriva
  if (abs(accelX) < 0.1 && abs(accelY) < 0.1 && abs(accelZ - 9.8) < 0.1) {
    velocidadX = 0;
    velocidadY = 0;
    velocidadZ = 0;
  }
  
  // Solo mostrar en Serial para depuración (cuando sea necesario)
  /*
  Serial.println("------------------------------");
  Serial.print("Aceleración (m/s²): X=");
  Serial.print(accelX);
  Serial.print(" Y=");
  Serial.print(accelY);
  Serial.print(" Z=");
  Serial.println(accelZ);
  
  Serial.print("Velocidad (m/s): X=");
  Serial.print(velocidadX);
  Serial.print(" Y=");
  Serial.print(velocidadY);
  Serial.print(" Z=");
  Serial.println(velocidadZ);
  
  Serial.print("Ángulos (grados): X=");
  Serial.print(anguloX);
  Serial.print(" Y=");
  Serial.print(anguloY);
  Serial.print(" Z=");
  Serial.println(anguloZ);
  */
}

// ========= Funciones Servidor Web =========
void handleRoot() {
  String html = "<!DOCTYPE html>"
                "<html>"
                "<head>"
                "  <meta charset='UTF-8'>"
                "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>"
                "  <title>ESP32 MPU6050 Monitor</title>"
                "  <style>"
                "    body { font-family: Arial, sans-serif; margin: 20px; }"
                "    h1 { color: #0066cc; }"
                "    .container { margin: 20px 0; }"
                "    .data-box { border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin: 10px 0; background-color: #f9f9f9; }"
                "    .refresh-btn { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }"
                "    .data-label { font-weight: bold; color: #555; }"
                "    .data-value { font-family: monospace; font-size: 16px; }"
                "  </style>"
                "</head>"
                "<body>"
                "  <h1>ESP32 MPU6050 Monitor</h1>"
                "  <div class='container'>"
                "    <button class='refresh-btn' onclick='fetchData()'>Actualizar Datos</button>"
                "    <div id='update-status'></div>"
                "  </div>"
                "  <div class='container'>"
                "    <h2>Aceleración (m/s²)</h2>"
                "    <div class='data-box'>"
                "      <div><span class='data-label'>X:</span> <span id='accelX' class='data-value'>--</span></div>"
                "      <div><span class='data-label'>Y:</span> <span id='accelY' class='data-value'>--</span></div>"
                "      <div><span class='data-label'>Z:</span> <span id='accelZ' class='data-value'>--</span></div>"
                "    </div>"
                "  </div>"
                "  <div class='container'>"
                "    <h2>Velocidad (m/s)</h2>"
                "    <div class='data-box'>"
                "      <div><span class='data-label'>X:</span> <span id='velX' class='data-value'>--</span></div>"
                "      <div><span class='data-label'>Y:</span> <span id='velY' class='data-value'>--</span></div>"
                "      <div><span class='data-label'>Z:</span> <span id='velZ' class='data-value'>--</span></div>"
                "    </div>"
                "  </div>"
                "  <div class='container'>"
                "    <h2>Ángulos (grados)</h2>"
                "    <div class='data-box'>"
                "      <div><span class='data-label'>X:</span> <span id='angX' class='data-value'>--</span></div>"
                "      <div><span class='data-label'>Y:</span> <span id='angY' class='data-value'>--</span></div>"
                "      <div><span class='data-label'>Z:</span> <span id='angZ' class='data-value'>--</span></div>"
                "    </div>"
                "  </div>"
                "  <script>"
                "    function fetchData() {"
                "      document.getElementById('update-status').innerHTML = 'Actualizando...';"
                "      fetch('/datos')"
                "        .then(response => response.json())"
                "        .then(data => {"
                "          document.getElementById('accelX').textContent = data.accel.x.toFixed(2);"
                "          document.getElementById('accelY').textContent = data.accel.y.toFixed(2);"
                "          document.getElementById('accelZ').textContent = data.accel.z.toFixed(2);"
                "          document.getElementById('velX').textContent = data.vel.x.toFixed(2);"
                "          document.getElementById('velY').textContent = data.vel.y.toFixed(2);"
                "          document.getElementById('velZ').textContent = data.vel.z.toFixed(2);"
                "          document.getElementById('angX').textContent = data.ang.x.toFixed(2);"
                "          document.getElementById('angY').textContent = data.ang.y.toFixed(2);"
                "          document.getElementById('angZ').textContent = data.ang.z.toFixed(2);"
                "          document.getElementById('update-status').innerHTML = 'Actualizado: ' + new Date().toLocaleTimeString();"
                "        })"
                "        .catch(error => {"
                "          document.getElementById('update-status').innerHTML = 'Error al actualizar datos';"
                "          console.error('Error:', error);"
                "        });"
                "    }"
                "    // Actualizar datos al cargar página"
                "    fetchData();"
                "    // Actualizar automáticamente cada 2 segundos"
                "    setInterval(fetchData, 2000);"
                "  </script>"
                "</body>"
                "</html>";
  
  server.send(200, "text/html", html);
}

void handleDatos() {
  // Crear objeto JSON con los datos del MPU6050
  StaticJsonDocument<300> jsonDoc;
  
  JsonObject accel = jsonDoc.createNestedObject("accel");
  accel["x"] = accelX;
  accel["y"] = accelY;
  accel["z"] = accelZ;
  
  JsonObject vel = jsonDoc.createNestedObject("vel");
  vel["x"] = velocidadX;
  vel["y"] = velocidadY;
  vel["z"] = velocidadZ;
  
  JsonObject ang = jsonDoc.createNestedObject("ang");
  ang["x"] = anguloX;
  ang["y"] = anguloY;
  ang["z"] = anguloZ;
  
  String jsonString;
  serializeJson(jsonDoc, jsonString);
  
  server.send(200, "application/json", jsonString);
}

void handleRSSI() {
  if (!server.hasArg("plain")) {
    server.send(400, "text/plain", "Body no encontrado");
    return;
  }

  String body = server.arg("plain");
  StaticJsonDocument<200> jsonDoc;
  DeserializationError error = deserializeJson(jsonDoc, body);
  if (error) {
    server.send(400, "application/json", "{\"error\":\"JSON inválido\"}");
    return;
  }

  int id = jsonDoc["id"];
  int rssi = jsonDoc["rssi"];

  Serial.printf("📡 Recibido RSSI -> ID: %d, RSSI: %d dBm\n", id, rssi);

  server.send(200, "application/json", "{\"status\":\"OK\"}");
}

// ========= Funciones WiFi =========
void gestionClientes() {
  if (WiFi.getMode() != WIFI_AP && WiFi.getMode() != WIFI_AP_STA) {
    Serial.println("AP desactivado inesperadamente. Reiniciando...");
    reiniciarAP();
  }
}

void mostrarInfoClientes() {
  int numClientes = WiFi.softAPgetStationNum();
  Serial.printf("Clientes conectados: %d\n", numClientes);

  wifi_sta_list_t stationList;
  tcpip_adapter_sta_list_t adapterList;

  if (esp_wifi_ap_get_sta_list(&stationList) == ESP_OK &&
      tcpip_adapter_get_sta_list(&stationList, &adapterList) == ESP_OK) {
    for (int i = 0; i < adapterList.num; i++) {
      tcpip_adapter_sta_info_t station = adapterList.sta[i];
      Serial.printf("  Cliente %d - MAC: %02X:%02X:%02X:%02X:%02X:%02X, IP: %s\n",
        i + 1,
        station.mac[0], station.mac[1], station.mac[2],
        station.mac[3], station.mac[4], station.mac[5],
        IPAddress(station.ip.addr).toString().c_str());
    }
  }

  Serial.printf("Memoria libre: %lu KB\n", ESP.getFreeHeap() / 1024);
  Serial.println("---------------------------");
}

void reiniciarAP() {
  Serial.println("Reiniciando AP...");
  WiFi.softAPdisconnect(true);
  delay(1000);
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(ip, ip, IPAddress(255, 255, 255, 0));
  WiFi.softAP(ssid, password, canal, ocultarRed, maxClientes);
}
