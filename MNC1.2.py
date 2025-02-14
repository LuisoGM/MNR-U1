# Código que implementa un esquema numérico para determinar la aproximación de Leibniz.
#
# Autor: Dr. Ivan de Jesus May-Cen
# Contacto: imaycen@hotmail.com
# Versión 1.0 : 29/01/2025

import numpy as np  # Se usa para obtener el valor real de π
import matplotlib.pyplot as plt  # Se usa para generar gráficos

def leibniz_pi(n):
    """
    Calcula la aproximación de π usando la serie de Leibniz.

    Parámetros:
    n (int): Número de términos en la serie.

    Retorna:
    float: Aproximación de π.
    """
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

# Valor real de π
true_pi = np.pi  

# Diferentes valores de N para la aproximación
N_values = [10, 100, 1000, 10000]  

# Listas para almacenar los errores calculados
errors_abs = []  # Error absoluto
errors_rel = []  # Error relativo
errors_sq = []   # Error cuadrático

# Iteración sobre los diferentes valores de N
for N in N_values:
    approx_pi = leibniz_pi(N)  # Cálculo de π usando la serie de Leibniz
    error_abs = abs(true_pi - approx_pi)  # Cálculo del error absoluto
    error_rel = error_abs / true_pi  # Cálculo del error relativo
    error_sq = error_abs**2  # Cálculo del error cuadrático
    
    # Almacenamos los errores en las listas
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_sq.append(error_sq)
    
    # Impresión de los resultados
    print(f"N={N}: Aproximación={approx_pi}, Error absoluto={error_abs}, Error relativo={error_rel}, Error cuadrático={error_sq}")

# Gráfica de los errores en escala logarítmica
plt.figure(figsize=(8, 6))
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o', linestyle='--')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s', linestyle='-.')
plt.plot(N_values, errors_sq, label='Error cuadrático', marker='^', linestyle=':')
plt.xscale('log')  # Escala logarítmica en el eje X
plt.yscale('log')  # Escala logarítmica en el eje Y
plt.xlabel('Número de términos (N)')
plt.ylabel('Error')
plt.legend()
plt.title('Errores en la aproximación de π usando la serie de Leibniz')
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()

# Modificaciónes realizado por: Luis Jorge Fuentes Tec