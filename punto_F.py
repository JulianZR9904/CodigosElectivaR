import math

def fuerza_cilindro(presion, diametro_piston):
    area = (math.pi * (diametro_piston ** 2)) / 4
    fuerza = presion * area
    return fuerza

# Valores dados
presion = 100  # Presión en psi (libras por pulgada cuadrada)
diametro_piston = 2  # Diámetro del pistón en pulgadas

# Calcular la fuerza de avance y retroceso
fuerza_avance = fuerza_cilindro(presion, diametro_piston)
fuerza_retroceso = fuerza_cilindro(presion, diametro_piston)

# Mostrar resultados
print("Fuerza de avance del cilindro:", fuerza_avance, "libras")
print("Fuerza de retroceso del cilindro:", fuerza_retroceso, "libras")
