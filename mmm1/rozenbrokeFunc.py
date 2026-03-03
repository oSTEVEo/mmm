import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection = '3d') 

## Make data
X = np.arange(-2.5, 2.5, 0.025)
Y = np.arange(-1, 3.5, 0.025)
X, Y = np.meshgrid(X, Y)
Y += 1
Z = 100*(Y-X**2)**2 + (1-X)**2
Z_masked = Z.copy()
mask = (Z < -1) | (Z > 2500)
Z_masked[mask] = np.nan

surface = ax.plot_surface(X, Y, Z_masked, cmap=cm.rainbow, linewidth=0, antialiased=False)
ax.set_zlim(top=4000)
fig.colorbar(surface, shrink=0.5, aspect=5)
plt.show()