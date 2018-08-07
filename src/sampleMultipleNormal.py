'''
Created on 6 Aug 2018

@author: benos
'''

import random


def sampleMultipleNormal(parameters,size,times):
    dist = [0]*size
    izpis=0
    for t in range(0,times):
        val = 1
        for p in parameters:
            newVal = sample(p)
            val *= newVal
        val *= 1#Flife
        dist[t] = val
        if t%(times/10) == 0:
            print(izpis,"%")
            izpis+=10            
    return
     

def sample(distribution):
    random.seed()
    rand = random.random()
    length = distribution[2].size
    beg = distribution[0]
    end = distribution[1]
    step = (end-beg)/length
    cumulSum = 0
    distance = beg
    for i in range(0,length-1):
        cumulSum += distribution[2][i]
        if cumulSum < rand:
            distance+=step
    return distance
    