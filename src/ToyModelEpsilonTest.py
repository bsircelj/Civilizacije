import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF, getAlonePossibility 


lowEpsilon = 0
highEpsilon = 0.03
sizeOfEpsilonRange = 20

xEpsilon = np.linspace(lowEpsilon, highEpsilon, sizeOfEpsilonRange)

pdf1 = []
for epsilon in xEpsilon:
    value = getAlonePossibility(low=epsilon, high = 0.2, lowerThan=1)
    pdf1.append(value)

pdf2 = []
for epsilon in xEpsilon:
    value = getAlonePossibility(low=epsilon, high = 0.2 - epsilon , lowerThan=1)
    pdf2.append(value)
'''
pdf3 = []
for epsilon in xEpsilon:
    value = getAlonePossibility(low=epsilon, high = 0.2, lowerThan=0.5)
    pdf3.append(value)
'''

plt.plot(xEpsilon, pdf1, label = 'range( epsilon, 0.2 )')
plt.plot(xEpsilon, pdf2, label = 'range(epsilon, 0.2 - epsilon )')
#plt.plot(xEpsilon, pdf3, label = 'cutoff = 0.5')
plt.title('ranges are different, cutoff is 1')
plt.ylabel('probability of being alone')
plt.xlabel('epsilon')
plt.legend( loc=1)
plt.xlim(lowEpsilon, highEpsilon)
plt.show()

