import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)

plt.plot(t, s)
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.savefig("myfigure.png")


