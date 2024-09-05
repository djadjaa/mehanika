import numpy as np
import time as time
import matplotlib.pyplot as plt

H=2000
g=9.81
k=0.17658

#zavisnost brzine od vremena
V=[]
T=[]

v0=0
t=0
dt=0.1
h=H
#v nam se menja asimptotski i imacemo priblizavanje pa ce nam uci u beskonacnu petlju
while h>0 and t<200:
    v0+= (g-k*v0)*dt #brzina se povecava pri padu a visina se smanjuje
    h-=v0*dt
    t+=dt

    V.append(v0)
    T.append(t)

plt.figure()
plt.plot(T,V,label='trenutna brzina')
plt.plot(T, np.ones(len(T))*g/k, '--r',label='asimptotska brzina') #kada t->inf tj asimptotska brzina
plt.legend()
plt.show()
