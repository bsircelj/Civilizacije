import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF, getAlonePossibility 


low = 0
high = 0.03
sizeOfEpsilonRange = 20
step = (high - low) / sizeOfEpsilonRange

x = np.linspace(low, high, sizeOfEpsilonRange)
pdf = []

for epsilon in x:
    value = getAlonePossibility(low=epsilon, lowerThan=0.75)
    pdf.append(value)

plt.plot(x, pdf)
plt.xlim(low, high)
plt.show()

