import numpy as np

from Pomegranate import create_network
from Variable_Elimination import create_ve_network
from Simulation import simulate

pom_network = create_network()
ve_network = create_ve_network()

pom_probs = []
beliefs = pom_network.predict_proba({})
for state, belief in zip(pom_network.states, beliefs):
    pom_probs.append((state.name, round(belief.parameters[0]['T'], 5)))

ve_probs = []
probs = [ve_network.find_node_probability(i) for i in range(8)]
for state, prob in zip(pom_network.states, probs):
    ve_probs.append((state.name, round(prob, 5)))

sim_probs = []
probs = simulate(10000)
for state, prob in zip(pom_network.states, probs):
    sim_probs.append((state.name, prob))

print()
print('Output with no fixed input values')
print()
print('Probabilites from Pomegranate Network:')
print()
print(pom_probs)
print()
print('Probabilities from Variable Elimination from scratch:')
print()
print(ve_probs)
print()
print('Probabilities from Brute Force Simulation:')
print()
print(sim_probs)


pom_probs = []
fixed = {'travel_to_asia': 'T', 'smoking': 'F'}
beliefs = pom_network.predict_proba(fixed)
for state, belief in zip(pom_network.states, beliefs):
    if state.name not in fixed:
        pom_probs.append((state.name, round(belief.parameters[0]['T'], 5)))


sim_probs = []
probs = simulate(10000, [0], [1])
for state, prob in zip(pom_network.states, probs):
    if state.name not in fixed:
        sim_probs.append((state.name, round(prob, 5)))

print()
print('Output given travel to asia is true and smoking is false')
print()
print('Probabilites from Pomegranate Network:')
print()
print(pom_probs)
print()
print('Probabilities from Brute Force Simulation:')
print()
print(sim_probs)
