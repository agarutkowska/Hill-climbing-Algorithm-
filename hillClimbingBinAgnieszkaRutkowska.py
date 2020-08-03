# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:42:34 2020

@author: arutk
"""

import random
import copy
import numpy as np
import matplotlib.pyplot as plt

def open_file(file_name):
    with open(file_name) as file:
        no_elements = int(file.readline())
        bin_size = int(file.readline())
        elements_sizes = []

        for i in range(no_elements):
            value = int(file.readline())
            elements_sizes.append(value)

    return no_elements, bin_size, elements_sizes

def hill_climbing_bin(
        no_elements, bin_size, 
        elements_sizes):
    x = random.sample(range(0, no_elements), no_elements)
    eval_values = []
    eval_x = eval_function(x, no_elements, 
                           bin_size, elements_sizes)
    eval_values.append(eval_x)
    no_iter = 0
    index = 0
    while index < maximum:
        x_n = neighbour(x, no_elements)
        eval_n = eval_function(x_n, no_elements, 
                               bin_size, elements_sizes)
        if eval_n <= eval_x:
            x = x_n
            eval_x = eval_n
            eval_values.append(eval_x)
            no_iter += 1
        index += 1
    return x, eval_x, eval_values, no_iter

def eval_function(
        vector_x, no_elements, bin_size, 
        elements_sizes):
    unique_x = np.unique(vector_x)
    no_unique_bins = len(unique_x)
    sum_bin = fun_sum_bin(vector_x, unique_x, 
                          bin_size, elements_sizes)
    eval_value = no_unique_bins + is_solution_not_correct(sum_bin) * (no_elements + sum_bin)
    return eval_value
    
def fun_sum_bin(
        vector_x, unique_x, bin_size, 
        elements_sizes):
    sum_bin = 0
    for i in unique_x:
        indeces = []
        for j in range(len(vector_x)):
            if vector_x[j] == i:
                indeces.append(j)
        weights_sum = 0
        for elem in indeces:
            weights_sum += elements_sizes[elem]
        sum_bin += max(0, (weights_sum - bin_size))
    return sum_bin

def is_solution_not_correct(sum_bin):
    result = 1
    if sum_bin > 0:
        return result
    else:
        result = 0
        return result
        
def neighbour(vector_x, no_elements):
    position_in_x = random.randint(0,(no_elements-1))
    new_vector_x = copy.copy(vector_x)
    while True:
        candidate_value = random.randint(0,(no_elements-1)) 
        if(candidate_value != new_vector_x[position_in_x]):
            new_vector_x[position_in_x] = candidate_value
            break
    return new_vector_x

def show_bin_weights(vector_x, elements_sizes):
    unique_x = np.unique(vector_x)
    bin_weights = {}
    for i in unique_x:
        indexes = []
        for j in range(len(vector_x)):
            if vector_x[j] == i:
                indexes.append(j)
        weights_sum = 0
        for elem in indexes:
            weights_sum += elements_sizes[elem]
        bin_weights[i] = weights_sum
    return bin_weights

def main():
    for file_name in file_names:
        print(f'File name: {file_name}')
        data = open_file(file_name)
        fmin_values = []
        for i in range(10):
            x, eval_x, eval_values, no_iter = hill_climbing_bin(data[0], data[1], 
                                                             data[2])                     
            fmin_values.append(eval_x)
            print(f'\nNo. of iteration of the solution: {i + 1}')
            print(f'Number of bins: {len(np.unique(x))}')
            print(f'Value of Min Function: {eval_x}')
            print(f'\nVektor x after optimalization: {x}')
            print(f'\nBin weights: {show_bin_weights(x, data[2])}')
            
            x = range(no_iter + 1)
            plt.plot(x, eval_values)
            graph_title = f'Graph f_min against index. File: {file_name}. Trial number: {i + 1}.'
            plt.title(graph_title)
            plot_name = f'./graphs/{file_name}_{i}.png'
            plt.savefig(plot_name)
            plt.show()
        
        mean = np.mean(fmin_values)
        std = np.std(fmin_values)
        
        print(f'\nMean: {mean} Standard devation: {std}\n\n')

if __name__ == "__main__":
    file_names = ['24_N1C2W2_D.txt', '25_N1C1W1_A.txt', '43_N2C3W2_B.txt', '46_N2C1W1_M.txt']
    maximum = 1000

    main()
