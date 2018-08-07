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
import openturns as ot
from openturns.viewer import View

size = 1000;


Rstar = loguniform(1,100,size)
Fplanets = loguniform(0.1,1,size)
Nhabitable = loguniform(0.1,1,size)
Flife = lognormal(10**(-200),1,size)
#Flife = loguniform(1,1000,size)
Fintelligence = loguniform(0.001,1,size)
Fcivilization = loguniform(0.01,1,size)
Length = loguniform(100,10000000000,size)

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


(xaxis, final) = sampleMultiple([Rstar,Fplanets,Nhabitable,Flife,Fintelligence,Fcivilization,Length],size,1000)
#(xaxis, final) = sampleMultiple([Rstar,Fplanets,Nhabitable,Fintelligence,Fcivilization,Length],size,1000)


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




