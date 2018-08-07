'''
Created on 1 Aug 2018

@author: benos
'''
import random
import openturns as ot
import numpy as np

def sampleMultiple(parameters,size,times):
    dist = [0]*size
    izpis=0
    for t in range(0,times):
        val = 1
        for p in parameters:
            newVal = sample(p)
            #newVal = p.getSample(1)
            '''
            print(newVal)
            pt = newVal.point
            print(pt)
            v = pt.value
            print(v)
            if newVal == 0:
                print("ZERO\n")
            '''
            val *= newVal
        dist = add(dist,size,val)
        if t%(times/10) == 0:
            print(izpis,"%")
            izpis+=10
            
    #return normalize(scale(size),dist)
    return (scale(size),dist)

def normalize(xaxis, dist):
    surface = 0
    for i in range(1,len(xaxis)-1):
        surface+= (xaxis[i]-xaxis[i-1])*dist[i]
    print("\n\nSURFACE",surface)
    newDist = [i/surface for i in dist]
    return (xaxis, newDist)
    
        
def scale(size):
    scale = [0]*size
    step = 55/size
    start = -40
    r = range(1,size)
    for i in r:
        scale[i] = 10**(start+step*i)
    return scale

def add(dist,size, value):
    step = 55/size
    start = -40
    r = range(1,size)
    for i in r:
        current = 10**(start+step*i)
        if value<current:
            dist[i-1]+=1
            return dist
        



def sample(distribution):
    random.seed()
    rand = random.random()
    length = distribution[2].size
    beg = distribution[0]
    end = distribution[1]
    lin = np.linspace(distribution[0], distribution[1], len(distribution[2]))
    cumulSum = 0
    distance = beg
    for i in range(0,length-1):
        cumulSum += distribution[2][i]
        if cumulSum > rand:
            return lin[i]
    return distance
    