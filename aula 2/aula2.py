import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi, 100)
y = np.cos(2*x)
a = np.sin(2*x)

plt.figure("Cosseno", figsize=(7, 5)) # tupla largura x altura em polegadas
plt.plot(x, y)
plt.title("Grafico do Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")

plt.figure("Seno", figsize=(7, 5))
plt.plot(x, a)
plt.title("Grafico do Seno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()