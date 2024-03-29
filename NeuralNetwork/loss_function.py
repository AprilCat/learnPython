from math import log
import numpy as np


def mean_squared_error(y, t):
    return 0.5*np.sum((y - t)**2)


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * log(y + delta))


