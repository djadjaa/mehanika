import numpy as np
import matplotlib.pyplot as plt

h = 1000
t = 0
v = 0
g = 9.81 #m/s^2
dt = 1e-4
H =[] #prazna lista; moze i preko np.array

#za svako h koje izracunamo uradicemo sledece
while h > 0:
    h += v * dt
    v -= g * dt
    t += dt
    H.append(h)

plt.figure(1)
plt.plot(np.zeros_like(H),H,'.r') #postavi crvene tacke da nam budu plotovi
#np.zeros_like - ekvidistancni trenuci - br nula onoliko koliko ima clanova niza H 
plt.show()

#visina ce srazmerno porasti sa vremenom; takodje kako se brzina smanjuje tako se smanjuje i visina

razlike = np.diff(H) #h[i]-h[i-1]
print(razlike)