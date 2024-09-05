import numpy as np
import time as time

GM=3.983324e14
R=6.371e6
V=10000
dt=1e-2
ha=V**2*R**2/(2*GM-R*V**2)

#CONST dt
pocetak1=time.time()
v=V
r=R
while v>=0:
    v-=GM/r**2*dt
    r+=v*dt
h1=r-R
vreme1=time.time()-pocetak1
print(h1/1000)
print(vreme1)

#ZAVISNI dt
pocetak2 = time.time()
v=V
r=R
C=GM*dt/R**2
while v>=0:
    DT = C*r**2/GM #ne pisemo dt jer je ono sadrzano u C-u
    v-= GM*DT/r**2
    r+=v*DT
h2 = r-R
vreme2 = time.time()-pocetak2
print(h2/1000)
print(vreme2)

print(abs(h1-ha)*100/ha)
print(abs(h2-ha)*100/ha)
print(vreme2/vreme1)
