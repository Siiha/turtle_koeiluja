import turtle,tl
t = turtle.Turtle()
p = 5
turtle.colormode(255)
def vino(x,y,p,k,va=0,v=(0,0,0)):
    if va == 0:
        return [[(a,b),v] for a,b in zip(range(x,p*k+x,k),range(y,p*k+x,k))]
    if va == 1:
        return [[(a,b),v] for a,b in zip(range(x,p*k*-1,-k),range(y,p*k,k))]

#N
def N():
    l = []
    l += vino(0,0,5,p,1,(255,0,0))
    l += tl.pysty(-20,0,4,p,(255,0,0))
    l += tl.pysty(0,0,5,p,(255,0,0))
    return l
#A
def A():
    l = []
    l += vino(10,0,5,p,0,(255,0,0))
    l += vino(50,0,5,p,1,(255,0,0))
    l += tl.rivi(25,10,3,p,(255,0,0))
    return l
def II():
    l = []
    l+= tl.pysty(-40,0,5,p,(255,0,0))
    l+= tl.pysty(-30,0,5,p,(255,0,0))
    return l
def S():
    l = [[(-50,20),(255,0,0)]]
    l += tl.pysty(-55,10,3,p,(255,0,0))
    l += tl.pysty(-50,0,3,p,(255,0,0))
    l+=[[(-55,0),(255,0,0)]]
    return l
k = S()+II()+N()+A()
for i in k:
    t.color((0,0,0),i[1])
    tl.siirry(i[0][0],i[0][1],t)
    tl.nelio(p,t)
