import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

GM = 3.98e14 #gravitaciona konstanta*masa
R=6.37e6 #poluprecnik zemlje

V = np.arange(100,1000,100) #zavisnost brzine od visina
H = np.zeros_like(V)

dt=1

Hg = V**2/(2*9.81) # za svaku brzinu uzmemo pocetnu brzinu izracunamo kje ce nam biti analiticko resenje; podrazumeva se da cemo sve vr u nizu kvadrirati i pomnoziti sa 2*9.81

for i,v in enumerate(V):
    y=R
    while v>0:
        v -= GM*dt/y**2
        y+=v*dt
    H[i] = (y-R)/1000

plt.figure()
plt.plot(V,H,'r')
plt.plot(V,Hg/1000,'b') #jer smo H[i] izrazili u km
plt.xlabel('brzina')
plt.ylabel('visina')
plt.show()

"""
zasto bas y-R

pri integraciji uzimamo za granice Rz (poluprecnik zemlje) i Rz+y, nama g zavisi od Rz
na taj nacin g*M se deli sa rastojanjem od centra Zemlje (y**2)
kako nam se g odnosi na ubrzanje mereno iz centra Zemlje i zbog toga y koje mi dobijamo je racunato iz centra zemlje
stoga kada racunamo brzinu racunamo je od centra zemlje isto kao i nase rastojanje y
tada je neophodno da u rezultatu da bismo dobili visinu kpja figurise u H[i]  da oduzmemo poluprecnik zemlje
"""