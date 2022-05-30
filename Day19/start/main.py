from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
screen = Screen()

screen.bgcolor("#000000")
screen.colormode(255)

tim.shape("turtle")
tim.color("#381769")
tim.speed("fastest")


def move_forwards():
    tim.fd(10)


def move_backwards():
    tim.bk(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(move_right, "d")


screen.onkey(clear, "c")

# screen.onkeypress(move_forwards, "up")
# screen.onkeypress(move_left, "left")
# screen.onkeypress(move_backwards, "down")
# screen.onkeypress(move_right, "right")


screen.exitonclick()
