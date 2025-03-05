#Bibliotecas y extensiones
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#data1
ruta_archivo= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/informe 2/Senosoidal1.csv"
df = pd.read_csv(ruta_archivo, encoding='latin1' , skiprows=17)
#data2
ruta_archivo1= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/informe 2/senosoidal2.csv"
df1 = pd.read_csv(ruta_archivo1, encoding='latin1', skiprows=17)
#data3
ruta_archivo3= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/informe 2/triangular1.csv"
df3 = pd.read_csv(ruta_archivo3, encoding='latin1', skiprows=17)
#data4
ruta_archivo4= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/informe 2/triangular2.csv"
df4 = pd.read_csv(ruta_archivo4, encoding='latin1', skiprows=17)
#data5
ruta_archivo5= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/informe 2/rectangular1.csv"
df5 = pd.read_csv(ruta_archivo5, encoding='latin1', skiprows=17)
#data6
ruta_archivo6= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/informe 2/rectangular2.csv"
df6 = pd.read_csv(ruta_archivo6, encoding='latin1', skiprows=17)
#data7
ruta_archivo7= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/informe 2/rectangular3.csv"
df7 = pd.read_csv(ruta_archivo7, encoding='latin1', skiprows=17)
#data8
ruta_archivo8= "C:/Users/rafad/OneDrive/Documents/codigos/Codigos Python/comunicaciones digita/informe 2/rectangular4.csv"
df8 = pd.read_csv(ruta_archivo8, encoding='latin1', skiprows=17)

#nuevo data 1
df = df.iloc[:, [3, 4]]
df.columns = ['x', 'y']

#nuevo data 2
df1 = df1.iloc[:, [3, 4]]
df1.columns = ['x', 'y']

#nuevo data 3
df3 = df3.iloc[:, [3, 4]]
df3.columns = ['x', 'y']

#nuevo data 4
df4 = df4.iloc[:, [3, 4]]
df4.columns = ['x', 'y']

#nuevo data 5
df5 = df5.iloc[:, [3, 4]]
df5.columns = ['x', 'y']

#nuevo data 6
df6 = df6.iloc[:, [3, 4]]
df6.columns = ['x', 'y']

#nuevo data 7
df7 = df7.iloc[:, [3, 4]]
df7.columns = ['x', 'y']

#nuevo data 8
df8 = df8.iloc[:, [3, 4]]
df8.columns = ['x', 'y']



#extraccion de data 1
x = df['x'].values
y = df['y'].values

#extraccion de data 2
x1 = df1['x'].values
y1 = df1['y'].values

#extraccion de data 3
x3 = df3['x'].values
y3 = df3['y'].values

#extraccion de data 4
x4 = df4['x'].values
y4 = df4['y'].values

#extraccion de data 5
x5 = df5['x'].values
y5 = df5['y'].values

#extraccion de data 6
x6 = df6['x'].values
y6 = df6['y'].values

#extraccion de data 7
x7 = df7['x'].values
y7 = df7['y'].values

#extraccion de data 8
x8 = df8['x'].values
y8 = df8['y'].values



#data1
print("\n")
print("Data 1")
print(df.head())
print("\n")
#print("\n")
#print(df.describe()) 
#print("\n")

#data2
print("\n")
print("Data 2")
print(df1.head())
print("\n")
#print("\n")
#print(df1.describe()) 
#print("\n")

#data3
print("\n")
print("Data 3")
print(df3.head())
print("\n")
#print("\n")
#print(df3.describe()) 
#print("\n")

#data4
print("\n")
print("Data 4")
print(df4.head())
print("\n")
#print("\n")
#print(df4.describe()) 
#print("\n")

#data5
print("\n")
print("Data 5")
print(df5.head())
print("\n")
#print("\n")
#print(df5.describe()) 
#print("\n")

#data6
print("\n")
print("Data 6")
print(df6.head())
print("\n")
#print("\n")
#print(df6.describe()) 
#print("\n")

#data7
print("\n")
print("Data 7")
print(df7.head())
print("\n")
#print("\n")
#print(df7.describe()) 
#print("\n")

#data8
print("\n")
print("Data 8")
print(df8.head())
print("\n")
#print("\n")
#print(df8.describe()) 
#print("\n")


fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle('señales laboratorio', fontsize=16)

axs[0, 0].plot(df['x'], df['y'], color='blue')
axs[0, 0].set_title('senosoidal1')
axs[0, 0].grid(True)

axs[0, 1].plot(df1['x'], df1['y'], color='green')
axs[0, 1].set_title('senosoidal2')
axs[0, 1].grid(True)

axs[1, 0].plot(df3['x'], df3['y'], color='red')
axs[1, 0].set_title('Triangular1')
axs[1, 0].grid(True)

axs[1, 1].plot(df4['x'], df4['y'], color='purple')
axs[1, 1].set_title('Triangular2')
axs[1, 1].grid(True)

fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle('señales rectangulares laboratorio', fontsize=16)

axs[0, 0].plot(df5['x'], df5['y'], color='blue')
axs[0, 0].set_title('rectangular1')
axs[0, 0].grid(True)

axs[0, 1].plot(df6['x'], df6['y'], color='green')
axs[0, 1].set_title('rectangular2')
axs[0, 1].grid(True)

axs[1, 0].plot(df7['x'], df7['y'], color='red')
axs[1, 0].set_title('rectangular3')
axs[1, 0].grid(True)

axs[1, 1].plot(df8['x'], df8['y'], color='purple')
axs[1, 1].set_title('rectangular4')
axs[1, 1].grid(True)

plt.tight_layout()

plt.show()


#dominios de la frecuencia 1
fft_resultado = np.fft.fft(y)
n = len(y)
dt = x[1] - x[0]
d=dt
frecuencias = np.fft.fftfreq(n, d)
magnitud = np.abs(fft_resultado)

#dominios de la frecuencia 2
fft_resultado1 = np.fft.fft(y1)
n1 = len(y1)
dt1 = x1[1] - x1[0]
d1=dt1
frecuencias1 = np.fft.fftfreq(n1, d1)
magnitud1 = np.abs(fft_resultado1)

#dominios de la frecuencia 3
fft_resultado3 = np.fft.fft(y3)
n3 = len(y3)
dt3 = x3[1] - x3[0]
d3=dt3
frecuencias3 = np.fft.fftfreq(n3, d3)
magnitud3 = np.abs(fft_resultado3)

#dominios de la frecuencia 4
fft_resultado4 = np.fft.fft(y4)
n4 = len(y4)
dt4 = x4[1] - x4[0]
d4=dt4
frecuencias4 = np.fft.fftfreq(n4, d4)
magnitud4 = np.abs(fft_resultado4)

#dominios de la frecuencia 5
fft_resultado5 = np.fft.fft(y5)
n5 = len(y5)
dt5 = x5[1] - x5[0]
d5=dt5
frecuencias5 = np.fft.fftfreq(n5, d5)
magnitud5 = np.abs(fft_resultado5)

#dominios de la frecuencia 6
fft_resultado6 = np.fft.fft(y6)
n6 = len(y6)
dt6 = x6[1] - x6[0]
d6=dt6
frecuencias6 = np.fft.fftfreq(n6, d6)
magnitud6 = np.abs(fft_resultado6)

#dominios de la frecuencia 7
fft_resultado7 = np.fft.fft(y7)
n7 = len(y7)
dt7 = x7[1] - x7[0]
d7=dt7
frecuencias7 = np.fft.fftfreq(n7, d7)
magnitud7 = np.abs(fft_resultado7)

#dominios de la frecuencia 8
fft_resultado8 = np.fft.fft(y8)
n8 = len(y8)
dt8 = x8[1] - x8[0]
d8=dt8
frecuencias8 = np.fft.fftfreq(n8, d8)
magnitud8 = np.abs(fft_resultado8)



fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle('señales laboratorio en el dominio de la frecuencia', fontsize=16)

axs[0, 0].plot(frecuencias[:n // 1], magnitud[:n // 1], color='blue')
axs[0, 0].set_title('senosoidal1 frecuencia')
axs[0, 0].grid(True)

axs[0, 1].plot(frecuencias1[:n // 1], magnitud1[:n // 1], color='green')
axs[0, 1].set_title('senosoidal2 frecuencia')
axs[0, 1].grid(True)

axs[1, 0].plot(frecuencias3[:n // 1], magnitud3[:n // 1], color='red')
axs[1, 0].set_title('triangular1 frecuencia')
axs[1, 0].grid(True)

axs[1, 1].plot(frecuencias4[:n // 1], magnitud4[:n // 1], color='purple')
axs[1, 1].set_title('triangular2 frecuencia')
axs[1, 1].grid(True)



fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle('señales rectangulares en el dominio de la frecuencia', fontsize=16)

axs[0, 0].plot(frecuencias5[:n // 1], magnitud5[:n // 1], color='blue')
axs[0, 0].set_title('rectangular1 frecuencia')
axs[0, 0].grid(True)

axs[0, 1].plot(frecuencias6[:n // 1], magnitud6[:n // 1], color='green')
axs[0, 1].set_title('rectangular2 frecuencia')
axs[0, 1].grid(True)

axs[1, 0].plot(frecuencias7[:n // 1], magnitud7[:n // 1], color='red')
axs[1, 0].set_title('rectangular3 frecuencia')
axs[1, 0].grid(True)

axs[1, 1].plot(frecuencias8[:n // 1], magnitud8[:n // 1], color='purple')
axs[1, 1].set_title('rectangular4 frecuencia')
axs[1, 1].grid(True)

plt.tight_layout()

plt.show()
