import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData,readData
from lifeDist import lifeDist, lifeDist2


plt.figure(1)
logArray = readData("Longevity")
# normed=1,rwidth=0.95
n, bins, patches = plt.hist(logArray, 1000, facecolor='red', alpha=0.75,cumulative=True)
#plt.grid(True)
#plt.axis([-5, 100,0,400])
#plt.show()

plt.figure(2)
normArray = [np.power(10,a) for a in logArray]


for i in range(0,4):

    start=0
    end=10**(i*2+5)
    plt.subplot(2,2,i+1)
    plt.axis([start, end,0,16000])
    plt.hist(normArray,np.linspace(start,end,1000),facecolor='red',alpha=0.75,cumulative=True)
    plt.title(str(start)+' - '+str(end))
    plt.tight_layout()

plt.show()