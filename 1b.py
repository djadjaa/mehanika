import numpy as np
import matplotlib.pyplot as plt

h = 100
t = 0
v = 0
g = 9.81 #m/s^2
#dt = 1e-4
DT = np.arange(1e-4,1e-2,1e-4) #pravi niz vremenskih intervala koji pocinju od 1e-4 i svakom clanu dodaje 1e-4 sve do 1e-2
V = np.zeros_like(DT) #kreira nam se novi niz kao DT gde su ostale vrednosti 0
T = np.zeros_like(DT)

for i,dt in enumerate(DT): #za svaki element iz niza DT (par (i,dt))
    h = 100
    t = 0
    v = 0

    while h > 0:
        h += v * dt
        v -= g * dt
        t += dt
    
    V[i] = v
    T[i] = t

plt.figure(1) #kreiranje
plt.plot(DT,V) #dodavanje tacaka i njihovo povezivanje
plt.xlabel('vremenski korak [s]') #imenovanje koordinata
plt.ylabel('brzina [m]')
plt.title('zavisnost brzine od vremenskog koraka')
#plt.show() - ako imamo samo jedan ispis spajaju se grafici

plt.figure(2) #kreiranje
plt.plot(DT,T) #dodavanje tacaka i njihovo povezivanje
plt.xlabel('vremenski korak [s]') #imenovanje koordinata
plt.ylabel('vreme [s]')
plt.title('zavisnost vremena od vremenskog koraka')
plt.show()