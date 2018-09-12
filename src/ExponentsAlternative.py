from mpSampleMultiple import mpSampleMultiple, mpSampleMultipleTime, sampleL
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from lifeDist import lifeDist, lifeDist2
from mpmath import mpmathify
import mpmath as mp
import time
from meanMedian import meanMedian
from IO import save, readFile
import random
from ToyModel import getCDFNIC, getMaxPDF, normalizePDF
import math
import pylab as p
from mpLogspace import mpLogspace
mp.dps=230


def getNEksponentSample():
    RStarSample = random.uniform( 0 , 2 )
    fPlanets = random.uniform( -1 , 0 )
    nEnvironment = random.uniform( -1 , 0 )
    fInteligence = random.uniform( -3 , 0 )
    fCivilization = random.uniform( -2 , 0 )
    L = random.uniform( 2 , 10 )
    
    fLife = lifeDist(vMin=0,vMax=15,tMin=14,tMax=17,mean=0, sigma=200)
    fLifeEks = float( mp.log(fLife, 10) )
    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    return resitev

def getDistributionOfEks( size = 1000, pdfSize = 2151, low = -15, high = 15):
    xOs = np.linspace(low, high, pdfSize )
    pdf= [0] * pdfSize
    zmnozek = ((pdfSize - 1) / (high - low))  # =1000
    pristevek = low * zmnozek  # =5000
    for i in range(0, size):
        parameters = getNEksponentSample()
        
        if (math.isinf(parameters)):
            pdf[0] += 1
            continue
        zaokrozenIndeks = round(parameters * zmnozek - pristevek )
        if (zaokrozenIndeks < 0):
            pdf[ 0 ] += 1
            continue
        if zaokrozenIndeks >= pdfSize - 1:
            pdf[ pdfSize - 1 ] += 1
            continue
        if (math.isinf(zaokrozenIndeks)):
            pdf[0] += 1
            continue
        indeksPDF = int( zaokrozenIndeks )
        pdf[ indeksPDF ] += 1
    
    return xOs, pdf

#dejanski program:
start = -40
stop = 15
pdfSize = 2151
size = 10000

xOs, pdf = getDistributionOfEks(size, pdfSize, low = start, high = stop)
cdf = getCDFNIC(pdf)
pdf[0] = pdf[1]
pdf=normalizePDF(pdf)
pdf = fl.gaussian_filter( pdf , 1)
#cdf = getCDFNIC(pdf)


l = mp.linspace( start, stop, pdfSize )
xOs = [mp.power(10, x) for x in l]

save(xOs, pdf , "pdf-sigma 200")
save(xOs, cdf , "cdf-sigma 200")

plt.xscale('log')
plt.plot(xOs, pdf, 'blue', label = 'pdf' )
plt.plot(xOs, cdf, 'red', label = 'cdf' )
p.fill(xOs, pdf, facecolor='blue', alpha=0.5)
plt.xlim(10**start , 10**stop)
plt.show()






