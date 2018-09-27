import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData
from lifeDist import lifeDist, lifeDist2

def getPoint():
    RStarSample = random.uniform(0 , 2)
    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fInteligence = random.uniform(-3 , 0)
    fCivilization = random.uniform(-2 , 0)
    L = random.uniform(2 , 10)
    
    fLife = lifeDist(vMin=-35, vMax=15, tMin=14, tMax=17, mean=0, sigma=200)
    fLifeEks = float(mp.log(fLife, 10))
    
    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    
        # modification
    skip = 0
    mini = -RStarSample - L
    for it in (fPlanets, nEnvironment, fInteligence, fCivilization, fLifeEks):
        if it < np.log10(1/(10**-mini+2)):
            skip = 1
            break
        mini-=it
    # modification
    if skip:
        return getPoint()
    #return np.power(10,resitev)
    if(math.isinf(resitev)):
        return getPoint()
    return resitev

array=[getPoint()]
startTime = time.time()
while(1):
    for _ in range(0,1000):
        array.append(getPoint())
    if time.time()-startTime>60:
        break


saveData(array,"test2")
print('done')
    
    