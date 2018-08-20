import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
#mp.dps=8
size = 100000
pdfSize = 1000
one = mpmathify(1.0)
hundretBilion = 100000000000

def getArrayOfProducts(size):
    arrayOfParameters =[]
    stevecManjsihOd1 = 0
    
    for j in range(0, size ):
        
        parameters = 1
        for i in range(0,9):
            r = random.uniform(0, 0.2)
            parameters *= r
            
        parameters = parameters * ( 100000000000 )  
        #if parameters<1:
        #    stevecManjsihOd1+=1
        stevecManjsihOd1+=(parameters<1)
        alonePossibility = stevecManjsihOd1/size
        arrayOfParameters.append( parameters )
    return (arrayOfParameters, alonePossibility, )

alonePossibility = getArrayOfProducts(size)[1]
print(alonePossibility)
#print(arrayOfProducts)
