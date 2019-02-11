import numpy as np
from copy import copy, deepcopy

#Aqui será a função que iremos fazer o crossover entre dois genes
def crossover(mother,father):

    child = deepcopy(mother)
    #print(child)
    for idx,gen in enumerate(child):
        #iremos colocar uma chance de 50% mesmo de mistura
        if(np.random.random() < 0.5 ):
            child[idx] = father[idx]
    return child