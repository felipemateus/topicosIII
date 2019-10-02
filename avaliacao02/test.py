import matplotlib
import numpy as np
import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt


delta = 0.025
x = np.arange(-10.0, 10.0, delta)
y = np.arange(-10.0, 10.0, delta)
X, Y = np.meshgrid(x, y)
Z =X**2 + Y**2

a = []
b = []
for i in range(20):
    a.append(round(random.uniform(0.0,10.0),2))
    b.append(round(random.uniform(0.0,10.0),2))


fig, ax = plt.subplots()
CS = ax.contour(X,Y,Z,levels=[0.10, 1 , 5 ,20, 50])
ax.clabel(CS,inline=1,fontsize=10)
ax.set_title('Simplest default with labels')
print("---  A  ----")
print(a)
print("---  B  ----")
print(b)
ax.scatter(a,b)
plt.show()