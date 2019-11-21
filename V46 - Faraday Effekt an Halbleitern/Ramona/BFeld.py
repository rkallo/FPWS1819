from scipy.optimize import curve_fit
from scipy.stats import sem
from uncertainties import ufloat
from scipy import stats
import scipy.constants as const
import numpy as np
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
import scipy as sp

#-------------------------
#plot homog. B-Feld
#-------------------------
     
z,B=np.loadtxt("b-feld.txt", unpack=True)
  
#Plot für B-Feld
plt.plot(z,B,'b.',label="Messwerte")
plt.xlabel(r"$z$ in mm")
plt.ylabel(r"$B$ in mT")
plt.legend(loc="best")
plt.grid()
plt.savefig("B-Feld.pdf")
plt.show()