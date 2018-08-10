'''
Created on 8 Aug 2018

@author: benos
'''

from mpLogUniform import mpLogUniform
from mpLogNormal import mpLogNormal
from mpSampleMultiple import mpSampleMultiple,mpSampleMultipleTime
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from lifeDist import lifeDist
from mpmath import *
import time
from meanMedian import meanMedian
from IO import save,readFile

size = 1000;

timeStart = time.time()

Rstar = mpLogUniform(1, 100, size)
Fplanets = mpLogUniform(0.1, 1, size)
Nhabitable = mpLogUniform(0.1, 1, size)
# Flife = lognormal(10**(-40),1,size)
# Flife = loguniform(1,1000,size)
Flife = (0,1,lifeDist(size))
Fintelligence = mpLogUniform(0.001, 1, size)
Fcivilization = mpLogUniform(0.01, 1, size)
Length = mpLogUniform(100, 10000000000, size)

'''
Rstar = ot.LogUniform(1,100)
graph = Rstar.drawPDF()

graph.setLogScale(ot.GraphImplementation.LOGX)
view = View(graph, plot_kwargs={'color':'blue'})
view.save('curve.png', dpi=100)
view.show()

Fplanets = ot.LogUniform(0.1,1)
Nhabitable = ot.LogUniform(0.1,1)
#Flife = ot.lognormal(10**(-200),1)
Flife = ot.LogUniform(1,1000)
Fintelligence = ot.LogUniform(0.001,1)
Fcivilization = ot.LogUniform(0.01,1)
Length = ot.LogUniform(100,10000000000)

'''

# (xaxis, final) = sampleMultiple([Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length],size,1000)
(xaxis, final) = mpSampleMultipleTime([Rstar, Fplanets, Nhabitable,Flife, Fintelligence, Fcivilization, Length], size, 10)
# (xaxis, final) = sampleMultiple([Flife],size,10000)

# tog = [Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length]
# (xaxis, final) = sampleMultiple(tog[0:4],size,1000)

save(xaxis,final,(time.time() - timeStart),'test')

final = fl.gaussian_filter(final, 5)
(mean, median) = meanMedian(final, xaxis)

print("time: ", (time.time() - timeStart))
print("\nMean: ", mean, "\nMedian: ", median)
plt.plot(xaxis, final)
plt.xscale("log")
plt.show()

