'''
Created on 9 Aug 2018

@author: benos
'''
from mpmath import mpmathify,mp,mpf
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
from mpLogNormal import mpLogNormal

size = 1000
#low = mpmathify(mpf('10')**(-188))
low = mpmathify(mpf('10'))
high = mpf('100.0')
x = mp.linspace(mp.log(low) , mp.log(high), size)
x = [ mp.exp(kos) for kos in x]

#lamb = mpLogNormal( mp.log(mpf('10')**(-188)) , mp.log(mpf('1')), size, mpf('1'), mpmathify(10**50) )[2]
lamb = mpLogNormal( mp.log(mpf('10')) , mp.log(mpf('100')), size, mpf('20'), mpf('5') )[2]

print(x)
print(lamb)
plt.plot(x, lamb)
#plt.xscale('log')
#plt.xlim(10**(-188),1)
plt.xlim(1,100)
plt.show()
#plot(lamb, xlim=[low, high])