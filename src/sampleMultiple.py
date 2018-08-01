'''
Created on 1 Aug 2018

@author: benos
'''
import random


def sampleMultiple(parameters,size,times):
    dist = [0]*size
    for t in range(0,times):
        val = 1
        for p in parameters:
            val *= sample(p)
        dist = add(dist,size,val)
    return dist
        
        
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
    random.seed(1)
    rand = random.random()#Check if Mersene Twister
    length = distribution[2].size
    beg = distribution[0]
    end = distribution[1]
    step = (end-beg)/length
    cumulSum = 0
    for i in range(0,length-1):
        cumulSum += distribution[2][i]
        if cumulSum >= rand:
            return step*(i+1)
    