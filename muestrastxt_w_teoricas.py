import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definir la ruta del archivo
file_path = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\muestras.txt'
file_path1 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\muestras2.txt'
file_path2 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\muestras11.txt'
file_path3 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\muestras21.txt'
file_path4 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\muestras31.txt'
file_path5 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\muestras41.txt'
file_path6 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\muestras51.txt'
file_path7 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\muestras61.txt'




# Cargar el archivo txt saltando la primera línea (header)
data= np.loadtxt(file_path, skiprows=1)
data1 = np.loadtxt(file_path1, skiprows=1)
data2 = np.loadtxt(file_path2, skiprows=1)
data3 = np.loadtxt(file_path3, skiprows=1)
data4 = np.loadtxt(file_path4, skiprows=1)
data5 = np.loadtxt(file_path5, skiprows=1)
data6 = np.loadtxt(file_path6, skiprows=1)
data7 = np.loadtxt(file_path7, skiprows=1)

#Teoricas

A =1
f = 200
DC = 1.5
T = 1/f
t = np.arange(0, 4 * T, T / 1000)
fase = 3*np.pi/2 -0.8
VT= A * np.sin(2*np.pi*f*t+fase) + DC 

A1 =1
f1 = 100
DC1 = 1.5
T1 = 1/f1
t1 = np.arange(0, 2 * T1, T1 / 1000)
fase1 = 0.7
VT1= A1 * np.sin(2*np.pi*f1*t1+fase1) + DC1 

A2 =1
f2 = 300
DC2 = 1.5
T2 = 1/f2
t2 = np.arange(0, 6 * T2, T2 / 1000)
fase2 = 3.4
VT2= A2 * np.sin(2*np.pi*f2*t2+fase2) + DC2 

A3 =1
f3 = 600
DC3 = 1.5
T3 = 1/f3
t3 = np.arange(0, 12 * T3, T3 / 1000)
fase3 = 3*np.pi/2
VT3= A3 * np.sin(2*np.pi*f3*t3+fase3) + DC3 

A4 =1
f4 = 900
DC4 = 1.5
T4 = 1/f4
t4 = np.arange(0, 18 * T4, T4 / 1000)
fase4 = 4.8
VT4= A4 * np.sin(2*np.pi*f4*t4+fase4) + DC4 

A5 =1
f5 = 1500
DC5 = 1.5
T5 = 1/f5
t5 = np.arange(0, 30 * T5, T5 / 1000)
fase5 = 5
VT5= A5 * np.sin(2*np.pi*f5*t5+fase5) + DC5 

A6 =1
f6 = 1800
DC6 = 1.5
T6 = 1/f6
t6 = np.arange(0, 36 * T6, T6 / 1000)
fase6 = 3*np.pi/2
VT6= A6 * np.sin(2*np.pi*f6*t6+fase6) + DC6 

A7 = 1
f7 = 100
DC7 = 1.5
T7 = 1/f7
t7 = np.arange(0, 2 * T7, T7 / 1000)
fase7 = -1
duty7 = 0.5 
VT7 = A7 * signal.square(2 * np.pi * f7 * t7 + fase7, duty7) + DC7

# Separar las columnas
x = data[:37, 0]  # Primera columna
y = data[:37, 1]  # Segunda columna

# Separar las columnas
x1 = data1[:37, 0]  # Primera columna
y1 = data1[:37, 1]  # Segunda columna

# Separar las columnas
x2 = data2[:37, 0]  # Primera columna
y2 = data2[:37, 1]  # Segunda columna

# Separar las columnas
x3 = data3[:37, 0]  # Primera columna
y3 = data3[:37, 1]  # Segunda columna

# Separar las columnas
x4 = data4[:37, 0]  # Primera columna
y4 = data4[:37, 1]  # Segunda columna

# Separar las columnas
x5 = data5[:37, 0]  # Primera columna
y5 = data5[:37, 1]  # Segunda columna

# Separar las columnas
x6 = data6[:37, 0]  # Primera columna
y6 = data6[:37, 1]  # Segunda columna

# Separar las columnas
x7 = data7[:37, 0]  # Primera columna
y7 = data7[:37, 1]  # Segunda columna


# Primera figura
fig, axs = plt.subplots(2, 2, figsize=(12, 12))
fig.suptitle('Señales laboratorio', fontsize=16)
plt.subplots_adjust(hspace=0.3)

stem_params = {
    'linefmt': 'b-',     
    'markerfmt': 'bo',    
    'basefmt': 'r-'       
}

markerline1, stemlines1, baseline1 = axs[0, 0].stem(x1, y1, **stem_params)
axs[0, 0].plot(t1, VT1, label='Teórica')
axs[0, 0].set_title('100 Hz')
axs[0, 0].grid(True, linestyle='--', alpha=0.7)

markerline2, stemlines2, baseline2 = axs[0, 1].stem(x2, y2, **stem_params)
axs[0, 1].plot(t2, VT2, label='Teórica')
axs[0, 1].set_title('300 Hz')
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

markerline3, stemlines3, baseline3 = axs[1, 0].stem(x3, y3, **stem_params)
axs[1, 0].plot(t3, VT3, label='Teórica')
axs[1, 0].set_title('600 Hz')
axs[1, 0].grid(True, linestyle='--', alpha=0.7)

markerline4, stemlines4, baseline4 = axs[1, 1].stem(x4, y4, **stem_params)
axs[1, 1].plot(t4, VT4, label='Teórica')
axs[1, 1].set_title('900 Hz')
axs[1, 1].grid(True, linestyle='--', alpha=0.7)

# Añadir etiquetas a todos los gráficos
for ax in [axs[0,0], axs[0,1], axs[1,0], axs[1,1]]:
    ax.set_ylabel('Voltaje (V)')
    ax.set_xlabel('Tiempo (S)')
    
    
# Segunda figura
fig, axs = plt.subplots(2, 2, figsize=(12, 12))
fig.suptitle('Señales laboratorio', fontsize=16)
plt.subplots_adjust(hspace=0.3)

stem_params = {
    'linefmt': 'b-',     
    'markerfmt': 'bo',    
    'basefmt': 'r-'       
}    
    
markerline5, stemlines5, baseline5 = axs[0, 0].stem(x5, y5, **stem_params)
axs[0, 0].plot(t5, VT5, label='Teórica')
axs[0, 0].set_title('1500 Hz')
axs[0, 0].grid(True, linestyle='--', alpha=0.7)

markerline6, stemlines6, baseline6 = axs[0, 1].stem(x6, y6, **stem_params)
axs[0, 1].plot(t6, VT6, label='Teórica')
axs[0, 1].set_title('1800 Hz')
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

markerline7, stemlines7, baseline7 = axs[1, 0].stem(x7, y7, **stem_params)
axs[1, 0].plot(t7, VT7, label='Teórica')
axs[1, 0].set_title('square 100 Hz')
axs[1, 0].grid(True, linestyle='--', alpha=0.7)

markerline8, stemlines8, baseline8 = axs[1, 1].stem(x, y, **stem_params)
axs[1, 1].plot(t, VT, label='Teórica')
axs[1, 1].set_title('200 Hz')
axs[1, 1].grid(True, linestyle='--', alpha=0.7)

# Añadir etiquetas a todos los gráficos
for ax in [axs[0,0], axs[0,1], axs[1,0], axs[1,1]]:
    ax.set_ylabel('Voltaje (V)')
    ax.set_xlabel('Tiempo (S)')
    
# Ajustar el tamaño de los marcadores
for markerline in [markerline1, markerline2, markerline3, markerline4, markerline5, markerline6, markerline7, markerline8]:
    plt.setp(markerline, markersize=4)

plt.show()
