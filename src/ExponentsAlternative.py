import numpy as np
import mpmath as mp
import random
import math
from lifeDist import lifeDist, lifeDist2

mp.dps = 230


def getNEksponentSample():
    RStarSample = random.uniform(0 , 2)
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
    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    #return (_, resitev)
    return resitev


def getDistributionOfEks(size=1000, pdfSize=2151, low=-15, high=15):
    xOs = np.linspace(low, high, pdfSize)
    pdf = [0] * pdfSize
    zmnozek = ((pdfSize - 1) / (high - low))  # =1000
    pristevek = low * zmnozek  # =5000
    izpis = 0
    for i in range(0, size):
        #(skip, parameters) = getNEksponentSample()
        parameters = getNEksponentSample()
        
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

