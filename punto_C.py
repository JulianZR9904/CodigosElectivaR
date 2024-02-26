import numpy as np

def rectangulares_a_cilindricas(x, y, z):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    z_cylindrical = z
    return rho, phi, z_cylindrical

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan2(np.sqrt(x**2 + y**2), z)
    phi = np.arctan2(y, x)
    return r, theta, phi

# interaccion de uso
x = 1
y = 1
z = 1

rho, phi, z_cylindrical= rectangulares_a_cilindricas(x, y, z)
print("Coordenadas cilíndricas:")
print("Rho:", rho)
print("Phi:", phi)
print("Z:", z_cylindrical)


r, theta, phi_spherical = cartesian_to_spherical(x, y, z)
print("\nCoordenadas esféricas:")
print("R:", r)
print("Theta:", theta)
print("Phi:", phi_spherical)
