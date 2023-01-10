from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20



class Voyager(Turtle):

    def __init__(self):
        # Inherit from the turtle class init method
        super().__init__()

        # Set up the voyager object
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_to_starting_position(self):
        """
        Move voyager object to starting position
        """
        self.goto(STARTING_POSITION)

    def move(self):
        """
        Move voyager object forward of the given move distance value 
        """
        self.forward(MOVE_DISTANCE)
