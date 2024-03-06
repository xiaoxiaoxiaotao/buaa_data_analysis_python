import numpy as np
from math import sqrt


def gaussian(x, mu, sigma):
    return np.exp(-(x-mu)**2/2*sigma**2)

def gaussian_2d(X, Y, mu, sigma):
    x,y = np.meshgrid(X, Y)
    z =np.exp(-((x - mu)**2 / sigma + (y - mu)**2 / sigma) / 2)
    return x,y,z