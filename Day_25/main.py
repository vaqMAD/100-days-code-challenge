import turtle
from traveler import Traveler
import pandas

# Read all needed tata
data = pandas.read_csv("Day_25/50_states.csv")

# Convert names of states to a list
all_states = data.state.to_list()

# Create the var for game logic
game_on = True
current_score = 0

# Set up all necessary objects
screen = turtle.Screen()
traveler = Traveler()

# Set up the screen object
screen.title("U.S. States Game")
image = "Day_25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Game logic
while game_on:

    # Ask a user for state
    user_answer = screen.textinput(
        title=(f"{current_score}/50 States Correct"), prompt="What is the another state's name?").title()

    # If user answer is Exit
    if user_answer == "Exit":
        game_on = False  # Exit the game
    # Check is current user score < 50
    elif current_score < 50:
        # Check does answer belong to list of states
        if user_answer in all_states:
            # Icrease current player score
            current_score += 1

            # Catch the current state guessed by the user
            state_data = data[data.state == user_answer]

            # Move traveler object to coordinates of the state at the turtle board
            traveler.travel((int(state_data.x), int(state_data.y)))
            # Write the name of the state at this coordinates
            traveler.write_state_on_map(user_answer)
    else:
        game_on = False

screen.exitonclick()
