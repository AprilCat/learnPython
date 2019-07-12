import sys, os
import numpy as np
import pickle
from PIL import Image
from math import sqrt
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from NeuralNetwork.activate_function import sigmoid, softmax

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y



x, t = get_data()
networtk = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(networtk, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1
print("Accuracy:%f" % (accuracy_cnt/len(x)))

accuracy_cnt = 0
batch_size = 100
for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(networtk, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])
print("batch accuracy:%f" % (accuracy_cnt/len(x)))

