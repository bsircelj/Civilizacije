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

(xaxis,yaxis) = readFile("sigma is 200 uniform.csv")



avg=0
for i in range(0,len(xaxis)):
    avg+=yaxis[i]*xaxis[i]
avg/=sum(yaxis)
print(sum(yaxis))
#avg=avg-24821395

    
yaxis = fl.gaussian_filter(yaxis, 20)

(mean,median) = meanMedian(xaxis,yaxis)

print("\nMean: ", mean, "\nMedian: ", median)
print("Average: ",avg)

#createGraph(xaxis,yaxis,start,end,size)
(length, xaxis, yaxis, cdf,cdfW )= StandardizeDistributionW(xaxis,yaxis)



plt.figure(1)
multiplier = -2

plt.subplot(4,2,1)
fromN = 10**(0+multiplier)
toN = 10**(2+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,2)
fromN = 10**(2+multiplier)
toN = 10**(4+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,3)
fromN = 10**(4+multiplier)
toN = 10**(6+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,4)
fromN = 10**(6+multiplier)
toN = 10**(8+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,5)
fromN = 10**(8+multiplier)
toN = 10**(10+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,6)
fromN = 10**(10+multiplier)
toN = 10**(12+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,7)
fromN = 10**(12+multiplier)
toN = 10**(14+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.subplot(4,2,8)
fromN = 10**(14+multiplier)
toN = 10**(16+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.plot(x,y)

plt.tight_layout()

plt.figure(2)

#yaxis = fl.gaussian_filter(yaxis, 15)


plt.plot(xaxis,cdf,'red', label = 'CDF')
#plt.plot(xaxis,cdfW,'green')
#plt.title('5 parameters')


#plt.yscale("log")
#plt.ylim(0,0.0200)

plt.xscale("log")
plt.plot(xaxis, yaxis,'blue',label='PDF')
plt.legend(loc=4)

plt.show()

