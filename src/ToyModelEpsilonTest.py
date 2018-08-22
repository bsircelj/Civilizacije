import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF, getAlonePossibility 

print(getAlonePossibility())