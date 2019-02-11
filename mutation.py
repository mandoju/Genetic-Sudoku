import numpy as np
from copy import copy, deepcopy

#Função para mutar um gene;
def mutation(gen, mutationRate):
    result = deepcopy(gen)
    
    for idx,val in enumerate(result):
        if(np.random.random() < mutationRate ):
            result[idx] = np.random.randint(10)
    return result