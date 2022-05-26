from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("#000000")
timmy = Turtle()
timmy.shape("turtle")
timmy.color("#381769")

# #----Draw a square----#
# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)
# #---------------------#
# #--Draw a dashed line-#
# for _ in range(30):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()
# #---------------------#


screen.exitonclick()

# import heroes

# print(heroes.gen())