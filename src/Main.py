'''
Created on 31 Jul 2018

@author: benos
'''
from loguniform import loguniform
from lognormal import lognormal
from sampleMultiple import sampleMultiple
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl

size = 1000;

Rstar = loguniform(1,100,size)
Fplanets = loguniform(0.1,1,size)
Nhabitable = loguniform(0.1,1,size)
Flife = lognormal(10**(-200),1,size)
#Flife = loguniform(1,1000,size)
Fintelligence = loguniform(0.001,1,size)
Fcivilization = loguniform(0.01,1,size)
Length = loguniform(100,10000000000,size)

(xaxis, final) = sampleMultiple([Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length],size,1000)
#(xaxis, final) = sampleMultiple([Rstar,Fplanets,Nhabitable,Fintelligence,Fcivilization,Length],size,1000)


#tog = [Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length]
#(xaxis, final) = sampleMultiple(tog[0:4],size,1000)


final = fl.gaussian_filter(final,5)
mean = 0
sum = 0
for p in range(1,len(final)):
    print(xaxis[p]," - ",final[p])
    mean += p*final[p]
    sum += final[p]


print("\nMean: ",xaxis[int(mean/sum)])
plt.plot(xaxis,final)
plt.xscale("log")
plt.show()




