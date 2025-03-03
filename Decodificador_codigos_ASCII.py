import numpy as np
import matplotlib.pyplot as plt

# 1. Entrada: Solicitar un carácter ASCII
char_input = input('Ingrese un caracter ASCII: ')

# Convertir el carácter a su valor ASCII y luego a cadena binaria de 8 bits
ascii_val = ord(char_input)
bin_str = format(ascii_val, '08b')
print(f'El valor ASCII de "{char_input}" es {ascii_val}')
print(f'La representación binaria de "{char_input}" es {bin_str}')

# 2. Parámetros para la simulación
bit_time = 1                # Duración de cada bit (en segundos)
samples_per_bit = 100       # Número de muestras por bit
T = bit_time / samples_per_bit  # Intervalo de muestreo
num_bits = len(bin_str)      
total_samples = num_bits * samples_per_bit
t = np.linspace(0, num_bits * bit_time, total_samples, endpoint=False)  # Vector de tiempo

# 3. Inicialización de señales
signals = {
    'NRZ': np.zeros(total_samples),
    'RZ': np.zeros(total_samples),
    'Manchester': np.zeros(total_samples),
    'AMI': np.zeros(total_samples)
}

# 4. Generación de las señales según el código de línea
current_polarity = 1  # Comenzamos con polaridad positiva

for bit_idx, bit in enumerate(bin_str):
    idx_start = bit_idx * samples_per_bit
    idx_end = (bit_idx + 1) * samples_per_bit
    half_bit = samples_per_bit // 2

    # NRZ
    signals['NRZ'][idx_start:idx_end] = int(bit)
    
    # RZ
    signals['RZ'][idx_start:idx_start + half_bit] = int(bit)
    
    # Manchester
    signals['Manchester'][idx_start:idx_start + half_bit] = 1 - int(bit)
    signals['Manchester'][idx_start + half_bit:idx_end] = int(bit)
    
    # AMI
    if bit == '1':
        signals['AMI'][idx_start:idx_end] = current_polarity
        current_polarity *= -1

# 5. Graficar las señales
plt.figure(figsize=(10, 8))

for i, (code, signal) in enumerate(signals.items(), 1):
    plt.subplot(4, 1, i)
    plt.plot(t, signal, linewidth=2)
    plt.ylim([-1.5, 1.5])
    plt.grid(True)
    plt.title(f'Código de línea {code}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Nivel')

plt.tight_layout()
plt.show()
