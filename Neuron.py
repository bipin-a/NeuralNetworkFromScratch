# One neuron. 
# Has a 4 input neurons
import numpy as np
# Random number
inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]

# Bias of this neuron
bias = 2


dot_out = np.dot(inputs, weights) + bias
print(dot_out)