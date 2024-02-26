import numpy as np

def rotacion_x(angulo):
    radianes = np.radians(angulo)
    matriz_rotacion = np.array([[1, 0, 0],
                                 [0, np.cos(radianes), -np.sin(radianes)],
                                 [0, np.sin(radianes), np.cos(radianes)]])
    return matriz_rotacion

def rotacion_y(angulo):
    radianes = np.radians(angulo)
    matriz_rotacion = np.array([[np.cos(radianes), 0, np.sin(radianes)],[0, 1, 0],
                                [-np.sin(radianes), 0, np.cos(radianes)]])
    return matriz_rotacion

def rotacion_z(angulo):
    radianes = np.radians(angulo)
    matriz_rotacion = np.array([[np.cos(radianes), -np.sin(radianes), 0],
                                 [np.sin(radianes), np.cos(radianes), 0],
                                 [0, 0, 1]])
    return matriz_rotacion

# cambiar posiciones
#angulo = 45
rotacion_x_es = rotacion_x(34)
print("Rotación en X es:")
print(rotacion_x_es )

rotacion_y_es = rotacion_y(26)
print("\nRotación en Y es:")
print(rotacion_y_es)

rotacion_z_es= rotacion_z(14)
print("\nRotación en Z es:")
print(rotacion_z_es)
