import numpy as np


def softmax(a):
    max_a = np.max(a)
    exp_a = np.exp(a - max_a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


if __name__ == "__main__":
    a = np.array([2000, 2001, 2002])
    print(softmax(a))
    print(np.sum(softmax(a)))
