import numpy as np

xn = 0
yn = 0
vxn = 3
vyn = 9
g = 9.8

t = np.arange(0, 5, 0.1)
x = xn + vxn * t
y = yn = vyn * t - g * t**2 / 2
coordinatiki = np.zeros((len(t), 3))
for i in range(len(t)):
  coordinatiki[i, 0] = t[i]
  coordinatiki[i, 1] = x[i]
  coordinatiki[i, 2] = y[i]
print(coordinatiki)