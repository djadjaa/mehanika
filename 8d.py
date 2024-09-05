import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

g=9.81
Hsp = 100
d=200
dt=1e-3

#alfa=np.arctan(Hsp/d)
#Vomin=np.sqrt(g*Hsp/(2*np.sin(alfa)**2))
Vo = np.arange(200,500,10)
ALFA = np.deg2rad(np.arange(10,80,2))

alfa_optimalno = np.zeros(len(Vo))
brzina_pogotka = np.zeros(len(Vo))
visina_pogotka = np.zeros(len(Vo))

for i in range(len(Vo)):
    razlika_visina = np.zeros(len(ALFA)) #ili zeros_like(ALFA)
    h_pogotka = np.zeros(len(ALFA))
    v_pogotka = np.zeros(len(ALFA))
    for j in range(len(ALFA)):
        #kosi hitac
        xks=0
        yks=0
        vxks=Vo[i]*np.cos(ALFA[j])
        vyks=Vo[i]*np.sin(ALFA[j])
        #slobodan pad
        xsp=d
        ysp=Hsp
        vsp=0 #ne uzimamo vx u obzir jer je x const

        while xks<d and yks>=0 and ysp>=0:
            #kosi hitac
            vyks-=g*dt
            xks+=vxks*dt
            yks+=vyks*dt
            #slobodan pad
            vsp-=g*dt
            ysp+=vsp*dt

        razlika_visina[j]=np.abs(yks-ysp)
        h_pogotka[j]=ysp
        v_pogotka[j]=np.sqrt(vxks**2+vyks**2)

    alfa_optimalno[i]=ALFA[np.argmin(razlika_visina)] #minimalan arg u nizu koj trazimo u ALFA
    visina_pogotka[i]=h_pogotka[np.argmin(razlika_visina)]
    brzina_pogotka[i]=v_pogotka[np.argmin(razlika_visina)]
v_min=Vo[np.argmin(visina_pogotka)]
plt.figure()
plt.plot(Vo,np.rad2deg(alfa_optimalno))
plt.xlabel('poc brzina')
plt.ylabel('poc ugao - opt vr')

plt.figure()
plt.plot(Vo,brzina_pogotka)
plt.xlabel('poc brzina')
plt.ylabel('brzina pogotka')

plt.figure()
plt.plot(Vo,visina_pogotka)
plt.plot(v_min,visina_pogotka[np.argmin(np.abs(visina_pogotka))],'or')
plt.xlabel('poc brzina')
plt.ylabel('visina pogotka')

plt.show()