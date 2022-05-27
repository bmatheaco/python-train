from random import choice, randint
from turtle import Turtle, Screen

color_list = [(210, 151, 98), (131, 158, 205), (151, 70, 52), (77, 92, 138),
              (132, 67, 86), (228, 84, 49), (237, 206, 90), (82, 119, 74),
              (200, 88, 109), (196, 131, 156), (88, 114, 178), (133, 174, 161),
              (156, 216, 167), (150, 148, 54), (74, 49, 41), (58, 52, 115)]

screen = Screen()
timmy = Turtle()

screen.bgcolor("#000000")
screen.colormode(255)

timmy.color("#381769")
timmy.speed("fastest")
timmy.penup()  # don't draw when turtle moves
timmy.hideturtle()

timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, choice(color_list))
    timmy.fd(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.fd(500)
        timmy.setheading(0)


screen.exitonclick()
