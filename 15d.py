import numpy as np
import time as time
import matplotlib.pyplot as plt

CdS=0.5
ro=1.23
g=9.81
H=10000 #krajnja visina
m=250

h_array=np.arange(100,10000,100)

dt=0.1
BC=m/CdS

#brzine sa i bez otpora
vbo=np.zeros_like(h_array)
vo=np.zeros_like(h_array)
wo=np.zeros_like(h_array) #rad sa otporom
wrke=np.zeros_like(h_array) #rad za racunanje razlika kinetickih energija

for i, h1 in enumerate(h_array):
    #bez otpora
    h=h1 #pocetni uslovi
    v=0
    while h>=0:
        v+=g*dt
        h-=v*dt
    vbo[i]=v

    #sa otporom
    h=h1
    v=0

    hh=[]
    w=0
    while h>=0:
        RO=ro*np.exp(-h/H)
        a0=-0.5*RO*v**2/BC
        v+=(g+a0)*dt
        h-=v*dt
        hh.append(h)
        if len(hh)>1:
            #rad PO DEFINICIJI
            w+=m*a0*(hh[-2]-hh[-1]) #+ je jer je a0 - 
    vo[i]=v
    wo[i]=w
    wrke[i]=0.5*m*(vo[i]**2-vbo[i]**2)
print(wo[-1])
print(wrke[-1])

"""plt.figure()
plt.plot(h_array, vbo, 'r', label='bez otpora')
plt.plot(h_array, vo, 'b', label='sa otporom')
plt.legend()
plt.xlabel('visina')
plt.ylabel('brzina udara o tlo')
plt.show()"""