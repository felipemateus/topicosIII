import tkinter
import matplotlib
import random
matplotlib.use( 'tkagg' )

from matplotlib import pyplot as plt
import numpy as np
import math

gamma = 0.2
precision = 0.01
max_iters = 10000
#equação da cicuferencia
#f(x1,x2) = x1**2 + x2**2

num_iters = 0

fig,ax = plt.subplots()

def derivada(x):
    return (2*x)


def gradienteMethod(init_x, init_y,init_z):
    print("\n#############################")
    print("valor de x: %d, valor de y: %d, valor de z: %d"%(init_x,init_y,init_z))
    next_x =init_x
    next_y =init_y
    next_z =init_z

    current_x = np.zeros(10000)
    current_y = np.zeros(10000)
    current_z = np.zeros(10000)

    num_iters=0
    for i in range(max_iters):
        current_x[i] = next_x
        current_y[i] = next_y
        current_z[i] = next_z


        next_x = current_x[i] - gamma*derivada(current_x[i])
        next_y = current_y[i] - gamma*derivada(current_y[i])
        next_z = current_z[i] - gamma*derivada(current_z[i])

        
        step_x = next_x - current_x[i]
        step_y = next_y - current_y[i]
        step_z = next_z - current_z[i]

        num_iters+=1
        print("[step_x: %f  step_y: %f step_z: %f]" %(step_x,step_y,step_z))
        #print("[value_x: %f  value_y: %f value_z: %f]" %(current_x[i],current_y[i],current_z[i]))
        
        #verifica error
        if abs((step_x + step_y+step_z)/2)<=precision:
            break

    print(num_iters)
    #convergencia
    print("[last_x: %f, last_y:%f, last_z:%f] "%(current_x[num_iters-1],current_y[num_iters-1],current_y[num_iters-1] ))
    print("\n#############################")


for i in range(20):
    gradienteMethod(random.randint(1,100) ,random.randint(1,100),random.randint(1,100))
 

#ax.plot(current_x[0:num_iters],color[j],label = 'gamma = '+str(gamma))
    
    
#legend = ax.legend(loc='upper right', shadow=True, fontsize='x-small')


#plt.show()
