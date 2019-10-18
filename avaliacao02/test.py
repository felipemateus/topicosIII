import matplotlib
import numpy as np
import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import math

def calcAckley2d(x,y):
    primeiraSoma = -0.2*math.sqrt(0.5*(x**2 + y**2))
    segundaSoma = 0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))
    result = -20*math.exp(primeiraSoma) - math.exp(segundaSoma) + math.e + 20 
    return result

def derivadaAckley2d(x,y):
    primeiroArg = (2.828*x/(math.sqrt(x**2+y**2)))
    segundoArg = math.exp(-0.2* math.sqrt(0.5*(x**2+y**2)))
    terceiroArgumento = math.pi * math.exp(0.5*math.cos(2*math.pi*x) + math.cos(2*math.pi*y)) * math.sin(2*math.pi*x)
    result = primeiroArg * segundoArg + terceiroArgumento
    return result


delta = 0.025
x = np.arange(-10.0, 10.0, delta)
y = np.arange(-10.0, 10.0, delta)
X, Y = np.meshgrid(x, y)
vfunc = np.vectorize(derivadaAckley2d)
#vfunc = np.vectorize(calcAckley2d)

Z =vfunc(X,Y)



a = []
b = []
for i in range(20):
    a.append(round(random.uniform(-10.0,10.0),2))
    b.append(round(random.uniform(-10.0,10.0),2))


fig, ax = plt.subplots()
CS = ax.contour(X,Y,Z,levels=8)
ax.clabel(CS,inline=1,fontsize=5)
ax.set_title('Simplest default with labels')
print("---  A  ----")
print(a)
print("---  B  ----")
print(b)
ax.scatter(a,b)
plt.show()