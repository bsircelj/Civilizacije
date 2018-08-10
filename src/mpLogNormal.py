'''
Created on 8 Aug 2018

@author: benos
'''
import numpy as np
from math import *
#from scipy import mpmath
from mpmath import *
import matplotlib.pyplot as plt
mp.dps = 5
from mpLogspace import mpLogspace

def mpLogNormal(low=0.000000000000000000001, high=1, size=1000, median=1.0, sigma=mpmathify(10**50) ):
    low = mpmathify(10**(-188))
    high = mpf('1.0')
    mu = mp.log(median, e)
    mu = mpf('1')
    
    #import matplotlib.pyplot as plt

    '''
    lahko to uporabis
    newList = [x / myInt for x in myList]
    
    
    
    pdf = (mp.exp(-(mp.log(x) - mu) ** 2 / (2 * sigma ** 2))
           / (x * sigma * mp.sqrt(2 * mp.pi)))
    

    return (min, max, pdf)
    '''
    pdf = mpLogspace(low, high, size)
    #summ = mpf('0')
    for i in range(0,len(pdf)):
        #pdf[i] = mpf('1.0')/(pdf[i] * (mp.log(high)- mp.log(low)))
        pdf[i] = (mp.exp(-(mp.log(pdf[i]) - mu) ** 2 / (2 * sigma * sigma )) / (pdf[i] * sigma * mp.sqrt(2 * mp.pi)))
        #summ = mp.fadd(summ,pdf[i])
    return  (low,high,[x/mp.fsum(pdf) for x in pdf])
'''
size = 1000
x = mp.linspace(mpf('10')**(-188) , mpf('1'), size)
lamb = mpLogNormal( mpf('10')**(-188) , mpf('1'), size, mpf('1'), mpf('10')**50 )
print(x)
print(lamb)
low = mpf('10') ** (-188)
print(low)

'''
'''
size = 10
low = mpmathify(mpf('10')**(-188))
high = mpf('1.0')
x = mp.linspace(mp.log(low) , mp.log(high), size)
x = [ mp.exp(kos) for kos in x]
lamb = mpLogNormal( mp.log(mpf('10')**(-188)) , mp.log(mpf('1')), size, mpf('1'), mpmathify(10**50) )[2]
print(x)
print(lamb)
plt.plot(x, lamb)
plt.xscale('log')
plt.xlim(10**(-188),1)
plt.show()
#plot(lamb, xlim=[low, high])

'''

