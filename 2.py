import numpy as np

# Definir tasas de llegada y servicio
tasa_llegada = 0.3  # Tasa de llegada
tasa_servicio = 0.8 # Tasa de servicio

# Inicializar variables
tiempo = 0          # Tiempo inicial
N = 0               # Tamaño de la cola
Tiempos_llegada = []# Lista para almacenar tiempos de llegada
Tiempos_salida = [] # Lista para almacenar tiempos de salida

while tiempo < 200:
    # Generar tiempo de llegada y servicio
    tiempo_llegada = np.random.exponential(1/tasa_llegada)
    tiempo_servicio = np.random.exponential(1/tasa_servicio)
    
    # Actualizar tiempo
    tiempo += tiempo_llegada
    
    # Verificar si hay tiempos de salida antes de calcular el tiempo de espera
    if Tiempos_salida:
        tiempo_espera = max(Tiempos_salida) - tiempo
    else:
        tiempo_espera = 0
    
    # Tiempo de salida
    tiempo_salida = tiempo + tiempo_espera + tiempo_servicio
    
    # Actualizar listas
    Tiempos_llegada.append(tiempo)
    Tiempos_salida.append(tiempo_salida)
    
    # Actualizar tamaño de la cola
    N += 1
    
    # Imprimir resultados
    print(f'Iteración: {N}, Tamaño de la cola (N): {N}, Tiempo de llegada (Tiempos_llegada): {tiempo}, Tiempo de salida (Tiempos_salida): {tiempo_salida}')
# Imprimir resultados finales
print(f'\nResultados finales:')
print(f'Tamaño de la cola (N): {N}')
print(f'Tiempos de llegada (Tiempos_llegada): {Tiempos_llegada}')
print(f'Tiempos de salida (Tiempos_salida): {Tiempos_salida}')
