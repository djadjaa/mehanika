import numpy as np
import time as time
import matplotlib.pyplot as plt

H=3.84e8
gamma=6.67e-11
Rz=6.378e6
Mz=5.97e24
Mm=7.348e22
g=9.81
print(np.sqrt(2*gamma*Mz*H/(Rz*H+Rz**2)))
dt=1e-1
korak=100
V=0
h=0
while h<H:
    h=Rz
    V+=korak
    v=V
    while v>=0 and h<H: #H-h
        v+=(-gamma*Mz/h**2+gamma*Mm/(H-h)**2)*dt
        h+=v*dt
print(V)