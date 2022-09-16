import turtle

t= turtle.Turtle()
t.pencolor('black')
t.pendown()

def Square(t):
  for i in  range(4):
    t.forward(100)
    t.left(90)

Square(t)

turtle.done()