#Librerias
import numpy as np
import matplotlib.pyplot as plt

def filtro_pasa_baja(corte, fs, num_coeficiente):
    newf = 0.5 * fs
    normal_corte = corte / newf #normaliza la frecuencia de corte
    coeficiente = np.sinc(2 * normal_corte * (np.arange(num_coeficiente) - (num_coeficiente - 1) / 2))#crea un arreglo de ceros y lo centra en 0, ajusta el arreglo a la frecuencia normalizada
    #np.sinc calcula es la base de los filtros FIR 
    #filtros fir respuesta finita al impulso
    window = np.hamming(num_coeficiente)#ventana de hamming
    coeficiente *= window#suaviza el filtro
    coeficiente /= np.sum(coeficiente)#normaliza los coeficientes
    return coeficiente

def graficas2x2(nombre, s1, s2, s3, s4, t):
    fig, axs = plt.subplots(2, 2, figsize=(18, 18))
    fig.suptitle('Señales '+ nombre)
    
    axs[0, 0].plot(t, s1)
    axs[0, 0].set_xlabel('Tiempo')
    axs[0, 0].set_ylabel('Amplitud')
    axs[0, 0].grid(True)
    
    axs[0, 1].plot(t, s2)
    axs[0, 1].set_xlabel('Tiempo')
    axs[0, 1].set_ylabel('Amplitud')
    axs[0, 1].grid(True)
    
    axs[1, 0].plot(t, s3)
    axs[1, 0].set_xlabel('Tiempo')
    axs[1, 0].set_ylabel('Amplitud')
    axs[1, 0].grid(True)
    
    axs[1, 1].plot(t, s4)
    axs[1, 1].set_xlabel('Tiempo')
    axs[1, 1].set_ylabel('Amplitud')
    axs[1, 1].grid(True)
    
    plt.show()

def graficas3x1(nombre, s1, s2, s3, s4, t):
    fig, axs = plt.subplots(3, 1,  figsize=(14, 14))
    fig.suptitle('Señales '+ nombre)
    
    axs[0].plot(t, s1)
    axs[0].plot(t, s2)
    axs[0].set_xlabel('Tiempo')
    axs[0].set_ylabel('Amplitud')
    axs[0].grid(True)
    
    axs[1].plot(t, s1)
    axs[1].plot(t, s3)
    axs[1].set_xlabel('Tiempo')
    axs[1].set_ylabel('Amplitud')
    axs[1].grid(True)
    
    axs[2].plot(t, s1)
    axs[2].plot(t, s4)
    axs[2].set_xlabel('Tiempo')
    axs[2].set_ylabel('Amplitud')
    axs[2].grid(True)
    
    plt.show()

def graficas2x1(nombre, s1, s2, t):
    fig, axs = plt.subplots(2, 1,  figsize=(14, 14))
    fig.suptitle('Señales '+ nombre)
    
    axs[0].plot(t, s1)
    axs[0].set_xlabel('Tiempo')
    axs[0].set_ylabel('Amplitud')
    axs[0].grid(True)
    
    axs[1].plot(t, s2)
    axs[1].set_xlabel('Tiempo')
    axs[1].set_ylabel('Amplitud')
    axs[1].grid(True)
    
    plt.show()

# Parámetros
fs = 10000000
t = np.arange(0, 0.0003, 1/fs)

# Señales
m = np.cos(1 * np.pi * 10000* t) 
m1 = np.cos(3 * np.pi * 30000* t) 
m2 = np.cos(5 * np.pi * 50000* t)  
mt = m + m1 + m2

nombre= "originales"

s1= m
s2= m1 
s3= m2
s4= mt

graficas2x2(nombre, s1, s2, s3, s4, t)

# Aplicar el filtro
corte = 14000  # Frecuencia de corte
num_coeficiente = 151  # Número de coeficientes del filtro
coeficiente = filtro_pasa_baja(corte, fs, num_coeficiente)
mt_filtrada = np.convolve(mt, coeficiente, mode='same')
num_coeficiente = 501  # Número de coeficientes del filtro
coeficiente = filtro_pasa_baja(corte, fs, num_coeficiente)
mt_filtrada2 = np.convolve(mt, coeficiente, mode='same')
num_coeficiente = 71  # Número de coeficientes del filtro
coeficiente = filtro_pasa_baja(corte, fs, num_coeficiente)
mt_filtrada3 = np.convolve(mt, coeficiente, mode='same')

s1= mt
s2= mt_filtrada
s3= mt_filtrada2
s4= mt_filtrada3

nombre= "filtradas"

graficas3x1(nombre, s1, s2, s3, s4, t)
