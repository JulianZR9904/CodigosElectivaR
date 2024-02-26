print( " \n Calcule el valor de potencia que consume un circuito, ingrese a continuación los valores:")

#Solicitud de los valores al usuario
voltaje = float(input("\n Ingrese el valor del voltaje: "))
Corriente = float(input("\n Ingrese el valor de la corriente: "))

# operación
Potencia = voltaje * Corriente
print(f"\n El valor de la potencia que consume el circuito es: {Potencia} W \n")
