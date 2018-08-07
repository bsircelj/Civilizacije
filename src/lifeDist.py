'''
Created on 7 Aug 2018

@author: benos
'''
from loguniform import loguniform
from lognormal import lognormal
from sampleMultiple import sampleMultiple 
from sampleMultiple import sample
import numpy as np
import matplotlib.pyplot as plt


def lifeDist(times):
    size = 1000
    lamb = lognormal(10**(-100),10**(100),size,1,10**50)
    V = lognormal(10**(-30),10**(20),size)
    t = lognormal(10**(7),10**(10),size)
    dist = [0]*times
    val = 1
    izpis = 0
    for i in range (0,times):
        if i%(times/10) == 0:
            print(izpis,"%--")
            izpis+=10
        
        val *= sample(lamb)
        val *= sample(V)
        val *= sample(t)        
        val = 1-np.exp(-(val))
                
        dist[int((times-1)*val)]+=1    
    return dist


size = 1000
y = lifeDist(size)

x = np.linspace(0,1,size)

plt.plot(x,y)
#plt.xscale("log")
plt.show()

    
    
    