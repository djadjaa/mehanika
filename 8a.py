import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

g=9.81
Hsp = 100
d=50
dt=1e-3

alfa=np.arctan(Hsp/d)
Vomin=np.sqrt(g*Hsp/(2*np.sin(alfa)**2))
xks=0
yks=0
vxks=Vomin*np.cos(alfa)
vyks=Vomin*np.sin(alfa)

xsp=d
ysp=Hsp
vsp=0#ne uzimamo vx u obzir jer je x const
x=[] #liste za kosi hitac i slobodan pad
y=[]
xs=[]
ys=[]
while xks<d and ysp>=0 and yks>=0:
    vyks-=g*dt
    xks+=vxks*dt
    yks+=vyks*dt
    
    vsp-=g*dt
    ysp+=vsp*dt

    xs.append(xsp)
    ys.append(ysp)
    x.append(xks)
    y.append(yks)

plt.figure()
plt.plot(x,y,'.')
plt.plot(xs,ys,'.r')
plt.show()


