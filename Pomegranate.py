import numpy as np
import pomegranate as pm

def create_network():

    travel_to_asia = pm.DiscreteDistribution({'T': 0.5, 'F': 0.5})

    smoking = pm.DiscreteDistribution({'T': 0.5, 'F': 0.5})

    tuberculosis = pm.ConditionalProbabilityTable(
        [['T', 'T', 0.2],
         ['T', 'F', 0.8],
         ['F', 'T', 0.01],
         ['F', 'F', 0.99]], [travel_to_asia])

    lung = pm.ConditionalProbabilityTable(
        [['T', 'T', 0.75],
         ['T', 'F', 0.25],
         ['F', 'T', 0.02],
         ['F', 'F', 0.98]], [smoking])

    bronchitis = pm.ConditionalProbabilityTable(
        [['T', 'T', 0.92],
         ['T', 'F', 0.08],
         ['F', 'T', 0.03],
         ['F', 'F', 0.97]], [smoking])

    tuberculosis_or_cancer = pm.ConditionalProbabilityTable(
        [['T', 'T', 'T', 1],
         ['T', 'T', 'F', 0],
         ['T', 'F', 'T', 1],
         ['T', 'F', 'F', 0],
         ['F', 'T', 'T', 1],
         ['F', 'T', 'F', 0],
         ['F', 'F', 'T', 0],
         ['F', 'F', 'F', 1]], [tuberculosis, lung])

    xray = pm.ConditionalProbabilityTable(
        [['T', 'T', 0.885],
         ['T', 'F', 0.115],
         ['F', 'T', 0.04],
         ['F', 'F', 0.96]], [tuberculosis_or_cancer])

    dyspnea = pm.ConditionalProbabilityTable(
        [['T', 'T', 'T', 0.96],
         ['T', 'T', 'F', 0.04],
         ['T', 'F', 'T', 0.89],
         ['T', 'F', 'F', 0.11],
         ['F', 'T', 'T', 0.96],
         ['F', 'T', 'F', 0.04],
         ['F', 'F', 'T', 0.89],
         ['F', 'F', 'F', 0.11]], [tuberculosis_or_cancer, bronchitis])

    d1 = pm.State(travel_to_asia, name='travel_to_asia')
    d2 = pm.State(smoking, name='smoking')
    d3 = pm.State(tuberculosis, name='tuberculosis')
    d4 = pm.State(lung, name='lung')
    d5 = pm.State(bronchitis, name='bronchitis')
    d6 = pm.State(tuberculosis_or_cancer, name='tuberculosis_or_cancer')
    d7 = pm.State(xray, name='xray')
    d8 = pm.State(dyspnea, name='dyspnea')

    network = pm.BayesianNetwork('Estimating Probability of Dyspnea')
    network.add_states(d1, d2, d3, d4, d5, d6, d7, d8)
    edges = [[d1, d3], [d2, d4], [d2, d5], [d3, d6],
             [d4, d6], [d6, d7], [d6, d8], [d5, d8]]
    for edge in edges:
        network.add_edge(edge[0], edge[1])
    network.bake()

    return network
