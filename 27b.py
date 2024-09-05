"""
Primenom OKM odrediti heliocentricnu putanju kosmicke letelice koja se sa Zemlje lansirana brzi-
nom 10km/s (u odnosu na Zemlju) normalno na pravac Zemljine heliocentricne brzine sa dijame-
tralno suprotne tacke od Sunca. Pp da se Zemlja krece po kruznoj putanji oko Sunca.

b) Uzeti u obzir gravitaciju Zemlje i gravitaciju Sunca i kretanje posmatrati u toku jedne juli-
jalnske godine (365.25)

"""

import numpy as np
import time as time
import matplotlib.pyplot as plt

Ms=1.989e30
Mz=5.972e24
Rz=6.378e6
aj=1.5e11 #astronomska jedinica = Rs
gamma=6.67e-11
v0=1e4
dt=10000 #manji od br godine
vorb=2*np.pi*aj/(365.25*24*60*60)

#pocetni uslovi (heliocentricni sistem) - letelica
x=[aj+Rz]
y=[0]
z=[0]
#pocetni uslovi - zemlja
xz=[aj]
yz=[0]
zz=[0]
#geocentricni sistem za letelicu
xgc=[Rz] #r-rz: x[0]-xz[0]
ygc=[0]
zgc=[0]

julgod=365.25*24*3600
t=0
omega=2*np.pi/julgod #ugaona brzina
vx=0
vy=vorb #brzina letelice
vz=v0

#phi=list(np.arctan2(y,x))

while t <= julgod:
    t+= dt
    ax=-gamma*Ms/(x[-1]**2+y[-1]**2+z[-1]**2)**(3/2)*x[-1]\
        - gamma*Mz/(xgc[-1]**2+ygc[-1]**2+zgc[-1]**2)**(3/2)*xgc[-1]
    ay=-gamma*Ms/(x[-1]**2+y[-1]**2+z[-1]**2)**(3/2)*y[-1]\
        - gamma*Mz/(xgc[-1]**2+ygc[-1]**2+zgc[-1]**2)**(3/2)*ygc[-1]
    az=-gamma*Ms/(x[-1]**2+y[-1]**2+z[-1]**2)**(3/2)*z[-1]\
        - gamma*Mz/(xgc[-1]**2+ygc[-1]**2+zgc[-1]**2)**(3/2)*zgc[-1]
    vx+=ax*dt
    vy+=ay*dt
    vz+=az*dt
    x.append(x[-1]+vx*dt) #crtamo putanju, dodajemo clanove za iscrtavanje
    y.append(y[-1]+vy*dt)
    z.append(z[-1]+vz*dt)

    lz=omega*t #longituda

    xz.append(aj*np.cos(lz))
    yz.append(aj*np.sin(lz))
    zz.append(0) #jer se zemlja krece po xOy ravni

    #r-rz; ovo radimo jer se zemlja krece i njen polozaj se menja
    xgc.append(x[-1]-xz[-1])
    ygc.append(y[-1]-yz[-1])
    zgc.append(z[-1]-zz[-1])
x1=np.array(x)
y1=np.array(y)
z1=np.array(z)

xz1=np.array(xz)
yz1=np.array(yz)
zz1=np.array(zz)
#3D PLOT
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax.set_xlim3d(-10,10)
#ax.set_ylim3d(-10,10)

plt.plot(xz1/aj,yz1/aj,zz1/aj,'g',label='zemlja') #zemlja
plt.plot(x1/aj,y1/aj,z1/aj,label='letelica') #letelica
plt.plot(0,0,0,'oy',label='sunce') #sunce
plt.legend()
plt.show()