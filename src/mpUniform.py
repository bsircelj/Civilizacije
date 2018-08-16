'''
Created on 10 Aug 2018

@author: benos
'''
from StandardizeDistribution import StandardizeDistribution


def mpUniform(low=0.01, high=1, size=10):
    pdf = [1 / size] * size
    return StandardizeDistribution((low, high, pdf))

