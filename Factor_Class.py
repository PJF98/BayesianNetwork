from itertools import product

import numpy as np


class Factor:
    def __init__(self, nodes, probs):
        self.nodes = np.array(nodes)
        self.probs = np.array(probs)


class Factor_List:
    
    def __init__(self, factors):
        self.factors = factors

    def find_node_ordering(self, target_node):
        all_nodes = np.concatenate([f.nodes for f in self.factors])
        unique = np.unique(all_nodes, return_counts=True)
        ordering = unique[0][np.argsort(unique[1])]
        return np.delete(ordering, ordering == target_node)

    def find_node_probability(self, target_node):
        self.red_factors = self.factors.copy()
        nodes = self.find_node_ordering(target_node)
        for node in nodes:
            factors_to_combine = []
            for factor in self.red_factors:
                if node in factor.nodes:
                    factors_to_combine.append(factor)
            for factor in factors_to_combine:
                self.red_factors.remove(factor)
            combined_factor = self.combine_factors(factors_to_combine)
            reduced_factor = self.reduce_factor(combined_factor, node)
            self.red_factors.append(reduced_factor)
        result = np.prod([i.probs[1] for i in self.red_factors])
        return result
    
    def combine_factors(self, ftc):
        if len(ftc) > 1:
            nodes = np.concatenate([f.nodes for f in ftc])
            nodes = np.sort(np.unique(nodes))
            dic = {}
            for i in range(len(nodes)):
                dic[nodes[i]] = i
            probs = np.ones([2]*len(nodes))
            for prod in product((0, 1), repeat=len(nodes)):
                for factor in ftc:
                    mult = factor.probs[tuple([prod[dic[i]] for i in factor.nodes])]
                    probs[prod] *= mult
            factor = Factor(nodes, probs)
        else:
            factor = ftc[0]
        return factor

    def reduce_factor(self, factor, node):
        probs = np.sum(factor.probs, axis=np.where(factor.nodes == node)[0][0])
        nodes = np.delete(factor.nodes, factor.nodes == node)
        return Factor(nodes, probs)
