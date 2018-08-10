'''
Created on 8 Aug 2018

@author: benos
'''
import random
import numpy as np
from mpmath import *
from mpLogspace import mpLogspace
from logHistogramAdd import logHistogramAdd
import time


def mpSampleMultiple(parameters,size,times):
    dist = [0]*size
    izpis=0
    for t in range(0,times):
        val = mpf('1.0')
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
        dist = logHistogramAdd(-40,15,size,dist,val)
        if t%(times/10) == 0:
            print(izpis,"%")
            izpis+=10
            
    #return normalize(scale(size),dist)
    return (scale(size),dist)

def mpSampleMultipleTime(parameters,size,timeLimit):
    dist = [0]*size
    timeStart = time.time()
    while True:
        val = mpf('1.0')
        for p in parameters:
            newVal = sample(p)
            val *= newVal
        dist = logHistogramAdd(-40,15,size,dist,val)
        if time.time()-timeStart>timeLimit:
            break  
            
    #return normalize(scale(size),dist)
    return (scale(size),dist)

def normalize(xaxis, dist):
    surface = mpf('0')
    for i in range(1,len(xaxis)-1):
        surface+= (xaxis[i]-xaxis[i-1])*dist[i]
    print("\n\nSURFACE",surface)
    newDist = [i/surface for i in dist]
    return (xaxis, newDist)
    
        
def scale(size):
    scale = [0]*size
    step = 55/size
    start = -40
    for i in range(1,size):
        scale[i] = 10**(start+step*i)
    return scale

'''
def add(dist,size, value):
    step = mpf(55/size)
    start = mpf('-40')
    for i in range(1,size):
        current = 10**(start+step*i)
        if value<current:
            dist[i-1]+=1
            return dist
'''



def sample(distribution):
    rand = random.random()
    length = len(distribution[2])
    lin = mpLogspace(distribution[0], distribution[1], length)
    cumulSum = mpf('0')
    for i in range(0,length-1):
        cumulSum += distribution[2][i]
        if cumulSum > rand:
            return lin[i]
    return distribution[1]