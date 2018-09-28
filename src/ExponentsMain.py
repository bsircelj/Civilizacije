import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getCDFNIC, normalizePDF
import mpmath as mp
import pylab as p
from ExponentsAlternative import getDistributionOfEks
from nicePsevdoPDF import getPDFNice
#dejanski program:
start = -40
stop = 15
pdfSize = 2151
size = 100000

xOs, pdf = getDistributionOfEks(size, pdfSize, low = start, high = stop, printOn=1)
cdf = getCDFNIC(pdf)
pdf[0] = pdf[1]
#pdf=normalizePDF(pdf)
l = mp.linspace( start, stop, pdfSize )
xOs = [mp.power(10, x) for x in l]
pdf = fl.gaussian_filter( pdf , 10)

save(xOs, pdf , "laplace_new")
save(xOs, cdf , "laplace_new_cdf")



#cdf = getCDFNIC(pdf)

pdfNice = getPDFNice( xOs, pdf )
print("done")

#save(xOs, pdfNice , "pdfNice 200")

#plt.xscale('log')
#plt.plot(xOs, pdfNice, 'blue', label = 'pdfNice' )
#plt.plot(xOs, cdf, 'red', label = 'cdf' )
#plt.legend( loc=4 )
#plt.plot([1,1],[0,1],'green')
#p.fill(xOs, pdf, facecolor='blue', alpha=0.5)
#plt.xlim(10**start , 10**stop)
#plt.show()

