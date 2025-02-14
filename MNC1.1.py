# Código que implementa un esquema numérico para determinar la precisión de una máquina.
#
# Autor: Dr. Ivan de Jesus May-Cen
# Contacto: imaycen@hotmail.com
# Versión 1.0 : 29/01/2025

import numpy as np  # Se importa NumPy, aunque en este código no es necesario.

# Inicialización de la variable epsilon con el valor 1.0
epsilon = 1.0  
iteracion = 0  # Contador para rastrear el número de iteraciones

# Bucle para encontrar la precisión de máquina
while 1.0 + epsilon != 1.0:  # Verifica si epsilon aún es distinguible en la suma con 1.0
    epsilon /= 2  # Se divide entre 2 en cada iteración para encontrar el menor valor representable
    iteracion += 1  # Se incrementa el contador de iteraciones
    print(f"Iteración: {iteracion}, Precisión de máquina: {epsilon}")  # Imprime la iteración y el valor actual de epsilon

# Se multiplica por 2 para recuperar el último valor válido
epsilon *= 2  
print(f"Precisión de máquina encontrada: {epsilon}")

# Modificaciónes realizado por: Luis Jorge Fuentes Tec