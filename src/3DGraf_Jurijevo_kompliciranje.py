from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from ExponentsAlternative import getDistributionOfEksKnownFL, getNEksponentSampleKnownFl

#input:
startFLife = -100
stopFLife = 0
sizeFlife = 100

startXOs = -84
stopXOs = 15
sizeXOs = 100




#fLife = np.linspace( startFLife, stopFLife , sizeFlife )
fLife = np.linspace(  stopFLife, startFLife, sizeFlife )
#fLife = np.flip(fLife)
xOs = np.linspace( startXOs , stopXOs , sizeXOs )

pdfARRAY = []

for value in fLife:
    pdf = getDistributionOfEksKnownFL(size=10000, pdfSize=sizeXOs, low=startXOs, high=stopXOs, flEks = value)[1]
    pdfARRAY.append(pdf)

#print(pdfARRAY)
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
#X = [ 1,2,3,4]
#Y = [-4,-3,-2,-1, 1, -5]
#X, Y = np.meshgrid(X, Y)
xOs, fLife = np.meshgrid( xOs, fLife)
#Z = xOs

#Z2 = X+Y
#Z / pdfARRAY:

Z = xOs
#for i in range( 0, sizeFlife ):
#    Z[i] = pdfARRAY[i]
    
X = xOs
Y = fLife
#Z = pdfARRAY
Z= np.array(pdfARRAY)
print(X,"\n")
print(Y,"\n")
print(Z)   
     
#print(xOs)


print("x:",np.shape(xOs)," y:",np.shape(fLife)," z:",np.shape(Z))
# Plot the surface.
surf = ax.plot_surface( xOs, fLife, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

#ax = fig.add_subplot(111, projection='3d')

# Plot the surface
#ax.plot_surface(X, Y, Z, color='b')
#plt.xscale("log")

ax.set_xlabel("log(N)")
ax.set_ylabel("log(Fl)")
plt.gca().invert_yaxis()


plt.show()