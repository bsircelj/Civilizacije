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
from mpmath import mpmathify,mp,mpf
from logHistogramAdd import logHistogramAdd


def lifeDist(size, times):
    #size = 1000
    # mpmathify(10**(-188))
    #lamb = mpLogNormal(mpmathify(10 ** (-10)), mpmathify(10 ** (10)), size, 1, mpmathify(10 ** 50))
    lamb = mpLogNormal(size=size)
    #lamb = mpLogUniform(mpmathify(10 ** (-188)), mpmathify(10 ** (12)), size)
    V = mpLogUniform(mpmathify(10 ** (-35)), mpmathify(10 ** (15)), size)
    t = mpLogUniform(mpmathify(10 ** (14)), mpmathify(10 ** (17)), size)
    dist = [0] * times
    izpis = 0
    mp.dps = 230
    for i in range (0, times):
        if i % (times / 10) == 0:
            print(izpis, "% lifeDist")
            izpis += 10
        val = mpf('1')
        val *= sample(lamb)
        val *= sample(V)
        val *= sample(t)
        val = 0-val
        expo = mp.exp(val)        
        val = mpf('1') - expo
        #print(val)
        
        start = -220
        end = 10
        
        dist = logHistogramAdd(start, end, times, dist, val)
        #dist[int((times - 1) * val)] += 1  # 10^-190 -> 10^10 
    mp.dps = 15
    return [ x/mp.fsum(dist) for x in dist]
'''
size = 1000
y = lifeDist(size)

x = mp.linspace(0, 1, size)

plt.plot(x, y)
plt.xscale("log")
plt.xlim(10**(-3) , 1)
plt.ylim(0,0000.1)
plt.show()
'''
    
