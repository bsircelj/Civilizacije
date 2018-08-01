import numpy as np
import matplotlib.pyplot as plt


def loguniform(low=0.01, high=1, size=10, base=np.exp(1)):
    pdf = np.linspace(low, high, size)
    pdf = 1/(pdf * (np.log(high)- np.log(low)))
    return  pdf/sum(pdf)

#f = loguniform(0.001,1,1000000)[0:2]
#plt.plot(f)
#plt.show()

