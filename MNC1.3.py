# Código que calcula errores en operaciones numéricas
# 
# Autor: Dr. Ivan de Jesus May-Cen
# Contacto: imaycen@hotmail.com
# Versión 1.1 : 06/02/2025 (Corrección de errores y mejoras)
#

def calcular_errores(x, y, valor_real):
    """
    Función que calcula la diferencia entre dos números y sus errores asociados.
    
    Parámetros:
    x (float): Primer número
    y (float): Segundo número
    valor_real (float): Valor exacto esperado
    
    Retorna:
    error_abs (float): Error absoluto
    error_rel (float): Error relativo
    error_cuadratico (float): Error cuadrático
    """

    # Se calcula la diferencia entre los dos valores
    diferencia = x - y

    # Cálculo del error absoluto (corregido)
    error_abs = abs(diferencia - valor_real)

    # Cálculo del error relativo
    error_rel = error_abs / abs(valor_real)

    # Cálculo del error cuadrático
    error_cuadratico = error_abs ** 2

    # Cálculo del error porcentual
    error_pct = error_rel * 100

    # Se imprimen los resultados con formato de precisión mejorado
    print(f"Diferencia: {diferencia:.10e}")
    print(f"Error absoluto: {error_abs:.10e}")
    print(f"Error relativo: {error_rel:.10e}")
    print(f"Error cuadrático: {error_cuadratico:.10e}")
    print(f"Error porcentual: {error_pct:.5f}%")
    
    return error_abs, error_rel, error_cuadratico

# Lista de valores a evaluar con diferentes órdenes de magnitud
valores = [
    (1.0000001, 1.0000000, 0.0000001),  # Primer caso
    (1.000000000000001, 1.000000000000000, 0.000000000000001)  # Segundo caso (mayor precisión)
]

# Se evalúan los valores y se muestran los resultados
for x, y, real in valores:
    print(f"\nPara x={x:.10e}, y={y:.10e}:")
    calcular_errores(x, y, real)

    # Modificaciónes realizado por: Luis Jorge Fuentes Tec