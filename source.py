import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
n = input("How much dots do you have? ")
_x = []
_y = []
for i in range(int(n)):
    _x.append(float(input("x[" + str(i) + "]= ")))
    _y.append(float(input("y[" + str(i) + "]= ")))
lag = interpolate.lagrange(_x, _y)
x = np.arange(-15, 15, 0.1)
y = lag(x)
plt.plot(_x, _y, "o", x, y, "-")
plt.show()
