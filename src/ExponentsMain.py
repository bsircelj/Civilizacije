import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getCDFNIC, normalizePDF
import mpmath as mp
import pylab as p
from ExponentsAlternative import getDistributionOfEks
#dejanski program:
start = -40
stop = 15
pdfSize = 2151
size = 100000

xOs, pdf = getDistributionOfEks(size, pdfSize, low = start, high = stop)
cdf = getCDFNIC(pdf)
pdf[0] = pdf[1]
pdf=normalizePDF(pdf)
l = mp.linspace( start, stop, pdfSize )
xOs = [mp.power(10, x) for x in l]

save(xOs, pdf , "pdf 200")
save(xOs, cdf , "cdf 200")


pdf = fl.gaussian_filter( pdf , 20)
#cdf = getCDFNIC(pdf)


plt.xscale('log')
plt.plot(xOs, pdf, 'blue', label = 'pdf' )
plt.plot(xOs, cdf, 'red', label = 'cdf' )
p.fill(xOs, pdf, facecolor='blue', alpha=0.5)
plt.xlim(10**start , 10**stop)
plt.show()

