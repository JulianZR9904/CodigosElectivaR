from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import numpy as np 

X0 = np.array([1, 5, 6])
X1 = np.array([4, 0, 4], dtype=float)
X2 = np.array([4, 4, 0], dtype=float)

errado = X2-X1
distancia = np.sqrt(np.sum(errado**2))

print(errado)
print(distancia)

figura =plt.figure()
grafica = figura.add_subplot(111,projection='3d')

[x,y,z] = X0
grafica.scatter(x,y,z, c='blue', marker = 'o', label ='X0')
[x,y,z] = X1
grafica.scatter(x,y,z, c='red', marker = 'o', label ='X0')
[x,y,z] = X2
grafica.scatter(x,y,z, c='green', marker = 'o', label ='X0')

linea = np.concatenate(([X0],[X1]), axis=0)
x= linea[:,0]
y= linea[:,1]
z= linea[:,2]
grafica.plot(x,y,z, label='||X1||')

#linea = np.concatenate(([X0],[X2]), axis=0)
#x= linea[:,0]
#y= linea[:,1]
#z= linea[:,2]
#grafica.plot(x,y,z, label='||X2||')

#linea = np.concatenate(([X1],[X2]), axis=0)
#x= linea[:,0]
#y= linea[:,1]
#z= linea[:,2]
#grafica.plot(x,y,z, label='||X||')

grafica.set_xlabel ('eje x')
grafica.set_ylabel ('eje y')
grafica.set_zlabel ('eje z')
grafica.legend()

grafica.view_init(35,25)

plt.show()
