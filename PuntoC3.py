import math
import matplotlib.pyplot as plt
import numpy as np

# Solicitud de datos del usuario por teclado
v = float(input ("\n Ingrese el valor de voltaje de entrada: "))
c = float(input(" \n Ingrese el valor del capacitor: "))
r = float(input("\n Ingrese el valor de la resistencia: "))

# Función de la ecuación para los valores ingresados por el usuario para la carga
def carga(v, c, r, t):
    return v * (1 - np.exp(-t / (r * c)))

# Función de la ecuación para los valores ingresados por el usuario para la descarga    
def descarga(v, c, r, t):
    return v * np.exp(-t / (r * c))

# Definición del tiempo de la simulación
t = np.linspace(0, 10, 1000)

# cálculo de la carga y la descarga
circuito_carga = carga(v, c, r, t)
circuito_descarga = descarga(v, c, r, t)

# Generar gráfica
plt.title('Carga y descarga de un circuito RC')
plt.plot(t, circuito_carga, label='Carga del circuito')
plt.plot(t, circuito_descarga, label='Descarga del circuito')
plt.legend()
plt.xlabel('Tiempo(S)')
plt.ylabel('Carga y Descarga (V)')
plt.grid(True)
plt.show()
