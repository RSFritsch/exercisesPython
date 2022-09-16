import turtle

t= turtle.Turtle()
n= 7
length= 70

t.pencolor('black')
t.pendown()

def Heptagono(t, n, length):
    angle= 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

Heptagono(t,n,length)

turtle.done()