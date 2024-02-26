import numpy as np

# (temperatura, resistencia)
punto1 = (60, 10) 
punto2 = (50, 25)  

temperaturas = np.array([punto1[0], punto2[0]])
resistencias = np.array([punto1[1], punto2[1]])

# Ajustar un polinomio de grado 1 (línea recta)
coeficientes = np.polyfit(temperaturas, resistencias, 1)#formula t=mx+b (para ajustar el polinomioa un conjunto de datos mediante el metodo de minimos cuadrados 

print("las resistencias son:", resistencias)
print("las temperaturas son:", temperaturas)
print("Coeficientes de la línea recta:", coeficientes)

# Función para calcular la resistencia a una temperatura dada
def calcular_resistencia_pt100(temperatura):
    return np.polyval(coeficientes, temperatura) # funcion para evaluar un polinomio en un punto dado 

print("calculo PT100 es:", calcular_resistencia_pt100(30))

