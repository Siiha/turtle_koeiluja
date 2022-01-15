import tl,turtle,random,math
turtle.colormode(255)
p = turtle.Turtle()
p.speed(10)
s = 10
t = 3
k = tl.kartta(s,s)
turtle.hideturtle()
p.hideturtle()
l = []
for i in range(round(s*(s/3))):
    k[random.randint(0,s-1)][random.randint(0,s-1)]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
for c in range(t):
    tl.varita(k,s)
    l.append(k)
    for a in range(s):
        for b in range(s):
            p.color(k[a][b])
            tl.siirry(a,b,p)
            p.begin_fill()
            for a in range(4):
                p.forward(1)
                p.right(90)
            p.end_fill()
    turtle.getscreen().getcanvas().postscript(file='o'+str(c)+'.ps')      
    turtle.resetscreen()
    p.hideturtle()
    turtle.hideturtle()
for a in l[0]:
    for b in a:
        for c in b:
            c = math.sqrt(c)
for a in range(s):
    for b in range(s):
        p.color(l[0][a][b])
        tl.siirry(a,b,p)
        p.forward(1)
turtle.getscreen().getcanvas().postscript(file='neliojuuri.ps')
