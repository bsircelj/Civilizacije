'''
Created on 22 Aug 2018

@author: benos
'''
from IO import readFile,save
import numpy as np
from logHistogramAdd import logHistogramAdd
from mpSampleMultiple import scale



(xaxis,yaxis) = readFile("sigma is 50.csv")

size = len(yaxis)

start = 0
end = np.log(xaxis[-1])

dist = [0]*size

izpis = 0
for i in range(0,size):
    dist = logHistogramAdd(start, end, size, dist, yaxis[i]+1)
    if i % (size / 10) == 0:
        print(izpis, "%")
        izpis += 10
    
save(scale(start,end,size),dist,'Sigma is 50 plus 1')

print('done')