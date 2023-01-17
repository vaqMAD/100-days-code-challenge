from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Actions with screen object
screen = Screen()  # Create screen object
screen.setup(1000, 1000)  # Set the board size
screen.title("Snake Game")  # Set the title of game
screen.bgcolor("black")  # Set backgroud color
screen.tracer(0)  # Run the treacer mode

# Create all necessary objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Snake actions
    snake.move()

    # Detect collision with food functionality
    if snake.head.distance(food) < 15:
        food.spawn_food()
        snake.extend_body()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 490 or snake.head.ycor() < -490: # When head will hit the board of the screen 
        scoreboard.game_over() # Print end of game  
        game_on = False # End of game 

    # Detect body collision
    for segment in snake.snake_segments[1:]: 
        if snake.head.distance() < 10: # If snake head is 10 px distance of the any other snake body segment 
            scoreboard.game_over() # Print end of game  
            game_on = False # End of game 
            


screen.exitonclick()
