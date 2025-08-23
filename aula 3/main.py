import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
a = np.cos(x)
b = np.sin(x)

plt.figure("Gráfico Seno Cosseno", figsize=(6,4))
plt.plot(x, a)
plt.plot(x, b)
plt.grid()
plt.show() 