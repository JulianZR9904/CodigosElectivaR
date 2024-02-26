import numpy as np
import matplotlib.pyplot as plt
#Amplitud
wx=[1,1.4,1.8,2.2,2.6]
#w2x=[2.6,2.2]
#WILMAR
ix=[2.8,2.8]
lx=[3,3,3.5,3.5]
mx=[3.7,4,4.4,4.8,5.2]
ax=[5.7,6.5,7.2]
hx=[6.78,6.18]
rx=[7.7,7.8,8.8,7.8,8.7]
#ALONSO
a2x=[1,1.9,2.8]
hax=[2.2,1.6]
l2x=[3,3,3.5,3.5]
ox=[3.8,4.5,5.3,4.5,3.8]
nx=[5.8,5.9,7.2,7.22]
sx=[7.5,8.9,7.5,8.9]
o2x=[9.4,10.1,10.8,10.1,9.4]
#Latitud
#WILMAR
wy=[6,1,3,1,6]
iy=[6,1,]
ly=[6,1,1,1]
my=[1,6,3.5,6,1]
ay=[1,6,1]
hy=[4,4]
ry=[1,6,4.8,3.8,1]
#ALONSO
a2y=[-6,-1,-6]
hay=[-3,-3]
l2y=[-1,-6,-6,-6]
oy=[-3.3,-1,-3.3,-6,-3.3]
ny=[-6,-1,-6,-1]
sy=[-6,-4,-2.5,-1]
o2y=[-3.3,-1,-3.3,-6,-3.3]
#Julianx=[2]
#Juliany=[2]
plt.plot( wx,wy)

plt.plot( ix,iy)
plt.plot( lx,ly)
plt.plot( mx,my)
plt.plot( ax,ay)
plt.plot( hx,hy)
plt.plot( rx,ry)
plt.plot( a2x,a2y)
plt.plot( hax,hay)
plt.plot( l2x,l2y)
plt.plot( ox,oy)
plt.plot( nx,ny)
plt.plot( sx,sy)
plt.plot( o2x,o2y)
plt.title('Comportamiento de un sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (ohm)')
plt.legend() 
plt.grid(True)
plt.show()