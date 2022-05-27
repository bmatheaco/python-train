from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
timmy = Turtle()

screen.bgcolor("#000000")
screen.colormode(255)

timmy.shape("turtle")
timmy.color("#381769")
timmy.speed("fastest")


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb = (red, green, blue)
    return rgb


for way in range(0, 361, 5):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(way)


screen.exitonclick()
