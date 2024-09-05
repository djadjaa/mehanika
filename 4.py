import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

v=100
alfa = np.deg2rad(45)
DT = np.arange(1e-2,1,1e-2) #zelimo da vidimo kako odstupanje zavisi od vremenskog koraka
#i kako domet zavisi za ojlerovu i ojler kromerovu metodu
D_o = np.zeros(len(DT))
D_ok = np.zeros_like(DT)

domet = v**2*np.sin(2*alfa)/9.81

ax=0
ay=-9.81

for i,dt in enumerate(DT):
    x=0
    y=0
    vx=v*np.cos(alfa)
    vy=v*np.sin(alfa)

    while y>=0:
        #vektori polozaja
        x+=vx*dt
        y+=vy*dt

        #brzine (ne zavise od x i  y)
        vx+=ax*dt
        vy+=ay*dt

    D_o[i] = x

    x=0
    y=0
    vx=v*np.cos(alfa)
    vy=v*np.sin(alfa)

    while y>=0:
        #zamenjujemo mesta
        vx+=ax*dt
        vy+=ay*dt

        x+=vx*dt
        y+=vy*dt

    D_ok[i]=x

plt.figure()
plt.plot(DT,D_o,'r')
plt.plot(DT,D_ok)
plt.show()

plt.figure()
plt.plot(DT,np.abs(D_o-domet))
plt.plot(DT,np.abs(D_ok-domet),'r')
plt.show()
