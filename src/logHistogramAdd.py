'''
Created on 10 Aug 2018

@author: benos
'''
from mpmath import mpmathify,mpf


def logHistogramAdd(start, end, size, dist, value):
    start = mpf(start)
    end = mpf(end)
    step = mpf((end-start) / size)
    for i in range(1, size):
        current = mpmathify(10 ** (start + step * i))
        if value < current:
            dist[i - 1] += 1
            return dist
