import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

g=-9.81
beta=np.deg2rad(np.arange(-30,0))
v=300
alfa=np.deg2rad(np.arange(0,50))
dt=1
domet = np.zeros([len(beta),len(alfa)]) #matrica od br uglova
for i in range(len(beta)):
   for j in range(len(alfa)):
    x=0;y=0   
    vx=v*np.cos(alfa[j])
    vy=v*np.sin(alfa[j])

    while x==0 or y>np.tan(beta[i])*x: #jer je beta neg pa je >
        vy+=g*dt
        x+=vx*dt
        y+=vy*dt

    domet[i][j] = x/np.cos(beta[i])

plt.figure()
plt.contourf(np.rad2deg(alfa),np.rad2deg(beta),domet,20,cmap=cm.jet)
plt.xlabel('alfa')
plt.ylabel('beta')
plt.colorbar()
plt.show()

#alfa = 30 -> pri manjem beta odnosno vecem nagibu ce se domet pomeriti za vece alfa