
import numpy as np
import matplotlib.pyplot as plt

#Declaracion de funcion
def temperatura_baja (A,B):
    return (A,B)
#Crear listas
resistencias_A= []
resistencias_B= []
temperaturasp= []
temperaturasn= []


#Operacion matematica 
for i in range (201):
 #Temperatura positiva
 ResistenciaTA=100*(1+0.003851*(i))
 #Temperatura negativa
 ResistenciaTB=100*(1+0.003851*(-i))
 #Retornar y guardar datos de resistencia en temperatura positiva y negativa
 A,B =temperatura_baja(ResistenciaTA,ResistenciaTB)
 #Llenar listas
 resistencias_A.append(A)
 resistencias_B.append(B)
 temperaturasp.append(i)
 temperaturasn.append(-i)

#Imprimir
plt.plot( temperaturasp,resistencias_A,label='Resistencia a temperatura Positiva')
plt.plot( temperaturasn,resistencias_B, label='Resistencia a temperatura Negativa')
plt.title('Comportamiento de un sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (ohm)')
plt.legend() 
plt.grid(True)
plt.show()




