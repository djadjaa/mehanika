import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

GM = 3.98e14 #gravitaciona konstanta*masa
R=6.37e6 #poluprecnik zemlje

v=3000
dt=1e-2
y=R #pocetno rastojanje

#hitac navise
while v>0:
    v -= GM*dt/y**2
    y+=v*dt
print((y-R)/1000) #visina do koje cemo doci