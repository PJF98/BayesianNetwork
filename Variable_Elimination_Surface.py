import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Factor_Class import Factor, Factor_List

x = np.arange(0.0, 1.0, 0.01)
probs = np.zeros([100, 100])

for i in range(100):
    for j in range(100):
        factors = Factor_List([])
        factors.factors.append(Factor([0], [x[i], 1-x[i]]))
        factors.factors.append(Factor([1], [x[j], 1-x[j]]))
        factors.factors.append(Factor([0, 2], [[0.99, 0.01], [0.8, 0.2]]))
        factors.factors.append(Factor([1, 3], [[0.98, 0.02], [0.25, 0.75]]))
        factors.factors.append(Factor([1, 4], [[0.97, 0.03], [0.08, 0.92]]))
        factors.factors.append(Factor([2, 3, 5], [[[1, 0], [0, 1]], [[0, 1], [0, 1]]]))
        factors.factors.append(Factor([5, 6], [[0.96, 0.04], [0.115, 0.885]]))
        factors.factors.append(Factor([4, 5, 7], [[[0.11, 0.89], [0.11, 0.89]], [[0.04, 0.96], [0.04, 0.96]]]))
        probs[i][j] = factors.find_node_probability(5)

X, Y = np.meshgrid(x, x)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, probs)
ax.set_xlabel('Probability of Travel To Asia')
ax.set_ylabel('Probability of Smoking')
ax.set_zlabel('Probability of Tuberculosis or Cancer')

plt.show()
