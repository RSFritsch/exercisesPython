import turtle

t=turtle.Turtle()
turtle.bgcolor('black')
t.pencolor('blue')

t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

forDis=0
dR=0

while(True):
    t.forward(forDis)
    t.right(dR)
    forDis+=3
    dR+=1
    if dR==210:
        break

turtle.done()