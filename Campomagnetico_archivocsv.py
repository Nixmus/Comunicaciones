#Bibliotecas y extensiones
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#data1
ruta_archivo= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/experimento campo magnetico phyphox/Raw Data.csv"
df = pd.read_csv(ruta_archivo)
#data2
ruta_archivo1= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/experimento campo magnetico phyphox/Raw Data1.csv"
df1 = pd.read_csv(ruta_archivo1)

#data1
print("\n")
print("\n")
print("\n")
print(df.head())
print("\n")
print("\n")
print("\n")
print(df.describe()) 
print("\n")
print("\n")
print("\n")

#data2
print("\n")
print("\n")
print("\n")
print(df1.head())
print("\n")
print("\n")
print("\n")
print(df1.describe()) 
print("\n")
print("\n")
print("\n")


fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle('Comparación del tiempo con los componentes del campo magnético (sesion1)', fontsize=16)

axs[0, 0].plot(df['Time (s)'], df['Magnetic Field x (µT)'], color='blue', label='Campo Magnético X')
axs[0, 0].set_xlabel('Tiempo (s)')
axs[0, 0].set_ylabel('Campo Magnético X (µT)')
axs[0, 0].set_title('Tiempo vs Campo Magnético X')
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].plot(df['Time (s)'], df['Magnetic Field y (µT)'], color='green', label='Campo Magnético Y')
axs[0, 1].set_xlabel('Tiempo (s)')
axs[0, 1].set_ylabel('Campo Magnético Y (µT)')
axs[0, 1].set_title('Tiempo vs Campo Magnético Y')
axs[0, 1].legend()
axs[0, 1].grid(True)

axs[1, 0].plot(df['Time (s)'], df['Magnetic Field z (µT)'], color='red', label='Campo Magnético Z')
axs[1, 0].set_xlabel('Tiempo (s)')
axs[1, 0].set_ylabel('Campo Magnético Z (µT)')
axs[1, 0].set_title('Tiempo vs Campo Magnético Z')
axs[1, 0].legend()
axs[1, 0].grid(True)

axs[1, 1].plot(df['Time (s)'], df['Absolute field (µT)'], color='purple', label='Campo Magnético Absoluto')
axs[1, 1].set_xlabel('Tiempo (s)')
axs[1, 1].set_ylabel('Campo Magnético Absoluto (µT)')
axs[1, 1].set_title('Tiempo vs Campo Magnético Absoluto')
axs[1, 1].legend()
axs[1, 1].grid(True)



fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle('Comparación del tiempo con los componentes del campo magnético (sesion2)', fontsize=16)

axs[0, 0].plot(df1['Time (s)'], df1['Magnetic Field x (µT)'], color='blue', label='Campo Magnético X')
axs[0, 0].set_xlabel('Tiempo (s)')
axs[0, 0].set_ylabel('Campo Magnético X (µT)')
axs[0, 0].set_title('Tiempo vs Campo Magnético X')
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].plot(df1['Time (s)'], df1['Magnetic Field y (µT)'], color='green', label='Campo Magnético Y')
axs[0, 1].set_xlabel('Tiempo (s)')
axs[0, 1].set_ylabel('Campo Magnético Y (µT)')
axs[0, 1].set_title('Tiempo vs Campo Magnético Y')
axs[0, 1].legend()
axs[0, 1].grid(True)

axs[1, 0].plot(df1['Time (s)'], df1['Magnetic Field z (µT)'], color='red', label='Campo Magnético Z')
axs[1, 0].set_xlabel('Tiempo (s)')
axs[1, 0].set_ylabel('Campo Magnético Z (µT)')
axs[1, 0].set_title('Tiempo vs Campo Magnético Z')
axs[1, 0].legend()
axs[1, 0].grid(True)

axs[1, 1].plot(df1['Time (s)'], df1['Absolute field (µT)'], color='purple', label='Campo Magnético Absoluto')
axs[1, 1].set_xlabel('Tiempo (s)')
axs[1, 1].set_ylabel('Campo Magnético Absoluto (µT)')
axs[1, 1].set_title('Tiempo vs Campo Magnético Absoluto')
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout()

plt.show()


plt.figure(figsize=(14, 10))
plt.suptitle('Comparación del tiempo con los componentes del campo magnético (sesion1)', fontsize=16)

plt.plot(df['Time (s)'], df['Magnetic Field x (µT)'], color='blue', label='Campo Magnético X')
plt.plot(df['Time (s)'], df['Magnetic Field y (µT)'], color='green', label='Campo Magnético Y')
plt.plot(df['Time (s)'], df['Magnetic Field z (µT)'], color='red', label='Campo Magnético Z')
plt.plot(df['Time (s)'], df['Absolute field (µT)'], color='purple', label='Campo Magnético Absoluto')

plt.xlabel('Tiempo (s)')
plt.ylabel('Campo Magnético (µT)')
plt.title('Tiempo vs Componentes del Campo Magnético')
plt.legend()
plt.grid(True)


plt.figure(figsize=(14, 10))
plt.suptitle('Comparación del tiempo con los componentes del campo magnético (sesion2)', fontsize=16)

plt.plot(df1['Time (s)'], df1['Magnetic Field x (µT)'], color='blue', label='Campo Magnético X')
plt.plot(df1['Time (s)'], df1['Magnetic Field y (µT)'], color='green', label='Campo Magnético Y')
plt.plot(df1['Time (s)'], df1['Magnetic Field z (µT)'], color='red', label='Campo Magnético Z')
plt.plot(df1['Time (s)'], df1['Absolute field (µT)'], color='purple', label='Campo Magnético Absoluto')

plt.xlabel('Tiempo (s)')
plt.ylabel('Campo Magnético (µT)')
plt.title('Tiempo vs Componentes del Campo Magnético')
plt.legend()
plt.grid(True)

plt.show()
