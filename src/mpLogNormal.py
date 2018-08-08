'''
Created on 8 Aug 2018

@author: benos
'''
import numpy as np
from math import *
#from scipy import mpmath
from mpmath import *

def mpLogNormal(low=0.000000000000000000001, high=1, size=1000000, median=0.63, sigma=0.679):
    
    mu = mp.log(median, e)
    mu = mpf('1')
    
    #import matplotlib.pyplot as plt

    '''
    lahko to uporabis
    newList = [x / myInt for x in myList]
    
    
    
    pdf = (mp.exp(-(mp.log(x) - mu) ** 2 / (2 * sigma ** 2))
           / (x * sigma * mp.sqrt(2 * mp.pi)))
    

    return (min, max, pdf)
    '''
    pdf = mp.linspace(low, high, size)
    sum = mpf('0')
    for i in range(0,len(pdf)):
        #pdf[i] = mpf('1.0')/(pdf[i] * (mp.log(high)- mp.log(low)))
        pdf[i] = (mp.exp(-(mp.log(pdf[i]) - mu) ** 2 / (2 * sigma ** 2)) / (pdf[i] * sigma * mp.sqrt(2 * mp.pi)))
        sum += pdf[i]
    return  (low,high,[x/sum for x in pdf])


