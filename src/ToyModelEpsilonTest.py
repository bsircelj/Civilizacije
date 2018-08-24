import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF
from ToyModel import getAlonePossibility, getAlonePossibilityLOGUNIFORM 


lowEpsilon = 0.0
highEpsilon = 0.04
sizeOfEpsilonRange = 20

xEpsilon = np.linspace(lowEpsilon, highEpsilon, sizeOfEpsilonRange)

pdf1 = []
for epsilon in xEpsilon:
    value = getAlonePossibility(low=0.001+epsilon, high = 0.2 - epsilon, lowerThan=1)
    pdf1.append(value)

pdf2 = []
for epsilon in xEpsilon:
    value = getAlonePossibilityLOGUNIFORM(low=0.001+epsilon, high = 0.2 - epsilon, lowerThan=1)
    pdf2.append(value)
'''
pdf3 = []
for epsilon in xEpsilon:
    value = getAlonePossibility(low=epsilon, high = 0.2, lowerThan=0.5)
    pdf3.append(value)
'''

plt.plot(xEpsilon, pdf1, label = 'uniform')
plt.plot(xEpsilon, pdf2, label = 'log-uniform')
#plt.plot(xEpsilon, pdf3, label = 'cutoff = 0.5')
plt.title('range(0.001 + epsilon, 0.2 ) , cutoff is 1')
plt.ylabel('probability of being alone')
plt.xlabel('epsilon')
plt.legend( loc=1)
plt.xlim(lowEpsilon, highEpsilon)
plt.show()

