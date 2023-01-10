from turtle import Screen
from player import Voyager
from scoreboard import Scoreboard
from car_manager import CarManager
import time


# Set up the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Set up the necessary objects
player = Voyager()
scoreboard = Scoreboard()
car_manager = CarManager()

# Screen event listeners
screen.listen()
screen.onkey(player.move, "w")


# Var for while loop
game_on = True

# Logic of game
while game_on:
    
    # Screen update actions
    time.sleep(0.1)
    screen.update()
    
    # Car manager actions 
    car_manager.create_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20: # If player hit the car 
            scoreboard.game_over() # Print end of game  
            game_on = False # End of game 

    # Check is player crossed the road
    if player.ycor() > 280: # If player crossed the road 
        player.move_to_starting_position() # Go to starting position
        car_manager.leve_up() # Lelvel up the scoreboard 
        scoreboard.increase_level() # Increase difficulty level

    car_manager.move_cars()
screen.exitonclick()
