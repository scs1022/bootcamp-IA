#import math as m
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

#Generamos una grafica para una X lineal (recta)
plt.plot(x, x, label='lineal') # y=x

#Generamos otra grafica para una X cuadratica (parabola)
plt.plot(x, x**2, label='cuadrática') # y=x*x

#Generamos una grafica para una X Cubica (cúbica)
plt.plot(x, x**3, label='cúbica') # y=x*x*x

#Generamos una grafica para una X cuártica ("x a la 4")
plt.plot(x, x**4, label='cuártica') # y=x*x*x

#Generamos una grafica para una X raiz cuadrada (square root: sqrt)
plt.plot(x, x**(1/2), label='raiz cuadrada') # y=x**(1/2)

#Agregamos las etiquetas y añadimos una leyenda.
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title("Gráfica de funciones: lineal, cuadrática, cúbica, cuártica, raiz cuadrada")
plt.legend()
plt.grid()
plt.show()
#plt.savefig('grafica_funciones.png')
plt.savefig('grafica_funciones2.jpg')
plt.close()