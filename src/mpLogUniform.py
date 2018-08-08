'''
Created on 8 Aug 2018

@author: benos
'''

import numpy as np
import matplotlib.pyplot as plt
from mpmath import *


def mpLogUniform(low=0.01, high=1, size=10, base=np.exp(1)):
    pdf = mp.linspace(low, high, size)
    sum = mpf('0')
    for i in range(0,len(pdf)):
        pdf[i] = mpf('1.0')/(pdf[i] * (mp.log(high)- mp.log(low)))
        sum += pdf[i]
    return  (low,high,[x/sum for x in pdf])


