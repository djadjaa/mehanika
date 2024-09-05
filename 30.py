"""
Odrediti putanju veˇstaˇckog Zemljinog satelita koji je lansiran sa visine od h = 200 km horizontalnom
brzinom od v0 = √γM/(R + h) ≈ 7, 78 km/s, uzimajuci u obzir gravitaciono polje Zemlje, kao i otpor
atmosfere. Balistiˇcki koeficijent letelice je 250 kg/m2, gustina atmosfere na povrˇsini Zemlje ρ0 = 1.23 kg
m3
a skala visina 8, 5km.
a) Koliki ce biti ˇzivotni vek ovog satelita?
b) Kako mu se menjaju brzina i visina sa vremenom?
c) ˇSta se deˇsava sa ˇzivotnim vekom ako se gustina atmosfere udvostruˇci?
d) Kako se menja moment koliˇcine kretanja u odnosu na geocentar?
e) Kako se menja ukupna mehaniˇcka energija letelice?
"""

import numpy as np
import time as time
import matplotlib.pyplot as plt

Mz=5.972e24
Rz=6.378e6
sek=3600*24
gamma=6.67e-11
ro0=1.23
H=8500
BC=250
h=2e5 #pocetna visina
v0=np.sqrt(gamma*Mz/(Rz+h)) #pocetna horizontalna visina

x=[Rz+h] #svejedno je kako postavimo koordinatni sistem
y=[0]
vx=[0]
vy=[v0] # -||-

L=[np.cross([x[-1],y[-1]],[vx[-1],vy[-1]])] #moment impulsa
E=[-gamma*Mz/(x[-1]**2+y[-1]**2)**0.5+(vx[-1]**2+vy[-1]**2)/2] #energija (masa zanemarljiva u odnosu na zemlju pa je ona materijalna tacka)

T=[0] #a
t=0
dt=1

while h>0:
    h=(x[-1]**2+y[-1]**2)**0.5-Rz #trenutna
    ro = ro0*np.exp(-h/H)
    t+=dt
    T.append(t/sek) #skaliracemo sa br sek
    v=(vx[-1]**2+vy[-1]**2)**0.5 #trenutna brzina
    ax=-gamma*Mz/(x[-1]**2+y[-1]**2)**(3/2)*x[-1]-ro/2/BC*v*vx[-1]
    ay=-gamma*Mz/(x[-1]**2+y[-1]**2)**(3/2)*y[-1]-ro/2/BC*v*vy[-1]
    vx.append(vx[-1]+ax*dt)
    vy.append(vy[-1]+ay*dt)
    x.append(x[-1]+vx*dt)
    y.append(y[-1]+vy*dt)

    L.append(np.cross([x[-1],y[-1]],[vx[-1],vy[-1]]))
    E.append(-gamma*Mz/(x[-1]**2+y[-1]**2)**0.5+(vx[-1]**2+vy[-1]**2)/2)
x = np.array(x)
y= np.array(y)
vx=np.array(vx)
vy=np.array(vy)
v=np.sqrt(vx**2+vy**2)
h=np.sqrt(x**2+y**2)-Rz
L=np.array(L)
E=np.array(E)
#zivotni vek
print(t/sek)
#zavisnost brzine i visine tokom vremena
plt.figure()
plt.plot(T,v,'b')
plt.plot(T,h,'r')
plt.show()
#moment kolicine kretanja tokom vremena
plt.figure()
plt.plot(T,L)
plt.show()
#uk meh energija letelice tokom vremena
plt.figure()
plt.plot(T,E)
plt.show()
#putanja letelice
plt.figure()
plt.plot(x/Rz,y/Rz)
plt.show()


