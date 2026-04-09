from turtle import *

def equal_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(100/sides)
        turtle.right(360/sides)
    turtle.end_fill()

def unknown_quad(turtle,sides):
    turtle.begin_fill()
    for i in range(4):
        turtle.goto(100,50)
        turtle.goto(123,-33)
        turtle.goto(-35,-66)
    turtle.end_fill()

def trapezoid(turtle,sides):
    turtle.begin_fill()
    turtle.forward(100/sides)
    turtle.right(67)
    turtle.forward(20)
    turtle.setheading(180)
    turtle.forward(50)
    turtle.home()
    turtle.end_fill()
def square(turtle,sides):
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(25)
        turtle.right(90)
    turtle.end_fill()
screen = Screen()
screen.bgcolor("teal")
screen.setup(400,400)

name = Turtle()
name.ht()
name.speed(0)
# name.teleport(0,100)

pen = Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()

while True:
    sides = int(input("How many sides do you want?  "))
    pen.clear()
    if sides == 4:
        parallelsides = int(input("How many parallel sides do you want?  "))
        if parallelsides == 0:
            unknown_quad(pen,4)
        elif parallelsides == 2:
            trapezoid(pen,4)
        elif parallelsides == 4:
            square(pen,4)
    else:
        equal_polygon(pen,sides)




screen.exitonclick()