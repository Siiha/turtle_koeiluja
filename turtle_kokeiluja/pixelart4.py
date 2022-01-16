import tl,turtle
t = turtle.Turtle()
turtle.colormode(255)
v = [(255,0,0),(255,100,0),(255,255,0),(255,0,100)]
p = 5
y = 10
t.hideturtle()
def kolmio(x,k,va=0):
    l = []
    if va == 0:
        for a in range(1,k+1):
            l += tl.rivi(0,a*p,a,p,v[0])
    if va == 1:
        for a in range(1,k+1):
            l += tl.rivi(0,a*p*-1,a,p,v[0])
    return l
t.speed(10)
k = tl.rivi(0,0,2,p,v[0])
k+=tl.rivi(10,0,2,5,v[1])
k+=tl.rivi(20,0,2,5,v[0])
k+=tl.rivi(0,5,2,5,v[2])
k+=tl.rivi(10,5,2,5,v[1])
k+=tl.rivi(20,5,2,5,v[2])
k+=tl.rivi(0,10,1,5,v[1])
k+=tl.rivi(5,10,4,5,v[3])
k+=tl.rivi(25,10,1,5,v[1])
for i in k:
    t.color((0,0,0),i[1])
    tl.siirry(i[0][0],i[0][1],t)
    tl.nelio(p,t)
