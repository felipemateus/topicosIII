import matplotlib
import numpy as np
import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
import threading

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


def geraAleatorio():
    while True:
        print(" NOVOS RANDS ___")
        time.sleep(3)
        a.clear()
        b.clear()
        for i in range(20):
            a.append(round(random.uniform(0.0,10.0),2))
            b.append(round(random.uniform(0.0,10.0),2))


threading.Thread(target=geraAleatorio).start()


fig, ax = plt.subplots()
def animate(i):
    print("Passei aqui")
    ax.clear()
    CS = ax.contour(X,Y,Z,levels=[0.10, 1 , 5 ,20, 50])
    ax.clabel(CS,inline=1,fontsize=10)
    ax.set_title('Simplest default with labels')
    print("---  A  ----")
    print(a)
    print("---  B  ----")
    print(b)
    ax.scatter(a,b)
    #a.clear()
    #b.clear()
    #for i in range(20):
    #    a.append(round(random.uniform(0.0,10.0),2))
    #    b.append(round(random.uniform(0.0,10.0),2))


interval = 2 #in seconds     
ani = FuncAnimation(fig,animate,5,interval=interval*1e+3,blit=False)

plt.show()

