

import numpy as np
import matplotlib.pyplot as plt

#Amplitud

Lx=[1,1,2,2]
Ex=[2.5,2.5]
Ex1=[2.5,3.5]
Ex2=[4,4]
Ex3=[4.5,4.5,5,5,5.5,5.5]
Ex5=[6,6]
Ex6=[6,7]
Ex7=[7,5]
#Latitud
Ly=[6,1,1,1]
Ey=[6,1]
Ey1=[1,1]
Ey2=[3,3]
Ey3=[6,6]
Ey4=[6,6,1,1,6,6]
Rx=[7.5,7.5,8,7.5,8]
Ry=[1,6,5,4,1]
Jx=[1,3,2,2,1]
Jy=[-1,-1,-1,-6,-6]
Ux=[3.5,3.5,4,4]
Uy=[-1,-6,-6,-1]
Lx=[4.5,4.5,5]
Ly=[-1,-6,-6]
Ix=[5.5,5.5]
Iy=[-1,-6]
Ax=[6.5,7,7.5]
Ay=[-6,-1,-6]
A1x=[6.7,7.3]
A1y=[-4,-4]
Nx=[8,8,8.5,8.5]
Ny=[-6,-1,-6,-1]




plt.plot( Lx,Ly,Ex,Ey,Ex1,Ey1,Ex1,Ey2,Ex1,Ey3,Ex2,Ey,Ex3,Ey4,Ex5,Ey,Ex6,Ey1,Ex6,Ey2,Ex6,Ey3,Rx,Ry)
plt.plot(Jx,Jy,Ux,Uy,Lx,Ly,Ix,Iy,Ax,Ay,A1x,A1y,Nx,Ny)


plt.legend() 
plt.grid(True)
plt.show()

