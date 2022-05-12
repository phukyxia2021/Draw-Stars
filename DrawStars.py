import turtle
s = turtle.Turtle()

s.getscreen().bgcolor("white")
s.penup()

s.goto(-200,100)
s.pendown()

s.color("violet", "orange",)
s.speed(30)

def star(turtle, size):
    if size <= 10:
        return 
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.pensize(2)
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
            turtle.end_fill()
star(s, 360)
turtle.done()