import matplotlib.pyplot as plt
import numpy as np

frecuencia1 = 8000  # Frecuencia en Hz
tiempo_total1 = 0.0005  # Tiempo total en segundos
frecuencia = 6000  # Frecuencia en Hz
tiempo_total = 0.0025  # Tiempo total en segundos


# Indice de modulacion
m= 1

# Crear el array de tiempo
tiempo1 = np.arange(0, tiempo_total1, 0.000000001)
tiempo = np.arange(0, tiempo_total, 0.00000001)

# Calcular la señal sinusoidal
amplitud1 = 1
amplitud = 1
senial1 = amplitud1 * np.cos(2 * np.pi * frecuencia1 * tiempo1)
senial = amplitud * np.cos(2 * np.pi * frecuencia * tiempo)

#señal modulada
Modulada= amplitud1 *np.cos(2* np.pi * frecuencia1 * tiempo + m *senial)

# Graficar la señal
plt.plot(tiempo1, senial1)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal Portadora')
plt.grid(True)
plt.show()

# Graficar la señal
plt.plot(tiempo, senial)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal moduladora')
plt.grid(True)
plt.show()

#señal modulada
plt.plot(tiempo, Modulada)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal modulada')
plt.grid(True)
plt.show()

# Graficar las señales
fig, axs = plt.subplots(2, 2, figsize=(12, 12))
fig.suptitle('Señales de 1kHz, 5kHz y 10kHz')
