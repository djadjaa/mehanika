import numpy as np
import time as time

import matplotlib.pyplot as plt

g=9.81
v0=100
alfa=np.deg2rad(45)
CS=0.001
ro=1.23
dt=1e-3

M=np.arange(100,10000,100)
Do=np.zeros(len(M))
Ho=np.zeros(len(M))

#BEZ OTPORA
Y=[]
x=0
y=0
vx=v0*np.cos(alfa)
vy=v0*np.sin(alfa)
while y>=0:
    vy+=-g*dt #posto je vx const nije neophodno pisati (ax=0)
    x+=vx*dt
    y+=vy*dt
    Y=np.append(Y,y)

D=np.ones_like(M)*x
h=np.amax(Y)
H=np.ones_like(M)*h

#SA OTPOROM

Yo=[[]for column in range(len(M))]

for i,m in enumerate(M):

    x0=0
    y0=0
    vx0=v0*np.cos(alfa)
    vy0=v0*np.sin(alfa)

    while y0 >= 0:
        vo = np.sqrt(vx0**2+vy0**2)#rast
        ax0=-(CS*ro*vo*vx0)/(2*m)
        ay0=-g-CS*ro*vo*vy0/(2*m)

        vx0+=ax0*dt
        vy0+=ay0*dt

        x0+=vx0*dt
        y0+=vy0*dt

        Yo[i].append(y0)

    Do[i]=x0


for i in range(len(Yo)):
    h0=np.amax(Yo[i])
    Ho[i]=h0

#plotovanje
plt.figure()
plt.plot(M,D,'--r')
plt.plot(M,Do,'b')
plt.show()

plt.figure()
plt.plot(M,H,'--r')
plt.plot(M,Ho)
plt.show()