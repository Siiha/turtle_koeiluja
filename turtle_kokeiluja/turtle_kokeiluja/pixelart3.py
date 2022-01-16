import turtle,tl,random,math
t = turtle.Turtle()
t.width(1)
t.speed(10)
p = 5
kp = 25
ka = kp*p
k = tl.kartta(kp,kp)
turtle.bgcolor(0,0,0)
def arvo(x,y):
    return random.randint(x,y)
for a in range(round(ka/2)):
    k[random.randint(0,kp-1)][random.randint(0,kp-1)]=(arvo(0,255),arvo(0,255),arvo(0,255))
for i in range(2):
    tl.varita(k,kp)
t.hideturtle()
turtle.colormode(255)
def nelio(x,y,z):
    t.color(k[y][z])
    t.begin_fill()
    for a in range(4):
        t.forward(x)
        t.right(90)
    t.end_fill()
x,y = 0,0
for a in range(0,ka,p):
    y = 0
    for b in range(0,ka,p):
        tl.siirry(a,b,t)
        nelio(p,x,y-1)
        tl.siirry(a,b,t)
        y += 1
    x += 1  
t.getscreen().getcanvas().postscript(file="pxart3.ps")
