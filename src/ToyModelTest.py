import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF

size = 100000
pdfSize = 10001
hundretBilion = 100000000000


tuple = getStandardTuple(size, pdfSize)
pdf = tuple[3]
print("pdf:")
print(pdf)
pdf = fl.gaussian_filter(pdf, 10)
x = tuple[2]
cdfNIC = tuple[4]
cdfPLOSCINA = tuple[5]
print("x:")
print(x)
print("pdf:")
print(pdf)
print(tuple[1])
print("konec")

#plt.plot(x, cdfPLOSCINA , 'green')
plt.plot(x, pdf, 'blue')
plt.plot(x, cdfNIC , 'red')
plt.xscale('log')
plt.xlim(10**(-5), 10**5)
plt.show()


#save(x, pdf, 'ToyModelPDF')
#save(x, cdfPLOSCINA, 'ToyModelCDF')
'''
pdfSize=10001 #mora bit +1 !
x = np.logspace(-5, 5, pdfSize )
for value in x:
    print (int(round(np.log10(value)*1000)+5000) )
'''
#print(arrayOfProducts)
