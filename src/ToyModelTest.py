import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save, readFile
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF
from ToyModel import getStandardTupleLOGUNIFORM , getStandardTupleNATURALSCALE

size = 100000
pdfSize = 10001

tuple1 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -135, stop = 5 , stParametrov = 9 , low=0.01, high=0.2, hundredBillions = 100000000000)

tuple2 = getStandardTupleLOGUNIFORM(size, pdfSize, lowerThan=1, start = -135 ,stParametrov = 9, stop = 5, low=0.00000000000000000001, high=0.2)

#tuple3 = getStandardTupleLOGUNIFORM(size, pdfSize, lowerThan=1, start = -45 ,stParametrov = 9, low=0.0000001, high=0.2)

arrayOfvalues1 = tuple1[0]
x1 = tuple1[2]
pdf1 = tuple1[3]
cdfNIC1 = tuple1[4]
cdfPLOSCINA1 = tuple1[5]
desetNaStDecimalk = tuple1[6]
polOdArraya = tuple1[7]
pdf1[ -1 ] = pdf1[ -2 ]


arrayOfvalues2 = tuple2[0]
x2 = tuple2[2]
pdf2 = tuple2[3]
cdfNIC2 = tuple2[4]
cdfPLOSCINA2 = tuple2[5]
'''
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


length2 = len(pdf2)
maxPDF2 = 0
index2 = 0
for i in range(0, length2):
    if (pdf2[i] > maxPDF2):
        maxPDF2 = pdf2[i]
        index2 = i


vsota = sum(arrayOfvalues2)
print('manjse od 1:' + str(tuple2[1]))
povprecje2=vsota/size
print(vsota/size)



'''


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
plt.title('low=0.0000001, high=0.2 ')

plt.plot(x1, pdf1, 'red', label='PDF_uniform')
plt.plot(x1, cdfNIC1 , 'orange', label = 'CDF_uniform')
plt.plot([povprecje1 , povprecje1 ], [0,1], 'darkred', label = 'average_uniform')
#plt.plot( 1 , cdfNIC1[int(round( - polOdArraya))], 'go', label = 'st. Civilizacij = 1')

plt.plot(x2, pdf2, 'blue', label = 'PDF_LOGuniform')
plt.plot(x2, cdfNIC2 , 'turquoise', label = 'CDF_LOGuniform')
plt.plot([povprecje2, povprecje2 ], [0,1], 'teal', label= 'average_LOGuniform')
'''

plt.plot(x3, pdf3, 'green', label='PDF_range(0.0000001, 0.2)')
plt.plot(x3, cdfNIC3 , 'lightgreen', label = 'CDF_range(0.0000001, 0.2)')
#plt.plot([povprecje3 , povprecje3 ], [0,1], 'darkgreen', label = 'range(0.0000001, 0.2)')
'''
#save( x1, pdf1, 'teoreticno-uniform, parameters=3')

#x,y = readFile('Toy-model-3-parameters-uniform2.csv')
#y = fl.gaussian_filter(y,3)
#y= normalizePDF(y)
#plt.plot(x, y, 'green', label='pdf(2)')



plt.legend( loc=2 )
plt.ylabel('relative frequency')
plt.xlabel('number of civilizations in the toy galaxy')
plt.xscale('log')
plt.xlim( 10**(-135) , 10**5 )
plt.show()

'''
ver01 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 1 , low=0, high=0.2, hundredBillions = 1000)[1]
print("1")
ver02 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 2 , low=0, high=0.2, hundredBillions = 10000)[1]
print('2')
ver03 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 3 , low=0, high=0.2, hundredBillions = 100000)[1]
print('3')
ver04 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 4 , low=0, high=0.2, hundredBillions = 1000000)[1]
print('4')
ver05 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 5 , low=0, high=0.2, hundredBillions = 10000000)[1]
print('5')
ver06 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 6 , low=0, high=0.2, hundredBillions = 100000000)[1]
print('6')
ver07 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 7 , low=0, high=0.2, hundredBillions = 1000000000)[1]
print('7')
ver08 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 8 , low=0, high=0.2, hundredBillions = 10000000000)[1]
print('8')
ver09 = getStandardTuple(size, pdfSize, lowerThan=1 , start = -6, stop = 5 , stParametrov = 9 , low=0, high=0.2, hundredBillions = 100000000000)[1]

print("1 parameter: "+str(ver01))
print("2 parametra: "+str(ver02))
print("3 parametri: "+str(ver03))
print("4 parametri: "+str(ver04))
print("5 parametrov: "+str(ver05))
print("6 parametrov: "+str(ver06))
print("7 parametrov: "+str(ver07))
print("8 parametrov: "+str(ver08))
print("9 parametrov: "+str(ver09))
x  = np.linspace(1, 9, 9)
y = [ver01, ver02, ver03, ver04, ver05, ver06, ver07, ver08, ver09 ]
plt.title('Probability of there being no civilizations depending on the number of parameters (1-9)')
plt.ylabel('Probability of there being no civilizations')
plt.xlabel('number of parameters')
plt.plot(x, y)
plt.show()
#save(x, pdf, 'ToyModelPDF')
#save(x, cdfPLOSCINA, 'ToyModelCDF')
'''
