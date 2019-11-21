from scipy.optimize import curve_fit
from scipy.stats import sem
from uncertainties import ufloat
from scipy import stats
import scipy.constants as const
import numpy as np
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
import scipy as sp
from pylab import figure, axes, pie, title, show
 

print('V46-Faraday Effekt')

x, y = np.loadtxt('Rein.txt', unpack=True,delimiter=',')
z, u = np.loadtxt('Dotiert.txt', unpack=True,delimiter=',')

plt.figure(1)
plt.plot(x,y,'x',label="Hochrein")
plt.plot(z,u,'o',label="Schwach Dotiert")
plt.xlabel(r"$\lambda$ in $\mu$m")
plt.ylabel(r"$\Delta\theta_{n}$ in $\frac{1}{mm}$")
plt.grid()
plt.legend(loc="best")
plt.savefig('Messdaten.pdf')

