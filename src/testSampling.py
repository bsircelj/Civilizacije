'''
Created on 14 Aug 2018

@author: benos
'''
import time
from meanMedian import meanMedian
from IO import save,readFile
import scipy.ndimage.filters as fl
import matplotlib.pyplot as plt
from createGraph import createGraph
from mpLogUniform import mpLogUniform
from mpSampleMultiple import *
from mpLogspace import mpLogspace

size = 1000

dist = mpLogUniform(0.1,1,size)
x = mpLogspace(dist[0],dist[1],size)
#plt.subplot(2,1,1)
plt.plot(x,dist[2])


times = 1000


yS = [0]*size
for i in range(0,times):
    val = sampleByBisection(StandardiseDistribution(dist))
    #val = sample(dist)
    
    for p in range(0,size):
        if x[p]<val:
            yS[p]+=1
            
yS = [x/sum(yS) for x in yS]
    


#plt.subplot(2,1,2)
plt.plot(x,yS)

plt.show()


