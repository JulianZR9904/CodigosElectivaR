import numpy as np
a=np.array([[2,3,4],[4,3,2],[3,4,2]])
b=np.array([[5,6,7],[7,6,5],[6,7,5]])

print("la suma de matrices:\n",a+b)
print("la resta de matrices:\n",a-b)
print("la multiplicacion de matrices:\n",a@b)
print("el producto cruz de las matrices:\n",np.cross (a,b))
print("la divicion de matrices:\n",a/b)
