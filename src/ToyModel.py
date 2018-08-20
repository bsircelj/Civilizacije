import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify

def getArrayOfProducts(size):
    arrayOfParameters =[]
    for j in range(0, size ):
    
        parameters = mpmathify(1.0)
        for i in range(0,9):
            r = random.uniform(0, 0.2)
            parameters *= r
        parameters = parameters * 100000000
        arrayOfParameters.append( parameters )
    return arrayOfParameters

print(getArrayOfProducts(10000))