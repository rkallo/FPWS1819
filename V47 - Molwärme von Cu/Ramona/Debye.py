import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show


x, y = np.loadtxt('Debye.txt', unpack=True,delimiter=',')

x_new = np.linspace(80 , 170 , 100)

plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')

plt.xlabel(r'$T$ / K')
plt.ylabel(r'$\theta$ / K')
plt.grid()
plt.legend(loc='best')


plt.savefig('Debye.pdf')