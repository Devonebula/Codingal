import turtle
import random
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.color("white")
t.shape("turtle")
t.pencolor("red")
t.pensize(3)
a=1
b=random.choice(["red", "green", "yellow", "white", "black", "orange"])

for i in range(100):
    
    t.circle(a)
    a=a+5
    t.pencolor(random.choice(["red", "green", "yellow", "white", "black", "orange"]))
turtle.done()