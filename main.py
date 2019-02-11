import numpy as np
from fitness import fitness #função para calcular o fitness
from crossover import crossover #função que irá fazer o crossover entre dois genes
from mutation import mutation

population_size = 100
mutation_rate = 0.10
epochs = 10 #quantidade de épocas
#Váriavel para definir o problema, os espaços vazios serão definidos como 0
problem = []
#Adicionando a primeira linha do problema
problem.append([5,3,0,0,7,0,0,0,0])
#Adicionando a segunda linha do problema
problem.append([6,0,0,1,9,5,0,0,0])
#Por ai vai
problem.append([0,9,8,0,0,0,0,6,0])

problem.append([8,0,0,0,6,0,0,0,3])
problem.append([4,0,0,8,0,3,0,0,1])
problem.append([7,0,8,0,2,0,0,0,6])

problem.append([0,6,0,0,0,0,2,8,0])
problem.append([0,0,0,4,1,9,0,0,5])
problem.append([0,0,0,0,8,0,0,7,9])


#Definindo o tamanho dos genes (basicamente contando o números de espaços vazios)
gen_size = 0
for row in problem:
    for col in row:
        if(col == 0):
            gen_size += 1

#criando os genes para preencher o sudoku
gens = []

for i in range(population_size):
    #np.random.randint(10, size=gen_size) cria um array de inteiros de 0 a 10
    gens.append(np.random.randint(1,high=10, size=gen_size).tolist())

for i in range(100):
    #calculando os fitness de cada gen
    fitness_list = []
    for gen in gens: 
        fitness_list.append(fitness(problem,gen))
    #escolhendo os dois melhores gens
    #iremos transformar em um numpy array para facilitar nosso trabalho
    fitness_list = np.array(fitness_list)
    #agora iremos pegar os indices dos 2 menores valores

    lowest_indexes = np.argpartition(fitness_list, 2)

    first_best_fitness = fitness_list[lowest_indexes[0]]
    second_best_fitness = fitness_list[lowest_indexes[1]]

    #print(gens)

    first_lowest_gen = gens[lowest_indexes[0]][:]
    second_lowest_gen = gens[lowest_indexes[1]][:]
    #print(gens)
    #print(fitness_list)
    #print(gens[lowest_indexes[0]])
    #print(second_lowest_gen)

    new_gens = []
    new_gens.append(first_lowest_gen)
    new_gens.append(second_lowest_gen)
    for i in range(population_size - 2):
        #iremos criar um gene que é a mutação do crossover entre o pai e a mãe
        #ou  seja: cria um crossover entre pai e a mãe e depois resolve a mutação
        #print(first_lowest_gen)
        new_gens.append( mutation( crossover(first_lowest_gen,second_lowest_gen), mutation_rate) )

    print("erros do melhor: " + str(first_best_fitness))
    print("erros do segundo melhor: " + str(second_best_fitness))
    gens = new_gens
    #print(problem)
print("Fim")
print("erros: "  + str(first_best_fitness))
print("solução: ")
print( str(first_lowest_gen))