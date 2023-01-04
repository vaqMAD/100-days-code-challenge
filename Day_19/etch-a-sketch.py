from turtle import Turtle, Screen

turtle = Turtle()

screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)
    
def clear_board():
    screen.resetscreen()


screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear_board, "c")

screen.exitonclick()
