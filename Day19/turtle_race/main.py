from turtle import Turtle, Screen
from random import choice, randint

is_race_on = False

screen = Screen()

screen.bgcolor("#000000")
screen.colormode(255)
screen.setup(500, 400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
all_turtles = []
initial_y = -100


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, initial_y)
    all_turtles.append(new_turtle)
    initial_y += 40

if user_bet:
    is_race_on = True

while is_race_on:



    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won. The {winner_color} turtle is the winner")
            else:
                print(f"You've lost. The {winner_color} turtle is the winner")

        random_distance = randint(0, 10)
        turtle.fd(random_distance)

screen.exitonclick()
