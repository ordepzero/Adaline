# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:43:35 2016

@author: PeDeNRiQue
"""

CONT_LEARNING = 0.5

def adaline(input_samples, labels,weight_samples):
    control = True
    time = 0
    while control:
        time = time + 1
        control = False
        for input_sample, label in zip(input_samples, labels):
            result = activation_function(input_sample, weight_samples)
            
            if(result != label):
                control = True
                weight_samples = update_weights(label, result, input_sample, weight_samples)
            
    
    print("Total de épocas: " + str(time))   
    print(weight_samples)
    
    test_adaline(weight_samples)


def formated_image(input_sample):
    cont = 0    
    for x in input_sample:
        if(cont > 0 and cont % 5 == 0):
            print("")
        if(x == 1):
            print("#", end='')
        else:
            print("_", end='')
        cont = cont + 1
    print("")

def activation_function(input_sample, weight_samples):
    output = 0
    output = [a*b for a,b in zip(input_sample,weight_samples)]
    
    return linear_activation_function(sum(output))

def load_and_problem():
    input_samples = [[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
    labels = [0,0,0,1]
    weight_samples = [0,0,0]
    
    return input_samples, labels, weight_samples

def load_entries_simbol_problem(filename):
    array = []
    with open(filename) as f:
    
        for line in f: # read rest of lines
            array.append([int(x) for x in line.split()])        

    entries = []
    vector = []
    
    for x in array:
    
        if(len(x) == 0):
            entries.append(vector)
            vector = []
        else:
            #print(vector)
            if(len(vector) == 0):
                vector = x
            else:
                vector = vector + x
    return entries

def load_labels_simbol_problem():
    array = []
    with open('labels.txt') as f:
        
        for line in f: # read rest of lines
            if(len(array) == 0):
                array = [int(x) for x in line.split()]
            else:
                array = array + [int(x) for x in line.split()]
    return array
    
def load_simbol_problem():
    input_samples = load_entries_simbol_problem('entry.txt')
    labels = load_labels_simbol_problem()
    weight_samples = [0] * len(input_samples[0])  
    
    print("TOTAL EXEMPLOS DE TREINO:" + str(len(input_samples)))    
    
    return input_samples, labels, weight_samples

def test_adaline(weight_samples):
    input_samples = load_entries_simbol_problem('test.txt')
    
    print("TESTANDO ADALINE")
    #print(input_samples, weight_samples)    
    
    for input_sample in input_samples:
        result = activation_function(input_sample, weight_samples)
        print("Entrada:"+ str(input_sample))
        formated_image(input_sample)
        print("Classe: "+ str(result))
    
    return 0
    
def load_samples():
    #input_samples, labels, weight_samples = load_and_problem()
    input_samples, labels, weight_samples = load_simbol_problem()
    
    #print (input_samples, labels)
    
    adaline(input_samples, labels,weight_samples)
    
        
def update_weights(label, result, input_sample, weight_samples):
    diference = label - result
    for i in range(len(weight_samples)):
        weight_samples[i] = weight_samples[i] + (CONT_LEARNING * diference * input_sample[i])
    
    return weight_samples

def linear_activation_function(value):
    if(value >= 0):
        return 1
    else:
        return -1
        
if __name__ == "__main__":
    load_samples()
    
