import numpy as np
import matplotlib.pyplot as plt

# Definir la ruta del archivo
file_path = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\histogramas\hstgrm.txt'
file_path1 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\histogramas\hstgrm1.txt'
file_path2 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\histogramas\hstgrm2.txt'
file_path3 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\histogramas\hstgrm3.txt'
file_path4 = r'C:\Users\rafad\OneDrive\Documents\codigos\Codigos Python\comunicaciones digita\laboratorio_adc\histogramas\hstgrm4.txt'


# Cargar el archivo txt saltando la primera línea (header)
data = np.loadtxt(file_path, skiprows=1)
data1 = np.loadtxt(file_path1, skiprows=1)
data2 = np.loadtxt(file_path2, skiprows=1)
data3 = np.loadtxt(file_path3, skiprows=1)
data4 = np.loadtxt(file_path4, skiprows=1)

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

# Crear figura para los histogramas
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Histogramas de las señales', fontsize=16)

# Histograma 1
mu1 = np.mean(y)
sigma1 = np.std(y)
axs[0, 0].hist(y, bins=50, density=True, alpha=0.7, color='blue', rwidth=0.95)
axs[0, 0].set_title(f'Histograma 1\nμ={mu1:.3f}, σ={sigma1:.3f}')
axs[0, 0].grid(True)

# Histograma 2
mu2 = np.mean(y1)
sigma2 = np.std(y1)
axs[0, 1].hist(y1, bins=50, density=True, alpha=0.7, color='green', rwidth=0.95)
axs[0, 1].set_title(f'Histograma 2\nμ={mu2:.3f}, σ={sigma2:.3f}')
axs[0, 1].grid(True)

# Histograma 3
mu3 = np.mean(y2)
sigma3 = np.std(y2)
axs[0, 2].hist(y2, bins=50, density=True, alpha=0.7, color='red', rwidth=0.95)
axs[0, 2].set_title(f'Histograma 3\nμ={mu3:.3f}, σ={sigma3:.3f}')
axs[0, 2].grid(True)

# Histograma 4
mu4 = np.mean(y3)
sigma4 = np.std(y3)
axs[1, 0].hist(y3, bins=50, density=True, alpha=0.7, color='purple', rwidth=0.95)
axs[1, 0].set_title(f'Histograma 4\nμ={mu4:.3f}, σ={sigma4:.3f}')
axs[1, 0].grid(True)

# Histograma 5
mu5 = np.mean(y4)
sigma5 = np.std(y4)
axs[1, 1].hist(y4, bins=50, density=True, alpha=0.7, color='orange', rwidth=0.95)
axs[1, 1].set_title(f'Histograma 5\nμ={mu5:.3f}, σ={sigma5:.3f}')
axs[1, 1].grid(True)

# Ajustar el espaciado
plt.tight_layout()

# Mostrar la figura
plt.show()

# Imprimir estadísticas
print("\nEstadísticas de las señales:")
print(f"Señal 1: Media = {mu1:.3f}V, Desviación estándar = {sigma1:.3f}V")
print(f"Señal 2: Media = {mu2:.3f}V, Desviación estándar = {sigma2:.3f}V")
print(f"Señal 3: Media = {mu3:.3f}V, Desviación estándar = {sigma3:.3f}V")
print(f"Señal 4: Media = {mu4:.3f}V, Desviación estándar = {sigma4:.3f}V")
print(f"Señal 5: Media = {mu5:.3f}V, Desviación estándar = {sigma5:.3f}V")
