"""
Primenom OKM odrediti heliocentricnu putanju kosmicke letelice koja je sa Zemlje lansirana brzi-
nama od 1km/s do 10km/s (sa korakom od 1km/s) u odnosu na Zemlju, u pravcu i smeru Zemljine

heliocentricne (orbitalne) brzine. PP kruznu putanju Zemlje. Uzeti u obzir samo grav. Sunca i
integraliti za 1 godinu.

a)odstampati odnose vremena integracije kodova (za svaku pocetnu brzinu) za konstantan vremen-
ski korak dt0 i za dt koji je srazmeran rastojanju u au, a u pocetnom trenutku je dt0.
"""

import numpy as np
import time as time
import matplotlib.pyplot as plt

Ms=1.989e30
R=6.378e6
gamma=6.67e-11
aj=1.496e11

julgod=365.25*24*60*60

vzemlja=2*np.pi*aj/julgod
V0=np.arange(0,10000,1000)
odnos=[] #odnos trajanja integracija
dt0=100 #const

for v0 in V0:
    pocetak = time.time()
    x=[aj]
    y=[0]

    vx=0
    vy=vzemlja+v0 #brzina letelice

    t=0
    dt=dt0
    while t<julgod:
        t+=dt

        ax=-gamma*Ms/(x[-1]**2+y[-1]**2)**(3/2)*x[-1]
        ay=-gamma*Ms/(x[-1]**2+y[-1]**2)**(3/2)*y[-1]

        vx +=ax*dt
        vy+=ay*dt

        x.append(x[-1]+vx*dt)
        y.append(y[-1]+vy*dt)
    x=np.array(x)
    y=np.array(y)

    vreme1 = time.time() - pocetak

    #promenljiv dt

    pocetak = time.time()

    x1=[aj]
    y1=[0]

    vx=0
    vy=vzemlja+v0 #brzina letelice

    t=0
    while t<julgod:
        dt = dt0*(x1[-1]**2+y1[-1]**2)**0.5/aj #direktno je srazmeran vektoru pomeraja, pocetni uslov mu je dt=dt0 i zbog srazmernosti mnozimo i skaliramo sa aj
        t+=dt
        ax = -gamma*Ms/(x1[-1]**2+y1[-1]**2)**(3/2)*x[-1]
        ay = -gamma*Ms/(x1[-1]**2+y1[-1]**2)**(3/2)*y[-1]

        vx += ax*dt
        vy += ay*dt

        x1.append(x1[-1]+vx*dt)
        y1.append(y1[-1]+vy*dt)

    x1 = np.array(x1)
    y1 = np.array(y1)

    vreme2 = time.time() - pocetak
    odnos.append(vreme1/vreme2)
print(odnos)

