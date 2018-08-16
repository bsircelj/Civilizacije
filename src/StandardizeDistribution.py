'''
Created on 14 Aug 2018

@author: JURIJ NASTRAN
'''
from mpLogspace import mpLogspace
from mpmath import mpf

def StandardizeDistribution (distribution):
    length = len(distribution[2])
    logXarray = mpLogspace( distribution[0], distribution[1], length )
    
    surface = mpf('0')
    cdf=[surface]
    #pdf=[None] * length
    for i in range(1,length):
        surface += (logXarray[i]-logXarray[i-1])*distribution[2][i]
        cdf.append(surface)                                            #eventually get cdf
    

    for i in range(0, length):
        #pdf[i]= distribution[2][i]                            #normalize pdf and cdf ( now: surface = 1 )
        cdf[i] = cdf[i] / surface
    stdDistribution = (length, logXarray, distribution[2], cdf )
    return stdDistribution