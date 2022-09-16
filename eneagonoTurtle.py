import turtle

t= turtle.Turtle()
t.pencolor('black')
t.pendown()

def Polygon(t):
    for i in range(9):
        t.forward(100)
        t.left(40)

Polygon(t)

turtle.done()