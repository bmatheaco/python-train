from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle(shape="turtle")
screen = Screen()

screen.bgcolor("#000000")
screen.colormode(255)
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

initial_x = -230
initial_y = -100
color_index = 0


def move_to_start(timmy):
    timmy.color(colors[color_index])
    timmy.penup()
    timmy.goto(initial_x, initial_y)


red = tim.clone()
green = tim.clone()
blue = tim.clone()
yellow = tim.clone()
purple = tim.clone()
orange = tim.clone()

turtles = [red, green, blue, yellow, purple, orange]

for t in turtles:
    move_to_start(t)
    color_index += 1
    initial_y += 40


screen.exitonclick()
