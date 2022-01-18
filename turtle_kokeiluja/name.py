import turtle,tl
t = turtle.Turtle()
p = 5
turtle.colormode(255)
t.speed(10)
t.hideturtle()
#N
def N():
    l = []
    l += tl.vino(0,0,5,p,1,(255,0,0))
    l += tl.pysty(-20,0,4,p,(255,0,0))
    l += tl.pysty(0,0,5,p,(255,0,0))
    return l
#A
def A():
    l = []
    l += tl.vino(10,0,5,p,0,(255,0,0))
    l += tl.vino(50,0,5,p,1,(255,0,0))
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
