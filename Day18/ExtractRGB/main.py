from random import choice, randint
from turtle import Turtle, Screen

color_list = [(210, 151, 98), (131, 158, 205), (151, 70, 52), (77, 92, 138),
              (132, 67, 86), (228, 84, 49), (237, 206, 90), (82, 119, 74),
              (200, 88, 109), (196, 131, 156), (88, 114, 178), (133, 174, 161),
              (156, 216, 167), (150, 148, 54), (74, 49, 41), (58, 52, 115)]

position_x = -300
position_y = -200

screen = Screen()
timmy = Turtle()

screen.bgcolor("#000000")
screen.colormode(255)

timmy.color("#381769")
timmy.speed("fastest")
timmy.penup()  # don't draw when turtle moves
timmy.goto(position_x, position_y)  # move the turtle to a location
timmy.hideturtle()


def move_in_line():
    for _ in range(10):
        timmy.dot(20, choice(color_list))
        timmy.fd(50)
    

def move_to_next_line():
    global position_y
    for _ in range(10):
        move_in_line()
        position_y += 50
        timmy.goto(position_x, position_y)


move_to_next_line()


screen.exitonclick()
