import numpy as np
import matplotlib.pyplot as plt

# 1. Entrada: Solicitar un carácter ASCII
char_input = input('Ingrese un caracter ASCII: ')

# Convertir el carácter a su valor ASCII
ascii_val = ord(char_input)
print(f'El valor ASCII de "{char_input}" es {ascii_val}')

# Convertir a cadena binaria de 8 bits
bin_str = format(ascii_val, '08b')
print(f'La representación binaria de "{char_input}" es {bin_str}')

# 2. Parámetros para la simulación
bit_time = 1                # Duración de cada bit (en segundos)
samples_per_bit = 100       # Número de muestras por bit
T = bit_time / samples_per_bit  # Intervalo de muestreo
num_bits = len(bin_str)      
total_samples = num_bits * samples_per_bit
t = np.arange(0, num_bits * bit_time, T)  # Vector de tiempo

# 3. Inicialización de señales
NRZ_signal = np.zeros(total_samples)
RZ_signal = np.zeros(total_samples)
Man_signal = np.zeros(total_samples)
AMI_signal = np.zeros(total_samples)

# 4. Generación de las señales según el código de línea
# Variable para alternar la polaridad en AMI
current_polarity = 1  # Comenzamos con polaridad positiva

for bit in range(num_bits):
    # Índices de la muestra para el bit actual
    idx_start = bit * samples_per_bit
    idx_end = (bit + 1) * samples_per_bit
    current_bit = bin_str[bit]  # '0' o '1'
    
    # Código NRZ: Nivel alto (1) para '1', bajo (0) para '0'
    if current_bit == '1':
        NRZ_signal[idx_start:idx_end] = 1
    else:
        NRZ_signal[idx_start:idx_end] = 0
    
    # Código RZ (Return-to-Zero):
    # Se utiliza la primera mitad del intervalo para el nivel (1 o 0)
    # y la segunda mitad se retorna a cero.
    half_bit = samples_per_bit // 2
    if current_bit == '1':
        RZ_signal[idx_start:idx_start + half_bit] = 1
    else:
        RZ_signal[idx_start:idx_start + half_bit] = 0
    RZ_signal[idx_start + half_bit:idx_end] = 0
    
    # Código Manchester:
    # Convención:
    # - Para '1': primera mitad baja (0) y segunda mitad alta (1)
    # - Para '0': primera mitad alta (1) y segunda mitad baja (0)
    if current_bit == '1':
        Man_signal[idx_start:idx_start + half_bit] = 0
        Man_signal[idx_start + half_bit:idx_end] = 1
    else:
        Man_signal[idx_start:idx_start + half_bit] = 1
        Man_signal[idx_start + half_bit:idx_end] = 0
    
    # Código Bipolar AMI:
    # Para '0': nivel 0
    # Para '1': asigna un pulso con polaridad alterna.
    if current_bit == '1':
        AMI_signal[idx_start:idx_end] = current_polarity
        # Cambia la polaridad para el siguiente bit '1'
        current_polarity = -current_polarity
    else:
        AMI_signal[idx_start:idx_end] = 0

# 5. Graficar las señales
plt.figure(figsize=(10, 8))

# Subplot para NRZ
plt.subplot(4, 1, 1)
plt.plot(t, NRZ_signal, linewidth=2)
plt.ylim([-1.5, 1.5])
plt.grid(True)
plt.title('Código de línea NRZ')
plt.xlabel('Tiempo (s)')
plt.ylabel('Nivel')

# Subplot para RZ
plt.subplot(4, 1, 2)
plt.plot(t, RZ_signal, linewidth=2)
plt.ylim([-1.5, 1.5])
plt.grid(True)
plt.title('Código de línea RZ')
plt.xlabel('Tiempo (s)')
plt.ylabel('Nivel')

# Subplot para Manchester
plt.subplot(4, 1, 3)
plt.plot(t, Man_signal, linewidth=2)
plt.ylim([-1.5, 1.5])
plt.grid(True)
plt.title('Código de línea Manchester')
plt.xlabel('Tiempo (s)')
plt.ylabel('Nivel')

# Subplot para AMI
plt.subplot(4, 1, 4)
plt.plot(t, AMI_signal, linewidth=2)
plt.ylim([-1.5, 1.5])
plt.grid(True)
plt.title('Código Bipolar AMI')
plt.xlabel('Tiempo (s)')
plt.ylabel('Nivel')

plt.tight_layout()
plt.show()
