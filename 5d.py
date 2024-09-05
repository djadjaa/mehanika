import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time as time

GM = 3.98e14 #gravitaciona konstanta*masa
R=6.37e6 #poluprecnik zemlje

V = np.arange(100,1000,100)
vreme = []

dt=1e-4

for i,v in enumerate(V):
    y=R
    pocetak = time.time() #pocetak merenja vremena
    while v>0:
        v -= GM*dt/y**2
        y+=v*dt
    vreme.append(time.time() - pocetak) 
    #sacuvace nam vreme nakon izlaska iz petlje; pocetak je rednost kada je zapoceto merenje tog vremena

plt.figure()
plt.plot(V,vreme,'r') #OK metoda
plt.xlabel('brzina')
plt.ylabel('vreme')
plt.show()
#lista daje potpune rezultate (nezaokruzene), a kod niza se formira implicitna konverzija u int