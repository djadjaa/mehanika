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
v0=10000
dt0=100 #const

#kako su vektori u pitanju, brzina ce nam se menjati u razl trenucima
x=[aj]
y=[0]
vx=[0]
vy=[vzemlja+v0] #brzina letelice

#x y, vx vy -> pocetni moment impulsa; ne racunamo m jer je letelica materijalna tacka ( masa letelice je znatno manja od mase sunca i samim tim je zanemarljiva)

L=[np.cross([aj,0], [0, vzemlja+v0])]

t=0
dt=dt0
while t<julgod:
    t+=dt

    ax=-gamma*Ms/(x[-1]**2+y[-1]**2)**(3/2)*x[-1]
    ay=-gamma*Ms/(x[-1]**2+y[-1]**2)**(3/2)*y[-1]

    vx.append(vx[-1]+ax*dt) #ne mozemo vx +=ax*dt jer smo ih def kao liste
    vy.append(vx[-1]+ay*dt)

    x.append(x[-1]+vx[-1]*dt) #ne mozemo x.append(x[-1]+vx*dt) jer je vx lista
    y.append(y[-1]+vy[-1]*dt)

    #tekuce koordinate vektora x i y i vx i vy
    L.append(np.cross([x[-1],y[-1]],[vx[-1],vy[-1]]))
print(L[0],len(L))