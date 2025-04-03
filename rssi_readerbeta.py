import network
import time
# Configurar el WiFi
wifi = network.WLAN(network.STA_IF)  # Modo estación (cliente WiFi)
wifi.active(True)  # Activar la interfaz WiFi
# Datos de tu hotspot WiFi
SSID = "POCO X6 Pro 5G"  # Reemplaza con el nombre de tu hotspot
PASSWORD = "Danna178"  # Reemplaza con la contraseña
def conectar_wifi():
    # Conectar al WiFi
    wifi.connect(SSID, PASSWORD)

    # Esperar a que se conecte
    max_intentos = 10
    while not wifi.isconnected() and max_intentos > 0:
        print("Conectando...")
        time.sleep(1)
        max_intentos -= 1

    # Verificar conexión
    if wifi.isconnected():
        print("✅ Conectado al WiFi!")
        print("IP:", wifi.ifconfig()[0])  # Muestra la dirección IP asignada
    else:
        print("❌ Error: No se pudo conectar al WiFi")
# Primera conexión
conectar_wifi()
# Loop cada 5 segundos para verificar el estado
while True:
    if wifi.isconnected():
        rssi = wifi.status('rssi')
        print("\nEstado actual:")
        print("IP:", wifi.ifconfig()[0])
        print("RSSI:", rssi, "dBm")
        print("Señal:", end=' ')
        if rssi > -50:
            print("Excelente")
        elif rssi > -60:
            print("Buena")
        elif rssi > -70:
            print("Regular")
        else:
            print("Débil")
    else:
        print("\nWiFi desconectado. Intentando reconectar...")
        conectar_wifi()

    time.sleep(5) 
