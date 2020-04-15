import numpy as np
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt

import QPSK_Helstrom as QH
import QPSK_error_montecalro as QEM

plt.close('all')


M=10
eta=0.72
dark=9.0805029224*10**(-3)/float(M)
visibility=0.996
trysim=10**5
meanphotonmax=10

Error2=QEM.errorM(M,eta,visibility,dark,trysim,meanphotonmax)

M=4
eta=0.72
dark=9.0805029224*10**(-3)/float(M)
visibility=0.996
trysim=10**5
meanphotonmax=10

Error22=QEM.errorM(M,eta,visibility,dark,trysim,meanphotonmax)

Photon = []
Helstrombox = []
Heterodynebox = []
for m in np.arange(0.1, meanphotonmax, 0.5):
    Helstrombox += [QH.Helstrom(np.sqrt(m))]
    Heterodynebox += [QH.Heterodyne(np.sqrt(m))]
    Photon += [m]

plt.plot(Photon, Error2, 'g')
plt.plot(Photon, Error22, 'r')

plt.plot(Photon, Helstrombox, color='black',  linestyle='dashed')
plt.plot(Photon, Heterodynebox, color='black', linestyle='dashdot')
plt.yscale('log')

plt.ylim([10**(-5),1])
plt.show()

