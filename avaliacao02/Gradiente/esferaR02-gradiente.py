import random
import time
import matplotlib
import numpy as np
import random
import sys
matplotlib.use( 'tkagg' )

import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading    
#####################################
#     Parametros da Animacao        #
#####################################
delta = 1
x = np.arange(-50.0, 50.0, delta)
y = np.arange(-50.0, 50.0, delta)
X, Y = np.meshgrid(x, y)
Z =X**2 + Y**2
fig, ax = plt.subplots()

gamma = [0.01, 0.05, 0.25, 0.3, 0.97]
current_gamma = 0
color = ['b','r','g','y','m']

precision = 0.01
max_iters = 10000
#equação da cicuferencia
#f(x1,x2) = x1**2 + x2**2

num_iters = 0
error = []


def derivada(x):
    return (2*x)

def calcError(step_x,step_y):
    errorCalc = abs((step_x+step_y)/2)
    error.append(errorCalc)
    return errorCalc

fig2,ax2 = plt.subplots()

def graficoErrorIteração(indexGamma):
    #iterações = np.arange(0,num_iters)
    ax2.plot(error[:100],color[indexGamma],label = 'gamma = '+str(gamma[indexGamma]))

    if(indexGamma == (len(gamma)-1)):
        legend = ax2.legend(loc='upper right', shadow=True, fontsize='x-small')
        ax2.set_xlabel("Iterações")
        ax2.set_ylabel("error")
        #fig2.show()
        plt.show(fig2)




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

        next_x = current_x - gamma[gammaIndex]*derivada(current_x)
        next_y = current_y - gamma[gammaIndex]*derivada(current_y)
        
        step_x = next_x - current_x
        step_y = next_y - current_y

        num_iters+=1
        print("[step_x: %f  step_y: %f]" %(step_x,step_y))
        #verifica error
        if(gammaIndex==0):
            time.sleep(0.1)
        else:
            time.sleep(0.2)
        if abs(calcError(step_x,step_y))<=precision:
            break

    print(num_iters)
    print(current_x)
    print("\n#############################")
    
def animate(i):
    print("Passei aqui")
    ax.clear()
    CS = ax.contour(X,Y,Z,levels=8)
    ax.clabel(CS,inline=1,fontsize=5)
    ax.set_title('Circuferência R² (gamma: %.2f  Iterações: %d)' %(current_gamma,num_iters))
    print("---  Current X  ----")
    print(current_x)
    print("---  Current Y  ----")
    print(current_y)
    ax.scatter(current_x,current_y)
    


# 20 inicializações diferentes (com sorteio aleatório da solução candidata inicial e variação da taxa de ajuste α).

def main ():
    random_x = random.randint(-50,50)
    random_y = random.randint(-50,50)
    for i in range(len(gamma)):
        gradienteMethod(random_x ,random_y,i)
        graficoErrorIteração(i)

        error.clear()


if __name__ == "__main__":
    if len(sys.argv)>1:
        print("Carregando grafico de erro")
        main()
    else:
        threading.Thread(target=main).start()
        interval = 1000#in seconds   
    
        ani = FuncAnimation(fig,animate,330,interval=interval,blit=False,save_count=50)
        #ani.save('animationGradienteEsferaR02.gif',fps=6)
        
        plt.show()


