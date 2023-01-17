from turtle import Turtle, Screen
import random

is_race_on = False

# Screen set up
screen = Screen()
screen.setup(width=500, height=400)

# Catch the user input
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race (red, green, blue) ? Enter a color : ")

# Required params to execute
y_positions = [-150, 0, 150]
turtle_colors = ["red", "green", "blue"]
all_turtles = []


for turtle_index in range(0, 3):
    # Creating and set up turtle  1
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[turtle_index])
    # Actions to set before race with turtle 1
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(
                    f"You've won! The {turtle.pencolor()} turtle is the winner")
            else:
                print(
                    f"You've lost! The {turtle.pencolor()} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
