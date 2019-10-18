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
#####################################
#     Parametros do Animacao        #
#####################################
delta = 1
x = np.arange(-50.0, 50.0, delta)
y = np.arange(-50.0, 50.0, delta)
z = np.arange(-50.0, 50.0, delta)

X, Y, Z = np.meshgrid(x, y, z)
K =X**2 + Y**2 + Z**2
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
current_x = 0
current_y = 0
current_z = 0

num_iters = 0 

def gradienteMethod(init_x, init_y,init_z,gammaIndex):
    global current_gamma
    global current_x 
    global current_y
    global current_z
    global num_iters 
    current_gamma = gamma[gammaIndex]



    print("\n#############################")
    print("valor de x: %d, valor de y: %d, valor de z: %d"%(init_x,init_y,init_z))
    next_x =init_x
    next_y =init_y
    next_z =init_z

    current_x = 0
    current_y = 0
    current_z = 0

    num_iters=0
    for i in range(max_iters):
        current_x = next_x
        current_y = next_y
        current_z = next_z


        next_x = current_x - gamma*derivada(current_x)
        next_y = current_y - gamma*derivada(current_y)
        next_z = current_z - gamma*derivada(current_z)

        
        step_x = next_x - current_x
        step_y = next_y - current_y
        step_z = next_z - current_z

        num_iters+=1
        print("[step_x: %f  step_y: %f step_z: %f]" %(step_x,step_y,step_z))
        #print("[value_x: %f  value_y: %f value_z: %f]" %(current_x,current_y[i],current_z[i]))
        
        #verifica error
        if abs((step_x + step_y+step_z)/2)<=precision:
            break

    print(num_iters)
    #convergencia
    #print("[last_x: %f, last_y:%f, last_z:%f] "%(current_x[num_iters-1],current_y[num_iters-1],current_y[num_iters-1] ))
    print("\n#############################")

def animate(i):
    print("Passei aqui")
    ax.clear()
    CS = ax.contour(X,Y,Z,K,levels=8)
    ax.clabel(CS,inline=1,fontsize=5)
    ax.set_title('Circuferência R² (gamma: %.2f  Iterações: %d)' %(current_gamma,num_iters))
    print("---  Current X  ----")
    print(current_x)
    print("---  Current Y  ----")
    print(current_y)
    ax.scatter(current_x,current_y,current_z)

def main ():
    random_x = random.randint(-50,50)
    random_y = random.randint(-50,50)
    for i in range(len(gamma)):
        gradienteMethod(random.randint(1,100) ,random.randint(1,100),random.randint(1,100),i)
        error.clear()



if __name__ == "__main__":
    threading.Thread(target=main).start()
    interval = 1000#in seconds   
    
    ani = FuncAnimation(fig,animate,330,interval=interval,blit=False,save_count=50)
    #ani.save('animation.gif',fps=6)
    plt.show()

    

#for i in range(20):
#    gradienteMethod(random.randint(1,100) ,random.randint(1,100),random.randint(1,100))
 

#ax.plot(current_x[0:num_iters],color[j],label = 'gamma = '+str(gamma))
    
    
#legend = ax.legend(loc='upper right', shadow=True, fontsize='x-small')


