import math
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

#print("hola-mundo.py")
c = math.sqrt(2)

x = np.linspace(-2*math.pi, 2*math.pi,100)
y = np.cos(x)

plt.plot(x,y)
plt.title("y=cos(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
