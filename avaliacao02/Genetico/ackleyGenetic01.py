import random
import time
import matplotlib
import numpy as np
import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import math    

#Algoritmo Genético com população de 20 indivíduos.
#Trace gráficos dos valores mínimos e médios da função de aptidão para cada iteração. Realize 10 diferentes
#inicializações com alterações nos parâmetros do algoritmo e comente os resultados obtidos
##### Globals  ######
numIteration = 0


def calcAckley2d(x,y):
    primeiraSoma = -0.2*math.sqrt(0.5*(x**2 + y**2))
    segundaSoma = 0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))
    result = -20*math.exp(primeiraSoma) - math.exp(segundaSoma) + math.e + 20 
    return result


#Criar a população de 20 individuos:
class Cromossomo:
    def __init__(self,geneX,geneY):
        self.geneX = geneX
        self.geneY = geneY
    
    def setFitness(self,fit):
        self.fitness = fit
    
    def mostra(self):
        print("GeneX: %f, GeneY: %f, fitness:%f  " %(self.geneX, self.geneY, self.fitness))




#####################################
#         Parametros do GA          #
#####################################
N = 20
M = 6 #Selecionados(Pais)
populacao = []
PREC = 0.5 #taxa de recombinação
PMULT = 0.001 # taxa de mutação
#####################################
#     Parametros do Animacao        #
#####################################
delta = 0.2
x = np.arange(-10.0, 10.0, delta)
y = np.arange(-10.0, 10.0, delta)
X, Y = np.meshgrid(x, y)
vfunc = np.vectorize(calcAckley2d)
Z =vfunc(X,Y)

fig, ax = plt.subplots()


#####################################
#         funcCircunferencia        #
#####################################
def funcCircunferencia(values):
    return values.geneX**2 + values.geneY**2



#####################################
#         randonValues              #
#####################################
def randonValues():
    x = round(random.uniform(-5.0,5.0),2)
    y = round(random.uniform(-5.0,5.0),2)
    return x,y


#####################################
#         genPopulacao              #
#####################################
#
def genPopulacao():
    for i in range(N):
        x,y = randonValues()
        populacao.append(Cromossomo(x,y))


#####################################
#          calcFitness              #
#####################################

def calcFitness():
    fitness = 0 
    print("#######   fitness  ######")
    for i in range(N):
        populacao[i].fitness = calcAckley2d(populacao[i].geneX,populacao[i].geneY)
        print(populacao[i].fitness)
    return fitness

#####################################
#             crossOver             #
#####################################
def crossOver(selecionados):
    #cross over em x de 1 e 2
    temp = selecionados[0].geneX 
    selecionados[0].geneX  = selecionados[1].geneX
    selecionados[1].geneX = temp
    #cross over em Y de 3 e 4
    temp = selecionados[2].geneY 
    selecionados[2].geneY  = selecionados[3].geneY
    selecionados[3].geneY = temp
    #cross over em Y de 5 e 6
    temp = selecionados[4].geneX 
    selecionados[4].geneX  = selecionados[5].geneX
    selecionados[5].geneX = temp

#####################################
#             mutation             #
#####################################
def mutation(selecionados):
    #verificar
     for i in range(0,len(selecionados)):
        if(selecionados[i].geneX >0):
            selecionados[i].geneX = selecionados[i].geneX - random.randint(1,9) * PMULT 
        else:
            selecionados[i].geneX = selecionados[i].geneX + random.randint(1,9) * PMULT
        if(selecionados[i].geneY >0):
            selecionados[i].geneY = selecionados[i].geneY - random.randint(1,9) * PMULT
        else:
            selecionados[i].geneY = selecionados[i].geneY + random.randint(1,9) * PMULT 

def mutation():
    #verificar
    # for i in range(0,N):
    #    populacao[i].geneX = populacao[i].geneX + random.randint(-9,9) * PMULT 
    #    populacao[i].geneY = populacao[i].geneY + random.randint(-9,9) * PMULT
    for i in range(0,N):
        if(populacao[i].geneX >0):
            populacao[i].geneX = populacao[i].geneX - random.randint(1,9) * PMULT 
        else:
            populacao[i].geneX = populacao[i].geneX + random.randint(1,9) * PMULT
        if(populacao[i].geneY >0):
            populacao[i].geneY = populacao[i].geneY - random.randint(1,9) * PMULT
        else:
            populacao[i].geneY = populacao[i].geneY + random.randint(1,9) * PMULT 

#####################################
#       TournmentSelection          #
#####################################
def TournmentSelection():
    selecionados = []
    for i in range(M):
        sorteados= []
        for i in range(4):
            selecionado = random.randint(0,N-1)
            sorteados.append(populacao[selecionado])
        
        sorteados.sort(key=lambda x: x.fitness)
        selecionados.append(sorteados[0])
    return selecionados

#####################################
#           novaGeração             #
#####################################

def novaGeração():
    #ordena por fitness
    populacao.sort(key=lambda x: x.fitness)
    #agora tenho q fazer a seleção dos pais. Existem vários métodos para tal: 
    # Roulette Wheel Selection, Stochastic Universal Sampling (SUS),Tournament Selection,Rank Selection
    selecionados = TournmentSelection()
    crossOver(selecionados)
    #mutation(selecionados)
    mutation()

    for i in range(M):populacao.pop(),populacao.append(selecionados[i])

#####################################
#       verificaPopulacao           #
#####################################

def verificaPopulacao():
    for i in range(N):
        if(populacao[i].fitness < 0.01):
            return True,i
    return False,0 

#####################################
#            animação               #
#####################################

def animate(i):
    a = []
    b = []
    for i in range(20):
        a.append(populacao[i].geneX)
        b.append(populacao[i].geneY)
    #print("Passei aqui")
    ax.clear()
    CS = ax.contour(X,Y,Z,levels=8)
    ax.clabel(CS,inline=1,fontsize=5)
    ax.set_title('Genético Ackley R² (Iterações: %d)' %numIteration)

    #print("---  A  ----")
    #print(a)
    #print("---  B  ----")
    #print(b)
    ax.scatter(a,b)

#ani = FuncAnimation(fig, animate, np.arange(1, 200), interval=10, blit=True)
#plt.show()


#####################################
#               main                #
#####################################
def main():
    global numIteration
    numIteration = 0
    #inicaliza geração
    genPopulacao()
    #calcula a  fitness da função
    fitness = calcFitness()
    #encontra nova Geração:
    while(True):
        numIteration+=1
        novaGeração() #<--- fez a o crossover e multação aqui
        calcFitness()
        #verifica se encontrou objetivo
        state,i =verificaPopulacao()
        if(state):
            print("************** ENCONTRADO ****************")
            populacao[i].mostra()
            print("Numero de iterações: %d" %numIteration)
            return 0

        time.sleep(0.5)

        print("Pass")
        for i in range(N):
            print("GeneX: %f, GeneY: %f, fitness:%f  " %(populacao[i].geneX, populacao[i].geneY, populacao[i].fitness))






if __name__ == "__main__":
    threading.Thread(target=main).start()
    interval = 2#in seconds     
    ani = FuncAnimation(fig,animate,100,interval=interval*1e+3,blit=False)
    ani.save('animationGeneticoAckleyR02.gif',fps=6)
    
    #plt.show()

    #main()