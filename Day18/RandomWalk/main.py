from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
timmy = Turtle()

screen.bgcolor("#000000")
screen.colormode(255)

timmy.shape("turtle")
timmy.color("#381769")
timmy.speed("fastest")
timmy.pensize(15)
timmy.ht()

ways = [90, 180, 270, 360]

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb = (red, green, blue)
    return rgb

while True:
    timmy.pencolor(random_color())
    timmy.setheading(choice(ways))
    timmy.forward(20)
