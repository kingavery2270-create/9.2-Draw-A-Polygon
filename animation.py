from turtle import *
import random

def generate_random_hex_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

    
def playing_area():
    pen = Turtle()
    pen.ht()
    pen.color("white")
    pen.speed(0)
    pen.goto(-240,240) 
    pen.begin_fill()
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()

def move_forward(turtle):
    turtle.fd(5)

    if turtle.xcor() > 235 or turtle.xcor() < -235:
        turtle.speed(0)
        turtle.setheading(180 - turtle.heading())
        turtle.fd(10)
        turtle.speed(1)
        turtles.append(create_turtle())

    if turtle.ycor() > 235 or turtle.ycor() < -235:
        turtle.speed(0)
        turtle.setheading(-turtle.heading())
        turtle.speed(1)
        turtles.append(create_turtle())

    return turtles
        
def move_xy(turtle,deltax,deltay):
    newX = turtle.xcor() + deltax
    newY = turtle.ycor() + deltay

    #out of bounds on right or left
    if newX > 240 or newX < -240:
        deltax *= -1
        newX = turtle.xcor()
    #out of bounds up or down
    if newY > 240 or newY < -240:
        deltay *= -1
        newY = turtle.ycor()
    turtle.goto(newX,newY)
    return deltax, deltay

def create_turtle():
    yertle = Turtle()
    yertle.color(generate_random_hex_color())   
    yertle.shape('circle')
    yertle.seth(random.randint(0,360))
    return yertle  

def create_player():
    global player
    player = Turtle()
    player.color(generate_random_hex_color())   
    player.shape('turtle')
    player.seth(random.randint(0,360))

# def up():   
#     global player
#     player.seth(90)
#     player.fd(10)     

def left():
    global player
    player.lt(10)
    

def right():
    global player
    player.rt(10)
    

# def down():
#     global player
#     player.seth(-90)
#     player.fd(10)


screen = Screen()
screen.bgcolor("Black")
screen.setup(500,500)
screen.listen()
screen.onkey(create_player,'space')
screen.onkey(up,'w')
screen.onkey(right,'d')
screen.onkey(down,'s')
screen.onkey(left,'a')
playing_area()

player = None

yertle = Turtle()
yertle.color(generate_random_hex_color())   
yertle.shape('circle')
yertle.seth(random.randint(0,360))
deltax = random.randint(-5,5)
deltay = random.randint(-5,5)

turtles = [yertle]

while True:
    if player != None:
        move_forward(player)
    for turtle in turtles:
        turtles = move_forward(turtle)
        if player != None:
            if player.distance(turtle) <= 20:
                turtle.ht()
                turtles.remove(turtle) 









screen.exitonclick()