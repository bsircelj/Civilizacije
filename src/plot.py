'''
Created on 13 Aug 2018

@author: benos
'''
import time
from meanMedian import meanMedian
from IO import save,readFile
import scipy.ndimage.filters as fl
import matplotlib.pyplot as plt
from createGraph import createGraph
from StandardizeDistribution import StandardizeDistributionW

(xaxis,yaxis) = readFile("sigma is 50 plus 1.csv")

yaxis = fl.gaussian_filter(yaxis, 10)

(mean,median) = meanMedian(xaxis,yaxis)

print("\nMean: ", mean, "\nMedian: ", median)

#createGraph(xaxis,yaxis,start,end,size)




plt.figure(1)

plt.subplot(4,2,1)
fromN = 0.00001
toN = 0.0001
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,2)
fromN = 0.0001
toN = 0.001
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,3)
fromN = 0.001
toN = 0.01
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,4)
fromN = 0.01
toN = 0.1
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,5)
fromN = 0.1
toN = 1
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,6)
fromN = 1
toN = 10
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,7)
fromN = 10
toN = 1000
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,8)
fromN = 1000
toN = 100000
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.tight_layout()

plt.figure(2)

#yaxis = fl.gaussian_filter(yaxis, 15)
'''
(length, xaxis, yaxis, cdf,cdfW )= StandardizeDistributionW(xaxis,yaxis)
plt.plot(xaxis,cdf,'green')
plt.plot(xaxis,cdfW,'red')
plt.title('Log Scale')
'''
plt.xscale("log")
#plt.yscale("log")
plt.ylim(0,200)

plt.plot(xaxis, yaxis,'blue')

plt.show()

