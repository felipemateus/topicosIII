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


def gradienteMethod(init_x,init_y):
    print("\n#############################")
    print("valor de x: %d valor de y: %d"%(init_x,init_y))
    next_x=init_x
    next_y=init_y
    current_x = np.zeros(10000)
    current_y = np.zeros(10000)

    num_iters=0
    for i in range(max_iters):
        current_x[i] = next_x
        current_y[i] = next_y

        next_x = current_x[i] - gamma*derivada(current_x[i])
        next_y = current_y[i] - gamma*derivada(current_y[i])
        
        step_x = next_x - current_x[i]
        step_y = next_y - current_y[i]

        num_iters+=1
        print("[step_x: %f  step_y: %f]" %(step_x,step_y))
        #verifica error
        if abs((step_x + step_y)/2)<=precision:
            break

    print(num_iters)
    print(current_x[num_iters-1])
    print("\n#############################")


# 20 inicializações diferentes (com sorteio aleatório da solução candidata inicial e variação da taxa de ajuste α).
for i in range(20):
    gradienteMethod(random.randint(1,100) ,random.randint(1,100))

# agora fazendo genético:

