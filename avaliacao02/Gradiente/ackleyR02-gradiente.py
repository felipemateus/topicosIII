import random
import time
import matplotlib
import numpy as np
import random
matplotlib.use( 'tkagg' )

import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading 
import math

#####################################
#     Parametros da Animacao        #
#####################################
def calcAckley2d(x,y):
    primeiraSoma = -0.2*math.sqrt(0.5*(x**2 + y**2))
    segundaSoma = 0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))
    result = -20*math.exp(primeiraSoma) - math.exp(segundaSoma) + math.e + 20 
    return result

delta = 0.2
x = np.arange(-10.0, 10.0, delta)
y = np.arange(-10.0, 10.0, delta)
X, Y = np.meshgrid(x, y)
vfunc = np.vectorize(calcAckley2d)
Z =vfunc(X,Y)

fig, ax = plt.subplots()

gamma = [0.01, 0.05, 0.25, 0.3, 0.5]
current_gamma = 0
color = ['b','r','g','y','m']

precision = 0.005
max_iters = 100
#equação da cicuferencia
#f(x1,x2) = x1**2 + x2**2

num_iters = 0
error = []
def derivadaAckley2d(x,y):
    primeiroArg = (2.828*x/(math.sqrt(x**2+y**2)))
    segundoArg = math.exp(-0.2* math.sqrt(0.5*(x**2+y**2)))
    terceiroArg = math.pi * math.exp(0.5*math.cos(2*math.pi*x) + math.cos(2*math.pi*y)) * math.sin(2*math.pi*x)
    result = (primeiroArg * segundoArg) + terceiroArg
    return result

def derivada(x):
    return (2*x)

def calcError(step_x,step_y):
    errorCalc =(abs(step_x)+abs(step_y))/2
    error.append(errorCalc)
    return errorCalc

current_x = 0
current_y = 0
num_iters = 0 
def gradienteMethod(init_x,init_y,gammaIndex):
    global current_gamma
    global current_x 
    global current_y
    global num_iters   
    current_gamma = gamma[gammaIndex]
    print("\n#############################")
    print("valor de x: %d valor de y: %d"%(init_x,init_y))
    next_x=init_x
    next_y=init_y
    current_x = 0
    current_y = 0
    num_iters=0
    for i in range(max_iters):
        current_x = next_x
        current_y = next_y

        next_x = current_x - gamma[gammaIndex]*derivadaAckley2d(current_x,current_y)
        next_y = current_y - gamma[gammaIndex]*derivadaAckley2d(current_y,current_x)
        
        step_x = next_x - current_x
        step_y = next_y - current_y

        num_iters+=1
        print("[step_x: %f  step_y: %f]" %(step_x,step_y))
        #verifica error
        if(gammaIndex==0):
            time.sleep(0.5)
        else:
            time.sleep(0.09)
        if abs(calcError(step_x,step_y))<=precision:
            break

    #print(num_iters)
    #print(current_x)
    print("\n#############################")
    
def animate(i):
    #print("Passei aqui")
    ax.clear()
    CS = ax.contour(X,Y,Z,levels=8)
    ax.clabel(CS,inline=1,fontsize=5)
    ax.set_title('Ackley R² (gamma: %.2f  Iterações: %d)' %(current_gamma,num_iters))
    #print("---  Current X  ----")
    #print(current_x)
    #print("---  Current Y  ----")
    #print(current_y)
    ax.scatter(current_x,current_y)
    


# 20 inicializações diferentes (com sorteio aleatório da solução candidata inicial e variação da taxa de ajuste α).

def main ():
    random_x = random.uniform(-5,5)
    random_y = random.uniform(-5,5)
    for i in range(len(gamma)):
        gradienteMethod(random_x ,random_y,i)
        error.clear()


if __name__ == "__main__":
    threading.Thread(target=main).start()
    interval = 1000#in seconds   
    
    ani = FuncAnimation(fig,animate,380,interval=interval,blit=False,save_count=50)
    ani.save('animationGradienteAckleyR02.gif',fps=6)
    
    #plt.show()


