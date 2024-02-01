# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:26:34 2024

@author: duter
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Numpy_files/noisydata.csv",skiprows=1,delimiter=",")

pressure = data[:,0]
flowrate = data[:,1]

# Polynomial curve fit

fit = np.polyfit(pressure, flowrate,2) # 2 -> order

flowfit = np.polyval(fit, pressure)

plt.plot(pressure, flowrate, "go")
plt.plot(pressure, flowfit, "k-")
plt.xlabel("Pressure (Pa)")
plt.ylabel("Flowrate ($m^3/s)$")
plt.show()

data_avg = np.mean(data,0)
print(data_avg)

"""
[ 5.         41.82439269]
"""

print(data_avg[1])

"""
41.82439268729078
"""

# Calculating pi :-)

n = 3000
x = np.random.uniform(size=n)
y = np.random.uniform(size=n)
print(sum(x*x+y*y<=1)/n*4)
plt.plot(x[x*x+y*y<=1], y[x*x+y*y<=1], "bo")
plt.plot(x[x*x+y*y>1], y[x*x+y*y>1], "ro")
plt.savefig("PI.png")
plt.show()

