# One neuron. 
# Has a 3 input neurons
import numpy as np
# Random number
inputs = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
weights = [[1,1],[1,1], [1,1], [1,1]]

# Bias of this neuron
bias = 2


dot_out = np.dot(inputs, weights)
print(dot_out)