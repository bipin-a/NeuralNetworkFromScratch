# Three neurons with 4 inputs.
import numpy as np

# Layer 1:
# Input: 3x4, Neurons: 3
inputs = [[1, 2, 3, 2.5],
        [2.0, 5.0, -1.0, 2.0],
        [-1.5, 2.7, 3.3, -0.8]]
weights = [ [0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87] ]
biases = [2, 3, 0.5]

# Layer 2: 
# Input: 3x3, Neurons: 3
weights2 = [ [0.1, -0.14, 0.5], [-0.5, 0.12, -0.33], [-0.44, 0.73, -0.13]]
# Removed one neruon per weight, because the input is now 3x3.
biases2 = [-1, 2, -0.5]
        
layer1_outputs = np.dot(inputs,np.array(weights).T) + biases    #Outputs 3x3
layer2_outputs = np.dot(layer1_outputs,np.array(weights2).T) + biases2

print (layer2_outputs)



# Old Fashion Method
'''
output_layer = []
for n_weights, n_bias in zip(weights, biases):
    n_output = 0
    for input, weight in zip(inputs, n_weights):      
        n_output += input*weight 
    n_output += n_bias
    output_layer.append(n_output)
print(output_layer)
'''