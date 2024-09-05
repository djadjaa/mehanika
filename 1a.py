#primenom ok metode odrediti brzinu kojom telo udara o tlo i vreme pada pri slobodnom padu sa proizvoljne visine h
g=-9.81
h=100
v=0
t=0
dt=1e-4
while h>0:
    h = h+v*dt
    v = v+g*dt
    t += dt 
print('h = ', h, '\n v= ', v, '\n t= ', t)
#brzina ce nam biti negativna zbog slobodnog pada i suprotna je y osi (da je istog pravca kao y osa, bila bi pozitivna)