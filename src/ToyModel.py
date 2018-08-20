import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from logHistogramAddFast import logHistogramAddFast
from mpLogspace import mpLogspace
from IO import save
#mp.dps=8
size = 500000
pdfSize = 1000
one = mpmathify(1.0)
hundretBilion = 100000000000

def getArrayOfProducts(size):
    arrayOfParameters =[]
    stevecManjsihOd1 = 0
    
    izpis = 0
    for j in range(0, size ):
        
        if j%(size/10) == 0:
            print(izpis,"%")
            izpis+=10
            
        parameters = 1
        for i in range(0,9):
            r = random.uniform(0, 0.2)
            #r = random.normal(0.1,0.1)
            parameters *= r
            
        parameters = parameters * ( 100000000000 )  
        #if parameters<1:
        #    stevecManjsihOd1+=1
        stevecManjsihOd1+=(parameters<1)
        alonePossibility = stevecManjsihOd1/size
        arrayOfParameters.append( parameters )
    return (arrayOfParameters, alonePossibility, )


(array,alonePossibility) = getArrayOfProducts(size)
print(alonePossibility)
#print(arrayOfProducts)

dist = [0]*pdfSize
start = -5
end = 5

izpis=0
for i in range(0,size):
    if i%(size/10) == 0:
        print(izpis,"%")
        izpis+=10
    dist = logHistogramAddFast(start, end, pdfSize, dist, array[i])
    
x = mpLogspace(np.exp(start),np.exp(end),pdfSize)

save(x,dist,0,'Array')

print('writing done')


