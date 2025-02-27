import matplotlib.pyplot as plt
import numpy as np

frecuencia1 = 100000  # Frecuencia en Hz
tiempo_total1 = 0.00004  # Tiempo total en segundos
frecuencia = 2000  # Frecuencia en Hz
tiempo_total = 0.0025  # Tiempo total en segundos

# Indice de modulacion
m= 1.5

# Crear el array de tiempo
tiempo1 = np.arange(0, tiempo_total1, 0.00000000001)
tiempo = np.arange(0, tiempo_total, 0.00001)

# Calcular la señal sinusoidal
amplitud1 = 24
amplitud = 6
senial1 = amplitud1 * np.cos(2 * np.pi * frecuencia1 * tiempo)
senial10 = amplitud1 * np.cos(2 * np.pi * frecuencia1 * tiempo1)
senial = amplitud * np.cos(2 * np.pi * frecuencia * tiempo)

# Encontrar los índices del pico y el valle
pico_indice1 = np.argmax(senial1)
valle_indice1 = np.argmin(senial1)
pico_indice = np.argmax(senial)
valle_indice = np.argmin(senial)

# Obtener los valores de tiempo y amplitud correspondientes
tiempo_pico1 = tiempo1[pico_indice1]
amplitud_pico1 = senial1[pico_indice1]

tiempo_valle1 = tiempo1[valle_indice1]
amplitud_valle1 = senial1[valle_indice1]

tiempo_pico = tiempo1[pico_indice]
amplitud_pico = senial[pico_indice]

tiempo_valle = tiempo1[valle_indice]
amplitud_valle = senial[valle_indice]

# Graficar la señal
plt.plot(tiempo1, senial10)
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

Modulada= amplitud1 *np.cos(2* np.pi * frecuencia1 * tiempo + m *senial)

plt.plot(tiempo, Modulada)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal modulada')
plt.grid(True)
plt.show()
