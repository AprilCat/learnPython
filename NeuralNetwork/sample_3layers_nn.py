from NeuralNetwork.activate_function import identical_function,sigmoid
import numpy as np


def init_network():
    network = {}
    network["W1"] = np.array([[1.1, 1.2], [1.3, 1.4], [1.5, 1.6]])
    network["b1"] = np.array([0.1, 0.1, 0.1])
    network["W2"] = np.array([[2.1, 2.2, 2.3], [2.4, 2.5, 2.6]])
    network["b2"] = np.array([0.2, 0.2])
    network["W3"] = np.array([[3.1, 3.2], [3.3, 3.4]])
    network["b3"] = np.array([0.3, 0.3])
    return network


def forward(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]
    a1 = np.dot(W1, x) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(W2, z1) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(W3, z2) + b3
    z3 = identical_function(a3)
    return z3



if __name__ == "__main__":
    network = init_network()
    print(forward(network, np.array([2, 4])))
