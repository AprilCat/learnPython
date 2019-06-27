import numpy as np
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def ReLU(x):
    return np.maximum(0, x)


if __name__ == "__main__":
    x = np.arange(-5, 5, 0.1)
    y1 = step_function(x)
    y2 = sigmoid(x)
    y3 = ReLU(x)
    plt.plot(x, y1)
    plt.plot(x, y2, linestyle="--", color="red")
    plt.plot(x, y3)
    plt.ylim(-0.1, 1.1)
    plt.show()
