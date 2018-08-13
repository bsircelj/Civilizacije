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

(xaxis,final) = readFile("firstTry.csv")

final = fl.gaussian_filter(final, 200)

(mean,median) = meanMedian(xaxis,final)

#print("\nMean: ", mean, "\nMedian: ", median)

#createGraph(xaxis,yaxis,start,end,size)


plt.figure(1)
plt.title('Log Scale')
plt.xscale("log")
plt.plot(xaxis, final)

plt.figure(2)

plt.subplot(4,2,1)
fromN = 0.00001
toN = 0.0001
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,final,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,2)
fromN = 0.0001
toN = 0.001
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,final,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,3)
fromN = 0.001
toN = 0.01
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,final,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,4)
fromN = 0.01
toN = 0.1
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,final,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,5)
fromN = 0.1
toN = 1
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,final,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,6)
fromN = 1
toN = 10
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,final,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,7)
fromN = 10
toN = 100
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,final,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,8)
fromN = 100
toN = 1000
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,final,fromN,toN,1000)
plt.plot(x,y)

plt.tight_layout()

plt.show()

