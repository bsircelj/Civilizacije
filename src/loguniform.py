import numpy as np
import matplotlib.pyplot as plt


def loguniform(low=0.01, high=1, size=10, base=np.exp(1)):
    pdf = np.linspace(low, high, size)
    pdf = 1/(pdf * (np.log(high)- np.log(low)))
    return  (low,high,pdf/sum(pdf))

#f = loguniform(1,100,1000)[2]
#plt.xscale("log")
#plt.plot(f)
#plt.show()

