# autor: Juan Diego Ortega
import numpy as np
import matplotlib.pyplot as plt

#Creo el vector aleatorio
np.random.seed(7)
vector = np.random.rnd(720)   # ERROR: no existe rnd

# 2) reshape pero con error de forma
matriz = vector.reshape(100, 6)   # ERROR: 100*6 != 720

# Intento de transpuesta mal escrito
matriz_T = matriz.tranpose()   # ERROR: mal escrito
matriz_T_C = np.array(matriz_T, order="c", copy=True)  # ERROR: 'c' minus
matriz_T_F = np.array(matriz_T, order="f", copy=True)

# Subplots con distinta disposición
fig, axes = plt.subplots(2, 3, figsize=(10, 8))
axes = axes.flatten()

x = np.arrange(matriz_T.shape[1])  # ERROR: arange mal escrito
colors = plt.cm.Set2.color         # ERROR: .color no existe

# Primer gráfico con errores en métodos/nombres
axes[0].plot(x, matriz_T[0], color=colors[0])
axes[0].setTitle("Linea fila 0")   # ERROR: set_title es el método correcto
