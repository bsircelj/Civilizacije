import numpy as np
import mpmath as mp
import random
import math
from lifeDist import lifeDist, lifeDist2
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getCDFNIC, normalizePDF
import mpmath as mp
import pylab as p
from ExponentsAlternative import getDistributionOfEks

mp.dps = 230


def calculatePoint():
    RStar = random.uniform(0 , 2)
    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fInteligence = random.uniform(-3 , 0)
    fCivilization = random.uniform(-2 , 0)
    L = random.uniform(2 , 10)
    
    fLife = lifeDist(vMin=0, vMax=15, tMin=14, tMax=17, mean=0, sigma=200)
    fLifeEks = float(mp.log(fLife, 10))
    '''
    # modification
    skip = 0
    mini = -RStarSample - L
    for it in (fPlanets, nEnvironment, fInteligence, fCivilization, fLifeEks):
        if it < mini:
            skip = 1
            break
    # modification    
    '''
    resitev = RStar + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    return fLifeEks


def getDistributionOfEks(size=1000, pdfSize=2151, low=-15, high=15):
    xOs = np.linspace(low, high, pdfSize)
    pdf = [0] * pdfSize
    zmnozek = ((pdfSize - 1) / (high - low))  # =1000
    pristevek = low * zmnozek  # =5000
    izpis = 0
    for i in range(0, size):
        parameters = calculatePoint()
        
        if i % (size / 10) == 0:
            print(izpis, "%")
            izpis += 10
        '''
        if skip:
            continue
        '''        
        if (math.isinf(parameters)):
            pdf[0] += 1
            continue
        zaokrozenIndeks = round(parameters * zmnozek - pristevek)
        if (zaokrozenIndeks < 0):
            pdf[ 0 ] += 1
            continue
        if zaokrozenIndeks >= pdfSize - 1:
            pdf[ pdfSize - 1 ] += 1
            continue
        if (math.isinf(zaokrozenIndeks)):
            pdf[0] += 1
            continue
        indeksPDF = int(zaokrozenIndeks)
        pdf[ indeksPDF ] += 1
    
    return xOs, pdf

start = -150
stop = 15
pdfSize = 2151
size = 10000

xOs, pdf = getDistributionOfEks(size, pdfSize, low = start, high = stop)
#pdf = fl.gaussian_filter( pdf , 20)
cdf = getCDFNIC(pdf)
pdf[0] = pdf[1]
pdf=normalizePDF(pdf)
l = mp.linspace( start, stop, pdfSize )
xOs = [mp.power(10, x) for x in l]

save(xOs, pdf , "pdf")
save(xOs, cdf , "cdf")



#cdf = getCDFNIC(pdf)


#plt.xscale('log')
plt.plot(xOs, pdf, 'blue', label = 'pdf' )
plt.plot(xOs, cdf, 'red', label = 'cdf' )
p.fill(xOs, pdf, facecolor='blue', alpha=0.5)
#plt.xlim(10**start , 10**stop)
plt.xlim(0 , 2)
plt.show()

