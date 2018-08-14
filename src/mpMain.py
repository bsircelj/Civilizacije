'''
Created on 8 Aug 2018

@author: benos
'''

from mpLogUniform import mpLogUniform
from mpLogNormal import mpLogNormal
from mpSampleMultiple import mpSampleMultiple, mpSampleMultipleTime
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from lifeDist import lifeDist
from mpmath import *
import time
from meanMedian import meanMedian
from IO import save, readFile
from mpUniform import mpUniform

size = 10000;
# size=500;

timeStart = time.time()

Rstar = mpUniform(1, 100, size)
Fplanets = mpUniform(0.1, 1, size)
Nhabitable = mpUniform(0.1, 1, size)
# Flife = lognormal(10**(-40),1,size)
# Flife = loguniform(1,1000,size)
# Flife = (0,1,lifeDist(size,size/2))
Flife = mpUniform(mpmathify(10 ** (-156)), 1, size)
Fintelligence = mpUniform(0.001, 1, size)
Fcivilization = mpUniform(0.01, 1, size)
Length = mpUniform(100, 10000000000, size)

'''
LOGUNIFORM
Rstar = mpLogUniform(1, 100, size)
Fplanets = mpLogUniform(0.1, 1, size)
Nhabitable = mpLogUniform(0.1, 1, size)
# Flife = lognormal(10**(-40),1,size)
# Flife = loguniform(1,1000,size)
#Flife = (0,1,lifeDist(size,size/2))
Flife = mpUniform(mpmathify(10**(-156)),1,size)
Fintelligence = mpLogUniform(0.001, 1, size)
Fcivilization = mpLogUniform(0.01, 1, size)
Length = mpLogUniform(100, 10000000000, size)
'''

# (xaxis, final) = sampleMultiple([Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length],size,1000)
(xaxis, final) = mpSampleMultipleTime([Rstar, Fplanets, Nhabitable, Flife, Fintelligence, Fcivilization, Length], size, 60000)
# (xaxis, final) = sampleMultiple([Flife],size,10000)

# tog = [Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length]
# (xaxis, final) = sampleMultiple(tog[0:4],size,1000)

save(xaxis, final, (time.time() - timeStart), 'All uniform in logspace')

# final = fl.gaussian_filter(final, 5)
(mean, median) = meanMedian(final, xaxis)

print("time: ", (time.time() - timeStart))
print("\nMean: ", mean, "\nMedian: ", median)
plt.plot(xaxis, final)
plt.xscale("log")
plt.show()

