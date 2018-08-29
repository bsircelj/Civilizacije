import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF
from ToyModel import getStandardTupleLOGUNIFORM 

size = 100000
pdfSize = 10001

tuple1 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -5 , stParametrov = 9, low=0, high=0.2, hundredBillions = 100000000000)

#tuple2 = getStandardTupleLOGUNIFORM(size, pdfSize, lowerThan=1, start = -45 ,stParametrov = 9, low=0.00001, high=0.2)

#tuple3 = getStandardTupleLOGUNIFORM(size, pdfSize, lowerThan=1, start = -45 ,stParametrov = 9, low=0.0000001, high=0.2)

arrayOfvalues1 = tuple1[0]
x1 = tuple1[2]
pdf1 = tuple1[3]
cdfNIC1 = tuple1[4]
cdfPLOSCINA1 = tuple1[5]
'''
arrayOfvalues2 = tuple2[0]
x2 = tuple2[2]
pdf2 = tuple2[3]
cdfNIC2 = tuple2[4]
cdfPLOSCINA2 = tuple2[5]

arrayOfvalues3 = tuple3[0]
x3 = tuple3[2]
pdf3 = tuple3[3]
cdfNIC3 = tuple3[4]
cdfPLOSCINA3 = tuple3[5]
'''



length1 = len(pdf1)
maxPDF1 = 0
index1 = 0
for i in range(0, length1):
    if (pdf1[i] > maxPDF1):
        maxPDF1 = pdf1[i]
        index1 = i
'''
print('Xvalue: '+str(x[ index ] ))
'''
vsota = sum(arrayOfvalues1)
print('manjse od 1:' + str(tuple1[1]))
povprecje1 = vsota / size
print(vsota/size)

'''
length2 = len(pdf2)
maxPDF2 = 0
index2 = 0
for i in range(0, length2):
    if (pdf2[i] > maxPDF2):
        maxPDF2 = pdf2[i]
        index2 = i

print('Xvalue: '+str(x[ index ] ))

vsota = sum(arrayOfvalues2)
print('manjse od 1:' + str(tuple2[1]))
povprecje2=vsota/size
print(vsota/size)



length3 = len(pdf3)
maxPDF3 = 0
index3 = 0
for i in range(0, length3):
    if (pdf3[i] > maxPDF3):
        maxPDF3 = pdf3[i]
        index3 = i

print('Xvalue: '+str(x[ index ] ))

vsota = sum(arrayOfvalues3)
print('manjse od 1:' + str(tuple3[1]))
povprecje3=vsota/size
print(vsota/size)

'''
print("konec")

#plt.plot(x1, cdfPLOSCINA1 , 'green')
plt.title('uniform with different ranges:')

plt.plot(x1, pdf1, 'blue', label='PDF_range(0.001, 0.2)')
plt.plot(x1, cdfNIC1 , 'turquoise', label = 'CDF_range(0.001, 0.2)')
#plt.plot([povprecje1 , povprecje1 ], [0,1], 'teal', label = 'range(0.001, 0.2)')
'''
plt.plot(x2, pdf2, 'red', label = 'PDF_range(0.00001, 0.2)')
plt.plot(x2, cdfNIC2 , 'orange', label = 'CDF_range(0.00001, 0.2)')
#plt.plot([povprecje2, povprecje2 ], [0,1], 'brown', label= 'range(0.00001, 0.2)')

plt.plot(x3, pdf3, 'green', label='PDF_range(0.0000001, 0.2)')
plt.plot(x3, cdfNIC3 , 'lightgreen', label = 'CDF_range(0.0000001, 0.2)')
#plt.plot([povprecje3 , povprecje3 ], [0,1], 'darkgreen', label = 'range(0.0000001, 0.2)')
'''
plt.legend( loc=2 )
plt.ylabel('relative frequency')
plt.xlabel('number of civilizations in the toy galaxy')
plt.xscale('log')
plt.xlim(10**(-3), 10**5)
plt.show()


#save(x, pdf, 'ToyModelPDF')
#save(x, cdfPLOSCINA, 'ToyModelCDF')
