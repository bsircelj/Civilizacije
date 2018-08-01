'''
Created on 31 Jul 2018

@author: benos
'''
import loguniform as loguniform
import lognormal as lognormal
import sampleMultiple as sampleMultiple
import numpy as np
import matplotlib as plt

size = 1000;

Rstar = loguniform(1,100,size)
Fplanets = loguniform(0.1,1,size)
Nhabitable = loguniform(0.1,1,size)
Flife = lognormal(1,100,size)
Fintelligence = loguniform(0.001,1,size)
Fcivilization = loguniform(0.01,1,size)
Length = loguniform(100,10000000000,size)

final = sampleMultiple([Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length])


