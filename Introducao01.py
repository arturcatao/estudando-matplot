import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi, 100)
y = np.cos(2*x)

plt.plot(x, y)
plt.title("Grafico do Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()