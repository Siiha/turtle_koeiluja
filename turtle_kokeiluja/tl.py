import turtle,math
from itertools import product

def neighbours(cell,size):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c
def siirry(x,y,t):
    t.penup()
    t.goto(x,y)
    t.pendown()
def kartta(x,y,c=(255,255,255)):
    return [[c for i in range(x)] for i in range(y)]
def varita(k,size):
    for a in range(size):
        for b in range(size):
            ab = (a,b)
            n = list(neighbours(ab,size))
            r = round(sum([k[i[0]][i[1]][0] for i in n])/len(n))
            g = round(sum([k[i[0]][i[1]][1] for i in n])/len(n))
            B = round(sum([k[i[0]][i[1]][2] for i in n])/len(n))
            k[a-size][b-size]=(r,g,B)

def neliojuuri(k,x):
    for a in range(x):
        for b in range(x):
            k[a][b] = (round(math.sqrt(k[a][b][0])),round(math.sqrt(k[a][b][1])),round(math.sqrt(k[a][b][2])))
def nelio(x,t):
    t.begin_fill()
    for a in range(4):
        t.forward(x)
        t.right(90)
    t.end_fill()
def rivi(x,y,p,k,v):
    return [[(i+x,y),v] for i in range(0,k*p,k)]
def pysty(x,y,p,k,v):
    return [[(x,y+i),v] for i in range(0,k*p,k)]
def vino(x,y,p,k,va=0,v=(0,0,0)):
    if va == 0:
        return [[(a,b),v] for a,b in zip(range(x,p*k+x,k),range(y,p*k+x,k))]
    if va == 1:
        return [[(a,b),v] for a,b in zip(range(x,p*k*-1,-k),range(y,p*k,k))]

