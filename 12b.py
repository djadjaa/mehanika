import numpy as np
import time as time
import matplotlib.pyplot as plt

H=2000
g=9.81
k=0.17658

v0=0
t=0
dt=0.1
v_as=g/k #asimptotska brzina
h=H
#v nam se menja asimptotski i imacemo priblizavanje pa ce nam uci u beskonacnu petlju
while h>0 and t<200:
    v0+= (g-k*v0)*dt #brzina se povecava pri padu a visina se smanjuje
    h-=v0*dt
    t+=dt

    if abs(v_as-v0)/v_as < 0.01: #relativna greska
        print(t,h)
        break