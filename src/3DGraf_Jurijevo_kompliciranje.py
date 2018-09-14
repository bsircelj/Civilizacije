'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from ExponentsAlternative import getDistributionOfEksKnownFL, getNEksponentSampleKnownFL

#input:
startFLife = -199
stopFLife = 0
sizeFlife = 20

startXOs = -84
stopXOs = 15
sizeXOs = 1000




fLife = np.linspace( startFLife, stopFLife , sizeFlife )
xOs = np.linspace( startXOs , stopXOs , sizeXOs )

pdfARRAY = []

for value in fLife:
    pdf = getDistributionOfEksKnownFL(size=10000, pdfSize=sizeXOs, low=startXOs, high=stopXOs, flEks = value)[1]
    pdfARRAY.append(pdf)

print(pdfARRAY)
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = [ 1,2,3,4]
Y = [-4,-3,-2,-1, 1, -5]
X, Y = np.meshgrid(X, Y)
xOs, fLife = np.meshgrid( xOs, fLife)
Z = xOs

Z2 = X+Y
#Z / pdfARRAY:

Z = xOs
for i in range( 0, sizeFlife ):
    Z[i] = pdfARRAY[i]
    
print(X)
print(Y)
print( Z2 )
print(xOs)


# Plot the surface.
surf = ax.plot_surface( xOs, fLife, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()