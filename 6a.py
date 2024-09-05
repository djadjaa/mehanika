import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

g=-9.81
beta=np.deg2rad(-30) #u ovoj orijentaciji je koordinatni sistem
v=300
alfa=np.deg2rad(50)
dt=1e-2
x=[0]
y=[0]

vx=v*np.cos(alfa)
vy=v*np.sin(alfa)

#beta i y su negativni
while x[-1]==0 or y[-1]>np.tan(beta)*x[-1]: #jer je beta neg pa je >
    #OK metoda
    vy+=g*dt
    X = x[-1]+vx*dt
    x.append(X) #dodajemo na kraj pa je -1 u petlji
    Y = y[-1]+vy*dt
    y.append(Y)

#domet
domet = x[-1]/np.cos(beta)
x=np.array(x)
y=np.array(y)
padina=x*np.tan(beta)

#putanja
plt.figure()
plt.plot(x,y,'r')
plt.plot(x,padina)
plt.show()