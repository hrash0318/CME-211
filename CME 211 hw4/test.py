import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,20.0,0.01)
s = np.sin(2*np.pi*t)

plt.plot(t,s)
plt.show()