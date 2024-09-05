import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #m/s^2
dt = 1e-4 #fiksiramo vremenski korak
H = np.linspace(10,1000,100) #formiramo niz visina; slicno kao arange, s tim da je razlika sto kod arangea definise se velicina koraka a kod linspacea broj koraka
# 100 = len(H); izmedju 10 i 1000 bice 100 vrednosti
V = np.zeros_like(H)
T = np.zeros_like(H)

for i,h in enumerate(H): #prebrojava elemente u nizu H tako da varijabla i ima indeks, a varijabla h vr iz niza H(npr (10,20,30) => (0,10) (1,20) (2,30))
    t = 0
    v = 0

    while h > 0:
        h += v * dt
        v -= g * dt
        t += dt
    
    V[i] = v
    T[i] = t

plt.figure(1)
plt.plot(H,V)
plt.xlabel('visina')
plt.ylabel('brzina [m]')
plt.title('zavisnost brzine od visine')

plt.figure(2) #kreiranje
plt.plot(H,T) #dodavanje tacaka i njihovo povezivanje
plt.xlabel('visina') #imenovanje koordinata
plt.ylabel('vreme [s]')
plt.title('zavisnost vremena od visine')
plt.show()

"""
drugi nacin:
H = np.array([])
H=[]
"""