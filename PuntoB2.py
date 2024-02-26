# Importar función random
from random import *
print("Mostrar números aleatorios en un rango determinado por el usuario")

print('\n Ingrese los números que quiera ver en el rango \n')

# Definición del rango, ingresado por el usuario
Inicio = int(input(" desde: "))

Fin = int(input("hasta...: "))

# aplicación de randint para generar los números aleatorios según rango
aleatorio = [randint(Inicio, Fin) for i in range (1, Fin)]

print(aleatorio)
