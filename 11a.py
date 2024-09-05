import numpy as np
import time as time
import matplotlib.pyplot as plt

H=3.84e8
g=9.81
dt=1e-4
korak=100
V=0
h=0
while h<H:
    h=0
    V+=korak
    v=V
    while v>=0:
        v-=g*dt
        h+=v*dt
print(V-korak)