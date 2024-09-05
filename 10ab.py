import numpy as np
import time as time

import matplotlib.pyplot as plt

g=9.81
v0=100
alfa=np.deg2rad(45)

dt=1e-2

#BEZ OTPORA
X=[]
Y=[]

x=0
y=0
vx=v0*np.cos(alfa)
vy=v0*np.sin(alfa)
while y>=0:
    vy-=g*dt #posto je vx const nije neophodno pisati (ax=0)
    x+=vx*dt
    y+=vy*dt
    X.append(x)
    Y.append(y)

#SA OTPOROM
CS=0.001
ro=1.23
m=1
Xo=[]
Yo=[]
x0=0
y0=0
vx0=v0*np.cos(alfa)
vy0=v0*np.sin(alfa)

while y0 >= 0:
    v0 = np.sqrt(vx0**2+vy0**2)#rast
    ax0=-(CS*ro*v0*vx0)/(2*m)
    ay0=-g-CS*ro*v0*vy0/(2*m)

    vx0+=ax0*dt
    vy0+=ay0*dt

    x0+=vx0*dt
    y0+=vy0*dt

    Xo.append(x0)
    Yo.append(y0)

X=np.array(X)
Y=np.array(Y)
Xo=np.array(Xo)
Yo=np.array(Yo)

#BEZ OTPORA
H=np.amax(Y)
D= X[-1]
Ho=np.amax(Yo)
Do=Xo[-1]
#plotovanje
plt.figure()
plt.plot(X,Y,'b')
plt.plot(Xo,Yo,'r')
plt.plot(X[np.argwhere(Y==H)],H,'ob')
plt.plot(D,Y[-1],'og')
plt.plot(Xo[np.argwhere(Yo==Ho)],Ho,'or')
plt.plot(Do,Yo[-1],'oy')
plt.show()

