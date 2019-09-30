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
        self.x = X
        self.y = Y
        self.xVelocity = 0
        self.yVelocity = 0
        self.pbestFitness =  1000 ##iniciliza com um valor grande
        self.pbest = [X,Y]
    
    def setFitness(self,fit):
        self.fitness = fit
    
    def mostra(self):
        print("GeneX: %f, GeneY: %f, fitness:%f  " %(self.x, self.x, self.fitness))

    def atualizaBestFitness(self):
        #caso for pontode maximo <(menor) passa a ser >(maior) 
        if self.fitness < self.pbestFitness:
            self.pbestFitness = self.fitness
            self.pbest =[self.x,self.y] 





#####################################
#        Parametros do PSO          #
#####################################
N = 20
W = 0.5
c1 = 0.8
c2 = 0.9
#global populacao
#global gbest
#global gbestFitness 

populacao = []
gbest = [1000,1000]
gbestFitness = 1000.0 

#####################################
#         funcCircunferencia        #
#####################################
def funcCircunferencia(values):
    return values.x**2 + values.y**2



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
#          calcFitness              #
#####################################

def calcFitness():
    global gbestFitness 
    global gbest
    print("#######   fitness  ######")
    for i in range(N):
        populacao[i].fitness = funcCircunferencia(populacao[i])
        populacao[i].atualizaBestFitness()
        if (populacao[i].fitness < gbestFitness):
            gbestFitness = populacao[i].fitness
            gbest = [populacao[i].x,populacao[i].y] 
        print(populacao[i].fitness)
    


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
#       verificaPopulacao           #
#####################################

def verificaPopulacao():
    for i in range(N):
        if(populacao[i].fitness < 0.01):
            return True,i
    return False,0 

#####################################
#          calcVelocidade           #
#####################################

def calcVelocidade(gbest):
    for i in range(N):
        r1 = round(random.uniform(0.0,1.0),2)
        r2 = round(random.uniform(0.0,1.0),2)
        oldVx = populacao[i].xVelocity
        oldVy = populacao[i].yVelocity
        posx = populacao[i].x
        posy = populacao[i].y
        pbestX = populacao[i].pbest[0]
        pbestY = populacao[i].pbest[1]
        populacao[i].xVelocity= W*oldVx + c1*r1*(pbestX-posx) + c2*r2*(gbest[0]-posx)  
        populacao[i].yVelocity= W*oldVy + c1*r1*(pbestY-posy) + c2*r2*(gbest[1]-posy)  
     
#####################################
#              attPos               #
#####################################

def attPos():
    for i in range(N):
       populacao[i].x = populacao[i].x + populacao[i].xVelocity
       populacao[i].y = populacao[i].y + populacao[i].yVelocity
     




#####################################
#               main                #
#####################################
def main():
    #inicaliza geração
    genPopulacao()
    #calcula a  fitness da função
    #calcFitness()
    #encontra nova Geração:
    while(True):
        #verifica se encontrou objetivo
        calcFitness()  #calcula o fitness globall e o de cada particula
        state,i =verificaPopulacao()
        if(state):
            print("************** ENCONTRADO ****************")
            populacao[i].mostra()
            return 0

        #calcula velocidade das Particulas
        calcVelocidade(gbest)

        #atualiza posição das particulas de acordo com a velocidade
        attPos()


        

        print("Pass")
        for i in range(N):
            print("GeneX: %f, GeneY: %f, fitness:%f  " %(populacao[i].x, populacao[i].y, populacao[i].fitness))






if __name__ == "__main__":
    main()