import numpy as np
import matplotlib.pyplot as plt

#Teoricas
A =1
B = 0.5
C = 1.2
f = 1000
DC = 2.5
T = 0.002
t = np.arange(0, T, 2e-6)
fase = 0
VT= A * np.sin(2*np.pi*f*t+fase) 
VT1= B * np.sin(2*np.pi*2*f*t+fase) 
VT2= C * np.sin(2*np.pi*3*f*t+fase) 

VTT = VT + VT1 + VT2 + DC

plt.figure
plt.plot(t, VTT)
plt.grid(True)
plt.show()

def get_voltage_at_time(tiempo, t, VTT):
    # Encuentra el índice más cercano al tiempo especificado
    idx = np.abs(t - tiempo).argmin()
    return t[idx], VTT[idx]

# Sección interactiva para consultar voltajes
while True:
    try:
        tiempo_consulta = float(input("\nIngrese el tiempo a consultar (entre 0 y 0.002 segundos), o -1 para salir: "))
        if tiempo_consulta == -1:
            break
        if 0 <= tiempo_consulta <= T:
            tiempo_exacto, voltaje = get_voltage_at_time(tiempo_consulta, t, VTT)
            print(f"Tiempo: {tiempo_exacto:.6f} s")
            print(f"Voltaje: {voltaje:.3f} V")
        else:
            print("Tiempo fuera de rango. Por favor ingrese un valor entre 0 y 0.002")
    except ValueError:
        print("Por favor ingrese un número válido")
