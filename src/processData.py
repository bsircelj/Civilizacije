import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData,readData
from lifeDist import lifeDist, lifeDist2

data = readData("sig200_2")

siz = len(data)

formatted = [0] * siz

for d in range(0,siz):
    
    