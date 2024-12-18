# Paso 1: Solicitar al usuario que ingrese el radio del círculo.
import math

radio = float(input("Por favor, ingrese el radio del círculo: ")) 

# Paso 2: Calcular el área del círculo con la fórmula correspondiente

area = math.pi * (radio**2)

# Paso 3: Mostrarle al usuario el resultado.

print("El área del círculo con radio", radio, "es:", area)