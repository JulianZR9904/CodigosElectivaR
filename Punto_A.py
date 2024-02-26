import numpy as np
a=np.array([2,3,4])
b=np.array([5,6,7])

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def productoPunto(a,b):
    p = a*b
    return sum(p)
productocruz = np.cross (a,b)

def div(a,b):
    return a / b



print ("la suma es ",suma(a,b))

print ("la resta es ",resta(a,b))

print ("el producto punto es ",productoPunto (a,b))

print ("el producto cruz es ",productocruz )

print ("la division es ",div (a,b))



