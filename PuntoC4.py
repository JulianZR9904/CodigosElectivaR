from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import numpy as np 

# Solicitar al usuario que ingrese los valores para X0
x0_input = input("Ingrese las coordenadas para X0 separadas por comas: ")
X0 = np.array([float(x) for x in x0_input.split(',')])

# Solicitar al usuario que ingrese los valores para X1
x1_input = input("Ingrese las coordenadas para X1 separadas por comas: ")
X1 = np.array([float(x) for x in x1_input.split(',')], dtype=float)

# Solicitar al usuario que ingrese los valores para X2
x2_input = input("Ingrese las coordenadas para X2 separadas por comas: ")
X2 = np.array([float(x) for x in x2_input.split(',')], dtype=float)

vfinal= X2 - X1


print("Vector final", vfinal)

#Creacion de figura en matplotlib
figura = plt.figure()
#Usamos 111 para que solo nos salga una figura con tamaño 1x1
grafica = figura.add_subplot(111, projection='3d')

#Guardamos las coordenadas del usuario para podder imprimir 
[x, y, z] = X0
#Dibujar El punto en el espacio
grafica.scatter(x, y, z, c='blue', marker='o', label='X0')
[x, y, z] = X1
grafica.scatter(x, y, z, c='red', marker='o', label='X1')
[x, y, z] = X2
grafica.scatter(x, y, z, c='green', marker='o', label='X2')
#Union de puntos X0 Y X1
linea = np.concatenate(([X0], [X1]), axis=0)
#Coordenadas de la matriz linea
x = linea[:, 0]
y = linea[:, 1]
z = linea[:, 2]
#Conectamos los puntos en un subplot 
grafica.plot(x, y, z, label='||X1||')
#Etiquetas
grafica.set_xlabel('eje x')
grafica.set_ylabel('eje y')
grafica.set_zlabel('eje z')
grafica.legend()

grafica.view_init(35, 25)

plt.show()