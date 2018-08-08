'''
Created on 7 Aug 2018

@author: benos
'''
from mpLogNormal import mpLogNormal
from sampleMultiple import sampleMultiple 
from sampleMultiple import sample
import numpy as np
import matplotlib.pyplot as plt


def lifeDist(times):
    size = 1000
    lamb = mpLogNormal(10 ** (-100), 10 ** (100), size, 1, 10 ** 9.99)
    V = mpLogNormal(10 ** (-30), 10 ** (20), size)
    t = mpLogNormal(10 ** (7), 10 ** (10), size)
    dist = [0] * times
    val = 1
    izpis = 0
    for i in range (0, times):
        if i % (times / 10) == 0:
            print(izpis, "% mp")
            izpis += 10
        
        val *= sample(lamb)
        val *= sample(V)
        val *= sample(t)        
        val = 1 - np.exp(-(val))
                
        dist[int((times - 1) * val)] += 1    
    return dist


#size = 1000
#y = lifeDist(size)

#x = np.linspace(0, 1, size)

#plt.plot(x, y)
# plt.xscale("log")
#plt.show()
    
    
