import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(-10,10,0.1)
y = 1/(1+math.e**(-x))

plt.plot(x,y)

#plt.show()
a = np.zeros([3,4])
print a