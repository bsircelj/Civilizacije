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
from mpLogspace import mpLogspace

dist = mpLogUniform(0.1,1,1000)

sampledDist = ...


x = mpLogspace(dist[0],dist[1])
plt.subplot()

plt.subplot(2,1,2)
plt.plot(xS,yS)


