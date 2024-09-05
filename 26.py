"""
Primenom OKM odrediti heliocentricknu putanju kosmicke letelice koja je sa Zemlje lansirana
brzinom 10km/s (u odnosu na Zemlju) u smeri Zemljine orbitalne brzine. pretpostaviti da se
Zemlja krece po kruznoj putanji oko Sunca i da na letelicu deluje samo gravitaciono polje Sunca
orbnutno prop. rastojanju letelice od Sunca. Odrediti period letelice.

pps da imamo grav polje sunca
"""
import numpy as np
import time as time
import matplotlib.pyplot as plt

Ms=1.989e30
Rz=6.378e6
aj=1.5e11 #astronomska jedinica
gamma=6.67e-11
v0=1e4
dt=100000 #manji od br godine
vorb=2*np.pi*aj/(365.25*24*60*60)
#pocetni uslovi (heliocentricni sistem)
x=[aj+Rz]
y=[0]
z=[0]

vx=0
vy=v0+vorb #brzina letelice
vz=0

phi=list(np.arctan2(y,x))

while len(phi)==1 or (len(phi)>1 and phi[-1]>phi[-2]):
    ax=-gamma*Ms/(x[-1]**2+y[-1]**2)**(3/2)*x[-1]
    ay=-gamma*Ms/(x[-1]**2+y[-1]**2)**(3/2)*y[-1]
    vx+=ax*dt
    vy+=ay*dt
    x.append(x[-1]+vx*dt) #crtamo putanju, dodajemo clanove za iscrtavanje
    y.append(y[-1]+vy*dt)
    phi.append(np.mod(np.arctan2(y[-1],x[-1]),2*np.pi)) #definisanje citave putanje(nacrtace nam se polovina jer nece obracunati negativni deo)
x1=np.array(x)
y1=np.array(y)
#3D PLOT
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
ax.set_xlim3d(-10,10)
ax.set_ylim3d(-10,10)
plt.plot(x1/aj,y1/aj,np.zeros(len(x1)))
plt.plot(0,0,0,'oy') #sunce
plt.plot(1,0,0,'og') #zemlja
plt.plot(0,1,0,'og')
plt.show()