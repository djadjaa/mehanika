import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

g=9.81
Hsp = 100
d=15
dt=1e-3

#alfa=np.arctan(Hsp/d)
#Vomin=np.sqrt(g*Hsp/(2*np.sin(alfa)**2))
Vo = np.arange(10,35,5)
ALFA = np.deg2rad(np.arange(70,95,5))

R = [[[]for column in range(len(ALFA))]for row in range(len(Vo))]
for i,v0 in enumerate(Vo):
    for j,alfa in enumerate(ALFA):
        xks=0
        yks=0
        vxks=Vo*np.cos(alfa)
        vyks=Vo*np.sin(alfa)

        xsp=d
        ysp=Hsp
        vsp=0 #ne uzimamo vx u obzir jer je x const

        while xks<d and yks>=0 and ysp>=0:
            vyks-=g*dt
            xks+=vxks*dt
            yks+=vyks*dt
            
            vsp-=g*dt
            ysp+=vsp*dt

        R[i][j]=np.sqrt((xsp-xks)**2+(ysp-yks)**2) #rastojanje

R=np.array(R)
resenje = np.where(R==np.min(R))
print(resenje[0][0])
print(Vo[resenje[0][0]])
print(np.rad2deg(alfa[resenje[0][0]]))