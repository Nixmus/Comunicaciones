"""Transmisor NRF24L01 para Raspberry Pi Pico W en un canal específico."""

import struct
import utime
import network
from machine import Pin, SPI
from nrf24l01 import NRF24L01
from micropython import const

# Configuración de pines para NRF24L01
SPI_ID = 0
SCK_PIN = 2
MOSI_PIN = 3
MISO_PIN = 4
CSN_PIN = 5
CE_PIN = 6

# LED interno para indicación visual
led = Pin("LED", Pin.OUT)

# Canal de radio (0-125)
CANAL_RF = 21  # Puedes elegir cualquier canal entre 0 y 125
DATA_RATE = 1  # 1 = 2Mbps
RF_POWER = 3  # Nivel de potencia: 0 (mínimo) a 3 (máximo)

# Dirección para la comunicación (formato little-endian)
TX_ADDRESS = b"\xe1\xf0\xf0\xf0\xf0"  # 0xf0f0f0f0e1 en big-endian

# Configuración WiFi
SSID = "POCO X6 Pro 5G"
PASSWORD = "Danna178"

def setup_nrf24l01():
    """Configura el módulo NRF24L01 para transmisión."""
    # Configuración del SPI
    spi = SPI(SPI_ID, sck=Pin(SCK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN))
    
    # Configuración de pines de control
    csn = Pin(CSN_PIN, mode=Pin.OUT, value=1)
    ce = Pin(CE_PIN, mode=Pin.OUT, value=0)
    
    # Inicialización del módulo NRF24L01
    nrf = NRF24L01(spi, csn, ce, payload_size=8)
    
    # Configuración básica
    nrf.set_channel(CANAL_RF)
    
    # Configuración de velocidad y potencia (usando registro RF_SETUP)
    # 0x26 = 250kbps, potencia máxima (0x06 = 1Mbps, 0x04 = 2Mbps)
    nrf.reg_write(0x06, 0x26)  # 250kbps, potencia máxima
    
    # Configuración de dirección de transmisión
    nrf.open_tx_pipe(TX_ADDRESS)
    
    print(f"NRF24L01 configurado en canal {CANAL_RF}")
    return nrf

def conectar_wifi():
    """Conecta a la red WiFi especificada."""
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    
    if not wifi.isconnected():
        print(f"Conectando a {SSID}...")
        wifi.connect(SSID, PASSWORD)
        
        max_intentos = 10
        while not wifi.isconnected() and max_intentos > 0:
            print(".", end="")
            utime.sleep(1)
            max_intentos -= 1
    
    if wifi.isconnected():
        print("\n:D / Conectado al WiFi!")
        print(f"IP: {wifi.ifconfig()[0]}")
        return wifi
    else:
        print("\nu-u / Error: No se pudo conectar al WiFi")
        return None

def get_wifi_strength(wifi):
    """Obtiene la fuerza de la señal WiFi en dBm."""
    if wifi and wifi.isconnected():
        try:
            return wifi.status('rssi')
        except:
            return -100  # Valor por defecto
    return -100

def transmit_message(nrf, message_id, message_value):
    """Transmite un mensaje a través del NRF24L01."""
    led.on()
    success = False
    
    try:
        payload = struct.pack("ii", message_id, message_value)
        nrf.send(payload)
        print(f"Mensaje {message_id} enviado - Valor: {message_value} dBm")
        success = True
    except Exception as e:
        print(f"Error al transmitir: {e}")
    
    led.off()
    return success

def main():
    """Función principal para transmisión periódica."""
    print("\n--- Iniciando transmisor NRF24L01 ---")
    
    # Conectar WiFi
    wifi = conectar_wifi()
    
    # Configurar NRF24L01
    try:
        nrf = setup_nrf24l01()
    except Exception as e:
        print(f"Error crítico al configurar NRF24L01: {e}")
        return
    
    message_id = 0
    
    try:
        while True:
            rssi = get_wifi_strength(wifi)
            
            if transmit_message(nrf, message_id, rssi):
                message_id += 1
            
            utime.sleep(2)
            
    except KeyboardInterrupt:
        print("\nTransmisión detenida por el usuario")
    finally:
        if wifi:
            wifi.disconnect()

if __name__ == "__main__":
    main()
