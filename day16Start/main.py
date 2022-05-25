# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkViolet")
# timmy.fd(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur", "Doduo"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass", "Flying"])

table.align = "l"

print(table)
