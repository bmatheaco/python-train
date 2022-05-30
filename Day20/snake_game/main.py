from turtle import Screen, Turtle
from random import randint
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

start_positions = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for position in start_positions:
    snake_part = Turtle(shape="square")
    snake_part.color("white")
    snake_part.penup()
    snake_part.goto(position)
    snake.append(snake_part)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for part_num in range(len(snake)-1, 0, -1):
        new_x = snake[part_num - 1].xcor()
        new_y = snake[part_num - 1].ycor()
        snake[part_num].goto(new_x, new_y)
    snake[0].fd(20)
    






screen.exitonclick()