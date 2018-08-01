import numpy as np


def loguniform(low=0.001, high=1, size=10, base=np.exp(1)):
    pdf = np.linspace(low, high, size)
    pdf = 1/(pdf * (np.log(high)- np.log(low)))
    return  pdf