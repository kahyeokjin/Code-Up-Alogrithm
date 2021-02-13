import turtle as t

def polygon(n):
    for x in range(n):
        t.fd(50)
        t.lt(360/n)

def polygon2(n,a):
    for x in range(n):
        t.fd(a)
        t.lt(360/n)


t.speed(0)
polygon(3)
polygon(5)

t.up()
t.fd(100)
t.down()

polygon2(3,75)
polygon2(5,100)
