import numpy as np
import matplotlib.pyplot as plt

# Número de muestras
n = 10000

# Generar números aleatorios uniformes en [0, 1]
random_numbers = np.random.rand(n)

# Aplicar transformada inversa
samples = random_numbers**(2/3)

# Graficar un histograma
num_bins = 500
plt.hist(samples, bins=num_bins, density=True, alpha=0.6, color='b', edgecolor='k')
plt.xlabel('Valores Generados')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Distribución Generada')
plt.grid(True)
plt.show()
