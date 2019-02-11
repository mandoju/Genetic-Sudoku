import numpy as np
from copy import copy, deepcopy
#Criando uma função fitness que servirá para contar o número de espaços preenchidos corretamente
def fitness(problem, gen):

    gen_temp = deepcopy(gen)
    solution = deepcopy(problem)
    #Iremos preencher a matrix do problema com o gene
    #enumerate serve para conseguirmos pegar o index dentro do for in
    for idx,row in enumerate(solution):
        for idy,col in enumerate(row):
            if(col == 0):
                solution[idx][idy] = gen_temp.pop()
    
    #Agora possuimos a matrix solução para cálcular a quantidade de números errados que possui 
    wrong_numbers = 0
    #Primeiro iremos verificar o número de vezes que um número repete numa linha
    for row in solution:
        #esta função irá transformar a lista em um dicionario com {valor: numero de vezes que ocorreu}
        dict_count = {i:row.count(i) for i in row}
        #agora iremos percorrer o dicionário para verificar se algum valor apareceu mais de uma vez
        for key in dict_count:
            if (dict_count[key] > 1):
                wrong_numbers += dict_count[key] - 1 
    #Agora iremos verificar o número de vezes que um número repete em uma coluna
    #Para facilitar nosso trabalho iremos transpor a matriz e percorrer da mesma maneira que anteriormente
    tranposted_solution = np.array(solution).T.tolist()

    for row in tranposted_solution:
        dict_count = {i:row.count(i) for i in row}
        for key in dict_count:
            if (dict_count[key] > 1):
                wrong_numbers += dict_count[key] - 1 

    #Agora precisamos verificar se existem números repitidos nos 9 quadrados interno 3x3 que definem o sudoku
    squares = []
    #Quadrados da primeira "Coluna de 3"
    squares.append([ solution[0][0], solution[0][1], solution[0][2], solution[1][0], solution[1][1], solution[1][2], solution[2][0], solution[2][1], solution[2][2]])
    squares.append([ solution[3][0], solution[3][1], solution[3][2], solution[4][0], solution[4][1], solution[4][2], solution[5][0], solution[5][1], solution[5][2]])
    squares.append([ solution[6][0], solution[6][1], solution[6][2], solution[7][0], solution[7][1], solution[7][2], solution[8][0], solution[8][1], solution[8][2]])

    #Quadrados da segunda "Coluna de 3"
    squares.append([ solution[0][3], solution[0][4], solution[0][5], solution[1][3], solution[1][4], solution[1][5], solution[2][3], solution[2][4], solution[2][5]])
    squares.append([ solution[3][3], solution[3][4], solution[3][5], solution[4][3], solution[4][4], solution[4][5], solution[5][3], solution[5][4], solution[5][5]])
    squares.append([ solution[6][3], solution[6][4], solution[6][5], solution[7][3], solution[7][4], solution[7][5], solution[8][3], solution[8][4], solution[8][5]])

    #Quadrados da terceira "Coluna de 3"
    squares.append([ solution[0][6], solution[0][7], solution[0][8], solution[1][6], solution[1][7], solution[1][8], solution[2][6], solution[2][7], solution[2][8]])
    squares.append([ solution[3][6], solution[3][7], solution[3][8], solution[4][6], solution[4][7], solution[4][8], solution[5][6], solution[5][7], solution[5][8]])
    squares.append([ solution[6][6], solution[6][7], solution[6][8], solution[7][6], solution[7][7], solution[7][8], solution[8][6], solution[8][7], solution[8][8]])

    #contando os números repetidos da mesma maneira que o anterior
    for square in squares:
        dict_count = {i:square.count(i) for i in square}
        for key in dict_count:
            if (dict_count[key] > 1):
                wrong_numbers += dict_count[key] - 1 
    return wrong_numbers