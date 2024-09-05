import numpy as np
import time as time
import matplotlib.pyplot as plt

g=9.81
Vo=np.arange(10,100,10)
alfa=np.deg2rad(np.arange(10,80,10))
dt=1e-3
M=np.arange(1,100,10)
domet=np.zeros([len(Vo),len(alfa),len(M)])
CS=0.1
ro=1.23
for i in range(len(Vo)):
    for j in range(len(alfa)):
        for k in range(len(M)):
            print(i,j,k)
            x0=0
            y0=0
            vx0=Vo[i]*np.cos(alfa[j])
            vy0=Vo[i]*np.sin(alfa[j])
            while y0>=0:
                v0=np.sqrt(vx0**2+vy0**2)
                ax0=-(CS*ro*v0*vx0)/(2*M[k])
                ay0=-g-CS*ro*v0*vy0/(2*M[k])

                vx0+=ax0*dt
                vy0+=ay0*dt

                x0+=vx0*dt
                y0+=vy0*dt

            domet[i][j][k]=x0

#3D PLOTOVANJE TODO
