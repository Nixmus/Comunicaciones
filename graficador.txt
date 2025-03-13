import numpy as np
import matplotlib.pyplot as plt

# Definir la ruta del archivo
file_path = r"C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\conjuntos de datos\datos.txt"
file_path1 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\conjuntos de datos\datos1.txt'
file_path2 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\conjuntos de datos\datos2.txt'
file_path3 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\conjuntos de datos\datos3.txt'
file_path4 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\conjuntos de datos\datos4.txt'


# Cargar el archivo txt saltando la primera línea (header)
data = np.loadtxt(file_path, skiprows=1)
data1 = np.loadtxt(file_path1, skiprows=1)
data2 = np.loadtxt(file_path2, skiprows=1)
data3 = np.loadtxt(file_path3, skiprows=1)
data4 = np.loadtxt(file_path4, skiprows=1)

# Separar las columnas
x = data[:100, 0]  # Primera columna
y = data[:100, 1]  # Segunda columna

# Separar las columnas
x1 = data1[100:200, 0]  # Primera columna
y1 = data1[100:200, 1]  # Segunda columna

# Separar las columnas
x2 = data2[100:200, 0]  # Primera columna
y2 = data2[100:200, 1]  # Segunda columna

# Separar las columnas
x3 = data3[250:500, 0]  # Primera columna
y3 = data3[250:500, 1]  # Segunda columna

# Separar las columnas
x4 = data4[:, 0]  # Primera columna
y4 = data4[:, 1]  # Segunda columna


fig, axs = plt.subplots(2, 2, figsize=(16, 16))
fig.suptitle('señales laboratorio', fontsize=16)

axs[0, 0].plot(x, y, linestyle='-', color='b')
axs[0, 0].set_title('data1')
axs[0, 0].grid(True)

axs[0, 1].plot(x1, y1, linestyle='-', color='b')
axs[0, 1].set_title('data2')
axs[0, 1].grid(True)

axs[1, 0].plot(x2, y2, linestyle='-', color='b')
axs[1, 0].set_title('data3')
axs[1, 0].grid(True)

axs[1, 1].plot(x3, y3, linestyle='-', color='b')
axs[1, 1].set_title('data4')
axs[1, 1].grid(True)

plt.show()

plt.plot(x4, y4, linestyle='-', color='b')
plt.title('data5')
plt.grid(True)

plt.show()
