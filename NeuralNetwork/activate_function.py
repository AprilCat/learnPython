import numpy as np
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == "__main__":
    x = np.arange(-5, 5, 0.1)
    y = step_function(x)
    z = sigmoid(x)
    plt.plot(x, y)
    plt.plot(x, z, linestyle="--")
    plt.ylim(-0.1, 1.1)
    plt.show()
