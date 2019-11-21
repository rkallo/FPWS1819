import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show


x, y = np.loadtxt('CvT.txt', unpack=True,delimiter=',')

x_new = np.linspace(80 , 300 , 100)

plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')

plt.xlabel(r'$T$ / K')
plt.ylabel(r'$C$ / $\frac{J}{mol K}$')
plt.grid()
plt.legend(loc='best')


plt.savefig('CvT2.pdf')
