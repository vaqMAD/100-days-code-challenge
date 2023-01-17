from turtle import Turtle


class Traveler(Turtle):

    def __init__(self):
        # Inherit from the turtle class init method
        super().__init__()

        # Set up the traveler object
        self.hideturtle()
        self.speed("fastest")
        self.penup()

    def travel(self, coordinates: tuple):
        """
        Move traveler object to coordinates
        Args:
            coordinates (tuple): trurtle screen coordinates
        """
        self.goto(coordinates)

    def write_state_on_map(self, state_name:str):
        """
        Write current guessed state on the map 

        Args:
            state_name (str): current guessed state name 
        """
        self.write(f"{state_name}", align="center",font=("Courier", "10", "normal"))