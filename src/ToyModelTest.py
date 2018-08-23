import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF 

size = 100000
pdfSize = 10001

tuple = getStandardTuple(size, pdfSize, lowerThan=1 ,stParametrov = 9, low=0, high=0.2)

pdf = tuple[3]
'''
print("pdf:")
print(pdf)
'''
x = tuple[2]
#pdf = fl.gaussian_filter(pdf, 100)
cdfNIC = tuple[4]
cdfPLOSCINA = tuple[5]

'''
print("x:")
print(x)
print("pdf:")
print(pdf)
print(tuple[1])
'''
index = 0
length = len(pdf)
maxPDF = 0
index = 0
for i in range(0, length):
    if (pdf[i] > maxPDF):
        maxPDF = pdf[i]
        index = i
'''
print('Xvalue: '+str(x[ index ] ))
'''

#print(cdfPLOSCINA)
arrayOfvalues = tuple[0]
vsota = sum(arrayOfvalues)
print('manjse od 0.75:' + str(tuple[1]))
print(vsota/size)


print("konec")

#plt.plot(x, cdfPLOSCINA , 'green')
plt.title('low=0.0, high=0.2')
plt.plot(x, pdf, 'blue')
plt.plot(x, cdfNIC , 'red')
plt.xscale('log')
plt.xlim(10**(-5), 10**5)
plt.show()


#save(x, pdf, 'ToyModelPDF')
#save(x, cdfPLOSCINA, 'ToyModelCDF')
