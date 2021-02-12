import numpy as np
from Factor_Class import Factor, Factor_List

def create_ve_network():

    factors = Factor_List([])
    factors.factors.append(Factor([0], [0.5, 0.5]))
    factors.factors.append(Factor([1], [0.5, 0.5]))
    factors.factors.append(Factor([0, 2], [[0.99, 0.01], [0.8, 0.2]]))
    factors.factors.append(Factor([1, 3], [[0.98, 0.02], [0.25, 0.75]]))
    factors.factors.append(Factor([1, 4], [[0.97, 0.03], [0.08, 0.92]]))
    factors.factors.append(Factor([2, 3, 5], [[[1, 0], [0, 1]], [[0, 1], [0, 1]]]))
    factors.factors.append(Factor([5, 6], [[0.96, 0.04], [0.115, 0.885]]))
    factors.factors.append(Factor([4, 5, 7], [[[0.11, 0.89], [0.11, 0.89]], [[0.04, 0.96], [0.04, 0.96]]]))

    return factors
