import random 
import string

def generar_linea_aleatoria(longitud=60):#Aqui se ajusta la longitud de la linea de caracteres.
    caracteres = string.ascii_letters + string.digits
    linea = ''.join(random.choice(caracteres) for _ in range(longitud))
    return linea

with open("100_lineas_60caracteres.txt", "w") as archivo: #"w" abre el archivo en modo escritura
    for _ in range(100): 
        linea = generar_linea_aleatoria() #llama la funcion
        archivo.write(linea + "\n") #crea el texto con un "\n" para que se separe por lineas
        
with open("100_lineas_60caracteres.txt", "r") as archivo:
    text = archivo.read()
    print(text)
