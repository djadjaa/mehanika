import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

GM = 3.98e14 #gravitaciona konstanta*masa
R=6.37e6 #poluprecnik zemlje

V = np.arange(100,1000,100)
T = np.zeros_like(V)
Tg = V/9.81 #(tau = vo/g)

dt=1e-2

for i,v in enumerate(V):
    y=R
    t=0
    while v>0:
        v -= GM*dt/y**2
        y+=v*dt
        t+= dt
    T[i] = t 

plt.figure()
plt.plot(V,T,'r') #OK metoda
plt.plot(V,Tg,'b') #analiticka metoda
plt.xlabel('brzina')
plt.ylabel('vreme')
plt.show()
#primeticemo da se linearno povecava vreme i brzina