import random

#Para as funções listadas abaixo, realizar a otimização utilizando um Otimização por Enxame de Partículas com
#população de 20 indivíduos. Trace gráficos dos valores mínimos e médios da função de aptidão para cada iteração.
#Realize 10 diferentes inicializações com alterações nos parâmetros do algoritmo, reinicie o treinamento e comente os
#resultados obtidos.

#equação da cicuferencia
#f(x1,x2) = x1**2 + x2**2

#Criar a população de 20 individuos:
class Particula:
    def __init__(self,X,Y):
        self.x = x
        self.y = Y
        #self.bestFitness =  
    
    def setFitness(self,fit):
        self.fitness = fit
    
    def mostra(self):
        print("GeneX: %f, GeneY: %f, fitness:%f  " %(self.geneX, self.geneY, self.fitness))







#####################################
#        Parametros do PSO          #
#####################################
N = 20
W = 0.5
c1 = 0.8
c2 = 0.9 

#####################################
#         funcCircunferencia        #
#####################################
def funcCircunferencia(values):
    return values.geneX**2 + values.geneY**2



#####################################
#         randonValues              #
#####################################
def randonValues():
    x = round(random.uniform(0.0,10.0),2)
    y = round(random.uniform(0.0,10.0),2)
    return x,y


#####################################
#         genPopulacao              #
#####################################
#
def genPopulacao():
    for i in range(N):
        x,y = randonValues()
        populacao.append(Particula(x,y))


#####################################
#         genPopulacao              #
#####################################

def calcFitness():
    fitness = 0 
    print("#######   fitness  ######")
    for i in range(N):
        populacao[i].fitness = funcCircunferencia(populacao[i])
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
            selecionados[i].geneX = selecionados[i].geneX - PMULT
        else:
            selecionados[i].geneX = selecionados[i].geneX + PMULT
        if(selecionados[i].geneY >0):
            selecionados[i].geneY = selecionados[i].geneY - PMULT
        else:
            selecionados[i].geneY = selecionados[i].geneY + PMULT


    
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
    mutation(selecionados)

    for i in range(M):populacao.pop(),populacao.append(selecionados[i])

#####################################
#           novaGeração             #
#####################################

def verificaPopulacao():
    for i in range(N):
        if(populacao[i].fitness < 0.01):
            return True,i
    return False,0 

    



#####################################
#               main                #
#####################################
def main():
    #inicaliza geração
    genPopulacao()
    #calcula a  fitness da função
    fitness = calcFitness()
    #encontra nova Geração:
    while(True):
        novaGeração() #<--- fez a o crossover e multação aqui
        calcFitness()
        #verifica se encontrou objetivo
        state,i =verificaPopulacao()
        if(state):
            print("************** ENCONTRADO ****************")
            populacao[i].mostra()
            return 0

        print("Pass")
        for i in range(N):
            print("GeneX: %f, GeneY: %f, fitness:%f  " %(populacao[i].geneX, populacao[i].geneY, populacao[i].fitness))






if __name__ == "__main__":
    main()