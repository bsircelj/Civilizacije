import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
#mp.dps=8
size = 100000
pdfSize = 10001
one = mpmathify(1.0)
hundretBilion = 100000000000

def getArrayOfProducts(size, pdfSize):   #WARNING: PDFSIZE MUST BE 101, 1001, OR 10001, ETC. 
    pdf= [0] * pdfSize
    cdfNIC = []
    cdfPLOSCINA = []
    #print("pdf1:")
    #print( pdf )
    arrayOfParameters =[]
    stevecManjsihOd1 = 0
    x = np.logspace(-5, 5, pdfSize )
    
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
        
        pdf[int(round(np.log10(parameters)*1000)+5000)]+=1
    
    #pdf = fl.gaussian_filter(pdf, 10)
    sumCDFNIC= 0
    maxPDF = 0
    for value in pdf:
        sumCDFNIC+=value
        cdfNIC.append(sumCDFNIC)
        
        if value > maxPDF:
            maxPDF = value
        
    sumCDFPLOSCINA = 0
    cdfPLOSCINA.append(0.0)
    for i in range(1, pdfSize):
        sumCDFPLOSCINA+= ( x[i] - x[i-1] ) * pdf[i]
        cdfPLOSCINA.append( sumCDFPLOSCINA )
    
    for i in range(0, pdfSize):
        pdf[i] = pdf[i] / maxPDF
        cdfNIC[i] = cdfNIC[i] / sumCDFNIC
        cdfPLOSCINA[i]  = cdfPLOSCINA[i] / sumCDFPLOSCINA
        
    
    return (arrayOfParameters, alonePossibility, x, pdf, cdfNIC, cdfPLOSCINA)

tuple = getArrayOfProducts(size, pdfSize)
pdf = tuple[3]
print(pdf)
pdf = fl.gaussian_filter(pdf, 10)
x = tuple[2]
cdfNIC = tuple[4]
cdfPLOSCINA = tuple[5]
print("x:")
print(x)
print("pdf:")
print(pdf)
print("konec")

#plt.plot(x, cdfPLOSCINA , 'green')
'''
plt.plot(x, pdf, 'blue')
plt.plot(x, cdfNIC , 'red')
plt.xscale('log')
plt.xlim(10**(-5), 10**5)
plt.show()
'''

save(x, pdf, 0, 'ToyModelPDF')
save(x, cdfPLOSCINA, 0, 'ToyModelCDF')
'''
pdfSize=10001 #mora bit +1 !
x = np.logspace(-5, 5, pdfSize )
for value in x:
    print (int(round(np.log10(value)*1000)+5000) )
'''
#print(arrayOfProducts)