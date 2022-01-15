import tl,turtle
t = turtle.Turtle()
turtle.colormode(255)
v = [(255,0,0),(255,100,0),(255,255,0),(255,0,100)]
p = 5
y = 10
t.hideturtle()
def kolmio(x,va=0):
    y = []
    if va == 0:
        for a in range(1,x+1):
            y += tl.rivi(0,a*p,a,p,v[0],t)
    if va == 1:
        for a in range(1,x+1):
            y += tl.rivi(0,a*p*-1,a,p,v[0],t)
    return y
k = kolmio(10,1)
t.speed(10)
for i in k:
    t.color(i[1])
    tl.siirry(i[0][0],i[0][1],t)
    tl.nelio(p,t)
