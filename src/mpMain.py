'''
Created on 8 Aug 2018

@author: benos
'''

from mpLogUniform import mpLogUniform
from mpLogNormal import mpLogNormal
from mpSampleMultiple import mpSampleMultiple
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
import openturns as ot
from lifeDist import lifeDist
from openturns.viewer import View
from mpmath import *

size = 1000;


Rstar = mpLogUniform(1,100,size)
Fplanets = mpLogUniform(0.1,1,size)
Nhabitable = mpLogUniform(0.1,1,size)
#Flife = lognormal(10**(-40),1,size)
#Flife = loguniform(1,1000,size)
#Flife = (0,1,lifeDist(size))
Fintelligence = mpLogUniform(0.001,1,size)
Fcivilization = mpLogUniform(0.01,1,size)
Length = mpLogUniform(100,10000000000,size)

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


#(xaxis, final) = sampleMultiple([Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length],size,1000)
(xaxis, final) = mpSampleMultiple([Rstar,Fplanets,Nhabitable,Fintelligence,Fcivilization,Length],size,10000)

#(xaxis, final) = sampleMultiple([Flife],size,10000)


#tog = [Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length]
#(xaxis, final) = sampleMultiple(tog[0:4],size,1000)


final = fl.gaussian_filter(final,5)
mean = 0
sum = 0
median = [0]*size
sumNo = 0
for p in range(1,len(final)):
    print(xaxis[p]," - ",final[p])
    mean += p*final[p]*(xaxis[p]-xaxis[p-1])
    sum += final[p]*(xaxis[p]-xaxis[p-1])
    if final[p]!=0 :
        median[sumNo]=xaxis[p]
        sumNo+=1


print("\nMean: ",xaxis[int(mean/sum)],"\nMedian: ",median[int(sumNo/2)])
plt.plot(xaxis,final)
plt.xscale("log")
plt.show()




