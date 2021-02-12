from random import random

import numpy as np

cond_table = {}
cond_table[0] = [[], [0.5]]
cond_table[1] = [[], [0.5]]
cond_table[2] = [[0], [0.01, 0.2]]
cond_table[3] = [[1], [0.02, 0.75]]
cond_table[4] = [[1], [0.03, 0.92]]
cond_table[5] = [[2, 3], [0, 1, 1, 1]]
cond_table[6] = [[5], [0.04, 0.885]]
cond_table[7] = [[4, 5], [0.89, 0.89, 0.96, 0.96]]


def simulate(n, true_indices=[], false_indices=[]):
    totals = np.zeros(8)
    valid_sims = 0
    for i in range(n):
        results = np.zeros(8)
        for j in range(8):
            if cond_table[j][0] == []:
                comp_num = cond_table[j][1][0]
            else:
                k = 0
                for h in range(len(cond_table[j][0])):
                    k += results[cond_table[j][0][h]] * (2**h)
                comp_num = cond_table[j][1][int(k)]
            if random() < comp_num:
                results[j] = 1
        if results_valid(results, true_indices, false_indices):
            totals += results
            valid_sims += 1
    if valid_sims > 0:
        return totals / valid_sims
    else:
        print('No Valid Sims found')


def results_valid(results, true_indices, false_indices):
    if np.all(results[true_indices] == 1) and np.all(results[false_indices] == 0):
        return True
    else:
        return False
