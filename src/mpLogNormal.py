'''
Created on 8 Aug 2018

@author: benos
'''
import numpy as np
from math import *
#from scipy import mpmath
from mpmath import *

def mpLogNormal(min=0.000000000000000000001, max=1, size=1000000, median=0.63, sigma=0.679):
    
    mu = mp.log(median, e)
    mu = 1
    
    #import matplotlib.pyplot as plt

    x = mp.linspace(min, max , size)
    '''
    lahko to uporabis
    newList = [x / myInt for x in myList]
    
    
    '''
    pdf = (mp.exp(-(mp.log(x) - mu) ** 2 / (2 * sigma ** 2))
           / (x * sigma * mp.sqrt(2 * mp.pi)))

    return (min, max, pdf)


