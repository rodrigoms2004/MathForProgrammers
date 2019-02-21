# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/25689238/show-origin-axis-x-y-in-matplotlib-plot

x = np.linspace(0.2,10,100)
fig, ax = plt.subplots()
ax.plot(x, 1/x)
ax.plot(x, np.log(x))
ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.show()