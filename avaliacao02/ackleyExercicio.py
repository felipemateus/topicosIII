import tkinter
import matplotlib
matplotlib.use( 'tkagg' )
from matplotlib import pyplot as plt
import numpy as np
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

# derivada de df/dx, para calcular
# a derivada de df/dy  substituir x por y
def derivadaAckley2d(x,y):
    primeiroArg = (2.828*x/(math.sqrt(x**2+y**2)))
    segundoArg = math.exp(-0.2* math.sqrt(0.5*(x**2+y**2)))
    terceiroArg = math.pi * math.exp(0.5*math.cos(2*math.pi*x) + math.cos(2*math.pi*y)) * math.sin(2*math.pi*x)
    result = (primeiroArg * segundoArg) + terceiroArg
    return result

def derivadaAckley3d(x,y,z):
    primeiroArg = (5.6562/math.sqrt(3))*(x/(math.sqrt(x**2 + y**2 +z**2)))
    segundoArg = math.exp(-0.2*math.sqrt(1/3 * (x**2 + y**2 + z**2)))
    terceiroArg = (math.pi*2/3) * math.exp(1/3*(math.cos(2* math.pi*x)) + math.cos(2* math.pi*y) + math.cos(2* math.pi*z)) * math.sin(math.pi*x)
    result = primeiroArg * segundoArg + terceiroArg
    return result


#print(calcAckley2d(1,1))
#print(derivadaAckley2d(0.0000001,0.000000001))
print(derivadaAckley3d(0.1,0.1,0.1))

