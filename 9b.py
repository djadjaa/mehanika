import numpy as np
import time as time

import matplotlib.pyplot as plt

GM=3.983324e14
R=6.371e6
V=np.arange(2000,10000,1000)
dt=1e-2
ha=V**2*R**2/(2*GM-R*V**2)
odnos=[]

for i in range(len(V)):

    #CONST dt
    pocetak1=time.time()
    v=V[i]
    r=R
    while v>=0:
        v-=GM/r**2*dt
        r+=v*dt
    h1=r-R
    vreme1=time.time()-pocetak1

    #ZAVISNI dt
    pocetak2 = time.time()
    v=V[i]
    r=R
    C=GM*dt/R**2
    while v>=0:
        DT = C*r**2/GM #ne pisemo dt jer je ono sadrzano u C-u
        v-= GM*DT/r**2
        r+=v*DT
    h2 = r-R
    vreme2 = time.time()-pocetak2

    odnos.append(vreme2/vreme1)
plt.figure()
plt.plot(V,odnos)
plt.grid()
plt.show()
