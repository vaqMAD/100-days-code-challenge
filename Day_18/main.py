from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("purple")

for _ in range(5): 
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


screen = Screen()
screen.exitonclick()