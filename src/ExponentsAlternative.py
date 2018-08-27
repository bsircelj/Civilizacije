from mpSampleMultiple import mpSampleMultiple, mpSampleMultipleTime, sampleL
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from lifeDist import lifeDist
from mpmath import mpmathify
import mpmath as mp
import time
from meanMedian import meanMedian
from IO import save, readFile
import random
from ToyModel import getCDFNIC, getMaxPDF, normalizePDF
mp.dps=230

#vnesi low and high pa sigmo in mu
low = -105
high = 15
median = 0
sigma = 2

def getNEksponentSample():
    RStarSample = random.uniform( 0 , 2 )
    fPlanets = random.uniform( -1 , 0 )
    nEnvironment = random.uniform( -1 , 0 )
    fInteligence = random.uniform( -3 , 0 )
    fCivilization = random.uniform( -2 , 0 )
    L = random.uniform( 2 , 10 )
    
    fLife = lifeDist(vMin=0,vMax=15,tMin=14,tMax=17,mean=0, sigma=100)
    fLifeEks = float( mp.log(fLife, 10) )
    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    return resitev

def getDistributionOfEks( size = 100000, pdfSize = 1201, low = -100, high = 15):
    xOs = np.linspace(low, high, pdfSize )
    pdf= [0] * pdfSize
    zmnozek = ((pdfSize - 1) / (high - low))  # =1000
    pristevek = low * zmnozek  # =5000
    for i in range(0, size):
        parameters = getNEksponentSample()
        
        indeksPDF = int(round(parameters * zmnozek - pristevek ))
        if indeksPDF < 0:
            indeksPDF = 1
        elif indeksPDF >= pdfSize:
            indeksPDF = pdfSize - 1
        pdf[indeksPDF] += 1
    
    return xOs, pdf

#dejanski program:
start = -100
stop = 15

xOs, pdf = getDistributionOfEks(low = start, high = stop)
cdf = getCDFNIC(pdf)
pdf=normalizePDF(pdf)
pdf = fl.gaussian_filter( pdf , 10)
#cdf = getCDFNIC(pdf)
plt.plot(xOs, pdf, 'blue', label = 'pdf' )
plt.plot(xOs, cdf, 'red', label = 'cdf' )
plt.xlim(low, high)
plt.show()




