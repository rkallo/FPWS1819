import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show


x, y = np.loadtxt('CvT.txt', unpack=True, delimiter=',')

plt.plot(x, y, "kx", label="Messwerte")
plt.errorbar(x, y, yerr=y, fmt="none", capsize=5, capthick=1, ms=9, markerfacecolor="red")

#def f(x,a,b):
 # return a*x+b
#popt, pcov = curve_fit(f, a, b)
#print(popt)
#print(np.diag(pcov))
#print(np.sqrt(np.diag(pcov)))

c_new = np.linspace(x[1], x[28], 100)

plt.figure(1)
#plt.plot(c_new, f(c_new), '-', label='Lineare Regression')
plt.xlabel(r'$T$ / K')
plt.ylabel(r'$C$ / $\frac{J}{mol K}$')
plt.grid()
plt.legend(loc= 'best')

plt.savefig('CvGegenT.pdf')
