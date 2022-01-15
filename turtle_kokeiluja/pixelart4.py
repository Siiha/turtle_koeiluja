import tl,turtle
t = turtle.Turtle()
turtle.colormode(255)
x = 5
y = 10
k = []
for a in range(y):
    l = [[[i,a*x],(0,0,0)] for i in range(0,x*y,x)]
    k.append(l)
v = []
        
