import tkinter
import matplotlib
matplotlib.use( 'tkagg' )

from matplotlib import pyplot as plt
import numpy as np
import math

gamma = [0.015, 0.02, 0.05, 0.09]
color = ['b','r','g','y']
precision = 0.01
max_iters = 10000

num_iters = 0

fig,ax = plt.subplots()
def der(x):
    return (0.30*np.pi*x - 37.5*np.pi*(x**(-2)))

for j in range(4):
    next_x=1
    current_x = np.zeros(10000)
    num_iters=0
    for i in range(max_iters):
        current_x[i] = next_x
        next_x = current_x[i] - gamma[j]*der(current_x[i])
        step = next_x - current_x[i]
        num_iters+=1
        
        if abs(step)<=precision:
            break
    print(num_iters)
    print(current_x[num_iters-1])
    #ax.axis([0, num_iters,-1,0])
    ax.plot(current_x[0:num_iters],color[j],label = 'gamma = '+str(gamma[j]))
    
    
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-small')

#plt.figure()
#plt.axis([0, num_iters,-1,0])
#plt.plot(current_x)
plt.show()
