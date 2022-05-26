from turtle import Turtle, Screen
import random

screen = Screen()
timmy = Turtle()

screen.bgcolor("#000000")
timmy.shape("turtle")
timmy.color("#381769")
timmy.speed(8)
timmy.penup()  # don't draw when turtle moves
timmy.goto(0, 200)  # move the turtle to a location
timmy.pendown()  # draw when the turtle moves

def draw_shape(num_side):
    angle = 360/num_side
    for i in range(num_side):
        timmy.right(angle)
        timmy.forward(50)


num_side = 3
colours = ["Blue", "#381769", "#1E90FF",
           "#00CED1", "#00FF00", "teal",
           "gold", "dark red", "ghost white",
           "magenta", "hot pink", "orchid",
           "saddle brown", "maroon", "dark orange",
           "navy", "dim gray", "cyan", "steel blue"]

while True:
    timmy.color(random.choice(colours))
    draw_shape(num_side)
    num_side += 1
