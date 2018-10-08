from IO import  readData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

size= 50


no = np.linspace(2,10,50)
arrayL = [None]*size
Z = [None]*size

bins = np.linspace(-100,100,51)

for i in range(0,50):
    #arrayL[i] = [10**a for a in readData("L/L"+str(no[i]))]
    arrayL[i] = readData("L/L"+str(no[i]))
    Z[i],_ = np.histogram(arrayL[i], bins)
    

X, Y = np.meshgrid(bins[0:-1],no)
   
     
print("x:",np.shape(X)," y:",np.shape(Y)," z:",np.shape(Z))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

print(X,"\n")
print(Y,"\n")
print(Z)  

# Plot the surface
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,shade=True,color='b',alpha=1)

ax.set_xlabel("log(N)")
ax.set_ylabel("log(maxL)")

#plt.xscale("log")
plt.show()

