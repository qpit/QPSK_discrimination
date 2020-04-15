import numpy as np
from math import erf


def Helstrom(alpha):
    return 1-abs(1/4*(np.sqrt(1+np.exp(-2*alpha**2)-np.exp(-alpha**2*(1+1j))-np.exp(-alpha**2*(1-1j)))+np.sqrt(1+np.exp(-2*alpha**2)+np.exp(-alpha**2*(1+1j))+np.exp(-alpha**2*(1-1j)))+np.sqrt(1-np.exp(-2*alpha**2)-np.exp(-alpha**2*(4+2j))*np.sqrt(-np.exp(alpha**2*(6+2j))*(-1+np.exp(2*1j*alpha**2))**2))+np.sqrt(1-np.exp(-2*alpha**2)+np.exp(-alpha**2*(4+2j))*np.sqrt(-np.exp(alpha**2*(6+2j))*(-1+np.exp(2*1j*alpha**2))**2))))**2


def Heterodyne(alpha):
    return 1-1/4*(1+erf(np.sqrt(alpha**2/2)))**2