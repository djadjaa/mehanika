import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


V = np.arange(50,101,1)
alfa = np.arange(0,91,1)
alfa = np.deg2rad(alfa)
domet = np.zeros([len(V),len(alfa)])
ax=0
ay=-9.81
dt=1e-3
for i in range(0,len(V)):
    for j in range(0,len(alfa)):
        x=0
        y=0
        vx = V[i]*np.cos(alfa[j])
        vy = V[i]*np.sin(alfa[j])

        while(y>=0):
            x += vx*dt
            y += vy*dt

            vx += ax*dt
            vy += ay*dt
        
        domet[i][j] = x

plt.figure()
plt.contour(np.rad2deg(alfa),V,domet,20,cmap=cm.jet)
plt.xlabel('ugao')
plt.ylabel('brzina')
plt.colorbar()
plt.show()


print(domet)
