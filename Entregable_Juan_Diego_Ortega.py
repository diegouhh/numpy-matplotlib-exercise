# autor: Juan Diego Ortega
import numpy as np
import matplotlib.pyplot as plt

#Creo el vector aleatorio
np.random.seed(7)  # para que siempre salgan iguales
vector = np.random.rand(720)

# 2) Le cambio la forma a (120, 6)
matriz = vector.reshape(120, 6)

#Hago la transpuesta y dos copias (una en C y otra en F)
matriz_T = matriz.T
matriz_T_C = np.array(matriz_T, order="C", copy=True)
matriz_T_F = np.array(matriz_T, order="F", copy=True)

#Armo la figura con 6 gráficos (3x2)
fig, axes = plt.subplots(3, 2, figsize=(10, 8))
axes = axes.flatten()

x = np.arange(matriz_T.shape[1])  # eje de 0 a 119
colors = plt.cm.Set2.colors        # colores bonitos

#los gtráficos
# Línea
axes[0].plot(x, matriz_T[0], color=colors[0])
axes[0].set_title("Línea fila 0")
axes[0].grid(True)
# Barras
axes[1].bar(np.arange(15), matriz_T[1, :15], color=colors[1])
axes[1].set_title("Barras fila 1 (15 datos)")
axes[1].grid(True)
# Dispersión
axes[2].scatter(x, matriz_T[2], s=20, color=colors[2])
axes[2].set_title("Scatter fila 2")
axes[2].grid(True)
# Histograma
axes[3].hist(matriz_T[3], bins=12, color=colors[3], alpha=0.7)
axes[3].set_title("Hist fila 3")
axes[3].grid(True)
# Stem
axes[4].stem(np.arange(30), matriz_T[4, :30], linefmt='--', markerfmt='o')
axes[4].set_title("Stem fila 4 (30 puntos)")
axes[4].grid(True)
# Pie
valores = matriz_T[5].reshape(6, 20).mean(axis=1)
axes[5].pie(valores, autopct="%1.1f%%", colors=colors[:6])
axes[5].set_title("Pie fila 5")
# 6) Ajusto espacios
fig.suptitle("Ejercicio: 6 tipos de gráficas", fontsize=13)
plt.tight_layout()
plt.show()
