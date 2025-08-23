import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
cos = np.cos(x)
sen = np.sin(x)

plt.figure("Graficos Cossenoidais", figsize=(8, 4))
plt.subplots_adjust(
    left=0.12,
    right=0.946,
    top=0.9,
    bottom=0.14,
    wspace=0.438,
    hspace=0.4
)

ax1 = plt.subplot(1, 2, 1) # (n de linhas, n de colunas, posição)
plt.plot(x, cos)
ax1.set_title("Grafico do Cosseno")
ax1.set_xlabel("Tempo")
ax1.set_ylabel("Amplitude")
plt.grid()

ax2 = plt.subplot(1, 2, 2)
plt.plot(x, sen)
ax2.set_title("Grafico do Seno")
ax2.set_xlabel("Tempo")
ax2.set_ylabel("Amplitude")
plt.grid()

plt.show()