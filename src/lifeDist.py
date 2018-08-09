'''
Created on 7 Aug 2018

@author: benos
'''
from mpLogNormal import mpLogNormal
from mpLogUniform import mpLogUniform
from mpSampleMultiple import mpSampleMultiple 
from mpSampleMultiple import sample
import numpy as np
import matplotlib.pyplot as plt
from mpmath import *


def lifeDist(times):
    size = 1000
    lamb = mpLogNormal(10 ** (-10), 10 ** (10), size, 1, 10 ** 50)
    V = mpLogUniform(10 ** (-35), 10 ** (15), size)
    t = mpLogUniform(10 ** (14), 10 ** (17), size)
    dist = [0] * times
    izpis = 0
    for i in range (0, times):
        if i % (times / 10) == 0:
            print(izpis, "% mp")
            izpis += 10
        val = 1
        val *= sample(lamb)
        val *= sample(V)
        val *= sample(t)        
        val = 1 - mp.exp(-(val))
                
        dist[int((times - 1) * val)] += 1    
    return dist

size = 1000
y = lifeDist(size)

x = mp.linspace(0, 1, size)

plt.plot(x, y)
plt.xscale("log")
plt.xlim(10**(-3) , 1)
plt.ylim(0,0000.1)
plt.show()

  
    
