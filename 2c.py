g=9.81
v=100
h=0
dt=1e-3
t_penjanja=0
t_padanja=0
#znamo da je brzina veca pri penjanju a manja pri padanju
while h>=0:
    h+=v*dt
    v-=g*dt
    if v>0:
        t_penjanja += dt
    else:
        t_padanja += dt
print(t_penjanja/t_padanja)