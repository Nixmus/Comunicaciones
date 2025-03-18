import numpy as np
import matplotlib.pyplot as plt

# Definir la ruta del archivo
file_path = r"C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft.txt"
file_pathrubik = r"C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft62.txt"
file_pathrubik2 = r"C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft65.txt"

file_path1 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft3.txt'
file_path2 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft6.txt'
file_path3 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft12.txt'
file_path4 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft15.txt'

file_path5 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft22.txt'
file_path6 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft25.txt'
file_path7 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft32.txt'
file_path8 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft35.txt'

file_path9 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft42.txt'
file_path10 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft45.txt'
file_path11 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft52.txt'
file_path12 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio muestras fft\fft55.txt'

# Cargar el archivo txt saltando la primera línea (header)
data = np.loadtxt(file_path, skiprows=1)
data_rubik = np.loadtxt(file_pathrubik, skiprows=1)
data_rubik2 = np.loadtxt(file_pathrubik2, skiprows=1)

data1 = np.loadtxt(file_path1, skiprows=1)
data2 = np.loadtxt(file_path2, skiprows=1)
data3 = np.loadtxt(file_path3, skiprows=1)
data4 = np.loadtxt(file_path4, skiprows=1)
data5 = np.loadtxt(file_path5, skiprows=1)
data6 = np.loadtxt(file_path6, skiprows=1)
data7 = np.loadtxt(file_path7, skiprows=1)
data8 = np.loadtxt(file_path8, skiprows=1)
data9 = np.loadtxt(file_path9, skiprows=1)
data10 = np.loadtxt(file_path10, skiprows=1)
data11 = np.loadtxt(file_path11, skiprows=1)
data12 = np.loadtxt(file_path12, skiprows=1)


# Separar las columnas
x = data[:, 0]  # Primera columna
y = data[:, 1]  # Segunda columna

# Separar las columnas
x1 = data1[:, 0]  # Primera columna
y1 = data1[:, 1]  # Segunda columna

# Separar las columnas
x2 = data2[:, 0]  # Primera columna
y2 = data2[:, 1]  # Segunda columna

# Separar las columnas
x3 = data3[:, 0]  # Primera columna
y3 = data3[:, 1]  # Segunda columna

# Separar las columnas
x4 = data4[:, 0]  # Primera columna
y4 = data4[:, 1]  # Segunda columna

# Separar las columnas
x5 = data5[:, 0]  # Primera columna
y5 = data5[:, 1]  # Segunda columna

# Separar las columnas
x6 = data6[:, 0]  # Primera columna
y6 = data6[:, 1]  # Segunda columna

# Separar las columnas
x7 = data7[:, 0]  # Primera columna   
y7 = data7[:, 1]  # Segunda columna

# Separar las columnas
x8 = data8[:, 0]  # Primera columna
y8 = data8[:, 1]  # Segunda columna

# Separar las columnas
x9 = data9[:, 0]  # Primera columna
y9 = data9[:, 1]  # Segunda columna

# Separar las columnas
x10 = data10[:, 0]  # Primera columna
y10 = data10[:, 1]  # Segunda columna

# Separar las columnas
x11 = data11[:, 0]  # Primera columna
y11 = data11[:, 1]  # Segunda columna

# Separar las columnas
x12 = data12[:, 0]  # Primera columna
y12 = data12[:, 1]  # Segunda columna


fig, axs = plt.subplots(2, 2, figsize=(16, 16))
fig.suptitle('Señales laboratorio', fontsize=16)

stem_params = {
    'linefmt': 'b-',     
    'markerfmt': 'bo',    
    'basefmt': 'r-'       
}

markerline1, stemlines1, baseline1 = axs[0, 0].stem(x1, y1, **stem_params)
axs[0, 0].set_title('Data 1')
axs[0, 0].grid(True, linestyle='--', alpha=0.7)

markerline2, stemlines2, baseline2 = axs[0, 1].stem(x2, y2, **stem_params)
axs[0, 1].set_title('Data 2')
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

markerline3, stemlines3, baseline3 = axs[1, 0].stem(x3, y3, **stem_params)
axs[1, 0].set_title('Data 3')
axs[1, 0].grid(True, linestyle='--', alpha=0.7)

markerline4, stemlines4, baseline4 = axs[1, 1].stem(x4, y4, **stem_params)
axs[1, 1].set_title('Data 4')
axs[1, 1].grid(True, linestyle='--', alpha=0.7)


fig, axs = plt.subplots(2, 2, figsize=(16, 16))
fig.suptitle('Señales laboratorio', fontsize=16)

stem_params = {
    'linefmt': 'b-',     
    'markerfmt': 'bo',    
    'basefmt': 'r-'       
}

markerline5, stemlines5, baseline5 = axs[0, 0].stem(x5, y5, **stem_params)
axs[0, 0].set_title('Data 5')
axs[0, 0].grid(True, linestyle='--', alpha=0.7)

markerline6, stemlines6, baseline6 = axs[0, 1].stem(x6, y6, **stem_params)
axs[0, 1].set_title('Data 6')
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

markerline7, stemlines7, baseline7 = axs[1, 0].stem(x7, y7, **stem_params)
axs[1, 0].set_title('Data 7')
axs[1, 0].grid(True, linestyle='--', alpha=0.7)

markerline8, stemlines8, baseline8 = axs[1, 1].stem(x8, y8, **stem_params)
axs[1, 1].set_title('Data 8')
axs[1, 1].grid(True, linestyle='--', alpha=0.7)



fig, axs = plt.subplots(2, 2, figsize=(16, 16))
fig.suptitle('Señales laboratorio', fontsize=16)

stem_params = {
    'linefmt': 'b-',     
    'markerfmt': 'bo',    
    'basefmt': 'r-'       
}

markerline9, stemlines9, baseline9 = axs[0, 0].stem(x9, y9, **stem_params)
axs[0, 0].set_title('Data 9')
axs[0, 0].grid(True, linestyle='--', alpha=0.7)

markerline10, stemlines10, baseline10 = axs[0, 1].stem(x10, y10, **stem_params)
axs[0, 1].set_title('Data 10')
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

markerline11, stemlines11, baseline11 = axs[1, 0].stem(x11, y11, **stem_params)
axs[1, 0].set_title('Data 11')
axs[1, 0].grid(True, linestyle='--', alpha=0.7)

markerline12, stemlines12, baseline12 = axs[1, 1].stem(x12, y12, **stem_params)
axs[1, 1].set_title('Data 12')
axs[1, 1].grid(True, linestyle='--', alpha=0.7)

# Ajustar el tamaño de los marcadores
for markerline in [markerline1, markerline2, markerline3, markerline4, markerline5, markerline6, markerline7, markerline8, markerline9, markerline10, markerline11, markerline12]:
    plt.setp(markerline, markersize=4)

# Añadir etiquetas a todos los gráficos
for ax in axs.flat:  # Usar .flat para iterar sobre todos los subplots de manera segura
    ax.set_xlabel('Tiempo (ms)')
    ax.set_ylabel('Voltaje (V)')

# Ajustar el espaciado
plt.tight_layout()

plt.show()
