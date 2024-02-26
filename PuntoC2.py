import matplotlib.pyplot as plt
import numpy as np 
from math import sqrt #De la libreria math importamos la funcion raiz cuadrada
from scipy import signal #De la libreria scipy importamos la funcion signal

#Creacion de la funcion, para resolver funcion cuadratica
def resolver_cuadratica(a,b,c):
    determinate = b**2 - 4*a*c

#Obtenemos el valor de las raices dependiendo el valor del determinante
    if determinate > 0:
      Raizuno = - b + sqrt(b**2-4*a*c) / (2*a)
      Raizdos = - b - sqrt(b**2-4*a*c) / (2*a)

      return Raizuno, Raizdos
    elif determinate == 0:
        Raizuno = - b / (2*a)
        return Raizuno,Raizuno
 #Al ser el determinates -1 obtendremos raices con parte imaginaria   
    else:
       Parte_real= -b/(2*a)
 #Obtenemos el valor absoluto de una raiz cuadrada
       Parte_imaginaria = sqrt(abs(determinate))/(2*a)
 #Se almasena el valor complejo con parte imaginaria en las raices      
       Raizuno= complex(Parte_real,Parte_imaginaria)
       Raizdos= complex(Parte_real, -Parte_imaginaria)
       
       return (Raizuno, Raizdos) 
    
# Determinamos el tipo del sistema 
def Tipo_de_sistema(a,b,c):
   Raizuno,Raizdos= resolver_cuadratica(a,b,c)
   Dato = -b/ (2* sqrt(a*c))
   
   if abs(Dato < 1) <1e-6:
      return 'Subamortiguado'
   elif Dato <1:
      return 'Criticamente Amortiguado'
   else: 
        return 'Sobreamortiguado'
    
a= float(input('Ingrese el coeficiente a: '))
b= float(input('Ingrese el coeficiente b: '))
c= float(input('Ingrese el coeficiente c: '))

#Imprimimos el tipo de sistema
Sistema = Tipo_de_sistema( a,b,c)
print('El sistema es:' ,Sistema)


t= np.linspace (0,20,1000)
#Coeficientes en lista.
num= [1]
den=[a,b,c]
#Respuesta en el dominio del tiempo
tout, yout = signal.step ((num,den), T=t)
#Imprimir
plt.plot (tout, yout)
plt.title('Respuesta en dominio del tiempo')
plt.xlabel('Tiempo')
plt.ylabel ('Respuesta')
plt.grid()
plt.show()

  
