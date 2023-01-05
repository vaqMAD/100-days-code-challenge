from turtle import Screen
from snake import Snake
import time

# Actions with screen object
screen = Screen()  # Create screen object
screen.setup(1000, 1000)  # Set the board size
screen.title("Snake Game")  # Set the title of game
screen.bgcolor("black")  # Set backgroud color
screen.tracer(0)  # Run the treacer mode

# Create snake object
snake = Snake()

# Screen event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Create var for while loop
game_on = True

# Logic of game
while game_on:
    # Screen update actions
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
