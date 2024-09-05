import numpy as np
import time as time

import matplotlib.pyplot as plt

GM=3.983324e14
R=6.371e6
V=np.arange(2000,10000,1000)
dt=1e-2
Ha=V**2*R**2/(2*GM-R*V**2)
razlike1=[]
razlike2=[]

for i in range(len(V)):

    #CONST dt
    v=V[i]
    r=R
    while v>=0:
        v-=GM/r**2*dt
        r+=v*dt
    h1=r-R
    razlike1.append(abs(h1-Ha[i])*100/Ha[i]) #zbog V Ha je postala lista
    #ZAVISNI dt
    v=V[i]
    r=R
    C=GM*dt/R**2
    while v>=0:
        DT = C*r**2/GM #ne pisemo dt jer je ono sadrzano u C-u
        v-= GM*DT/r**2
        r+=v*DT
    h2 = r-R
    razlike2.append(abs(h2-Ha[i])*100/Ha[i])

plt.figure()
plt.plot(V,razlike1)
plt.plot(V,razlike2)
plt.grid()
plt.show()
