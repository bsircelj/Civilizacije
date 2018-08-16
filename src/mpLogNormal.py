'''
Created on 8 Aug 2018

@author: benos
'''
import numpy as np
from math import *
from mpmath import *
import matplotlib.pyplot as plt
mp.dps = 200
from mpLogspace import mpLogspace

def mpLogNormal(low=mpmathify(10**(-188)), high=mpmathify(10**12), size=100000, median=mpmathify(1.0), sigma=mpmathify(10**50) ):
    x = mpLogspace(low, high, size)
    pdf = mp.linspace(1, size, size)
    mu = mp.log(median)
    sum = mpf('0')
    for i in range(0,len(pdf)):
        pdf[i] = (mp.exp(-(mp.log(x[i]) - mu) ** 2 / (2 * sigma * sigma )) / ( x[i] * sigma * mp.sqrt(2 * mp.pi)))
        sum += pdf[i]

    for i in range(0,len(pdf)):
        pdf[i] = pdf[i] / sum


    return (low, high, pdf)
    
    

'''
x = np.logspace(-188, 12, 100000)
pdf=mpLogNormal()[2]

plt.plot(x, pdf, linewidth=2, color='r')
plt.xscale('log')
plt.show()
'''

