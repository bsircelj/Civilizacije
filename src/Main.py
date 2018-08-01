'''
Created on 31 Jul 2018

@author: benos
'''
from loguniform import loguniform
from lognormal import lognormal
from sampleMultiple import sampleMultiple
import numpy as np
import matplotlib.pyplot as plt

size = 1000;

Rstar = loguniform(1,100,size)
Fplanets = loguniform(0.1,1,size)
Nhabitable = loguniform(0.1,1,size)
Flife = lognormal(0.00000001,1,size)
Fintelligence = loguniform(0.001,1,size)
Fcivilization = loguniform(0.01,1,size)
Length = loguniform(100,10000000000,size)

final = sampleMultiple([Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length],size,1000)

plt.plot(final)
plt.show()


