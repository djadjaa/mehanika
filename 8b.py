import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

g=9.81
Hsp = 100
d=15
dt=1e-3

alfa=np.arctan(Hsp/d)
Vomin=np.sqrt(g*Hsp/(2*np.sin(alfa)**2))
Vo = np.arange(10,35,5)
ALFA = np.deg2rad(np.arange(70,95,5))


X = [[[] for column in range(len(ALFA))] for row in range(len(Vo))]
Y = [[[] for column in range(len(ALFA))] for row in range(len(Vo))]
Xsp = [[[] for column in range(len(ALFA))] for row in range(len(Vo))]
Ysp = [[[] for column in range(len(ALFA))] for row in range(len(Vo))]

for i,v0 in enumerate(Vo):
    for j,alfa in enumerate(ALFA):
        xks=0
        yks=0
        vxks=Vomin*np.cos(alfa)
        vyks=Vomin*np.sin(alfa)

        xsp=d
        ysp=Hsp
        vsp=0#ne uzimamo vx u obzir jer je x const

        while xks<d and ysp>=0 and yks>=0:
            vyks-=g*dt
            xks+=vxks*dt
            yks+=vyks*dt
            
            vsp-=g*dt
            ysp+=vsp*dt

            Xsp[i][j].append(xsp)
            Ysp[i][j].append(ysp)
            X[i][j].append(xks)
            Y[i][j].append(yks)

fig = plt.figure(figsize=(14,12),layout = 'constrained') #svaki grafik ostaje uokviren
for i in range(len(Vo)):
    for j in range(len(ALFA)):
        ax=fig.add_subplot(len(Vo),len(ALFA),len(ALFA)*i+j+1)
        ax.plot(X[i][j],Y[i][j],'.')
        ax.plot(Xsp[i][j],Ysp[i][j],'.r')
        v = Vo[i]
        a = np.rad2deg(ALFA[j])
        ax.set_title(f'a = {"%0.1f" % a}, v = {"%0.1f" % v}')
plt.show()

