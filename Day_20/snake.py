from turtle import Turtle

# Constans values
# Create list staring positions of snake objects
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Distance to move of snake segments on the board
MOVE_DISTANCE = 20
# Snake head directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):

        # Set up the esnake object
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def add_snake_segment(self, position: tuple):
        """Create snake segments at the given positions 

        Args:
            position (tuple): snake segment coordinates 
        """

        # Create snake object
        snake_segment = Turtle(shape="square")

        # Actions with snake object
        snake_segment.speed(speed="normal")  # Set the snake speed
        snake_segment.penup()  # Set pen to not draw
        snake_segment.resizemode("user")  # Resize snake shape
        snake_segment.shapesize()

        # Set starting positions# Set the size of snake
        snake_segment.goto(position)

        # Set up the snake color
        snake_segment.color("white")

        # Add segment to snake list
        self.snake_segments.append(snake_segment)

    def extend_body(self):
        """
        Extend body of the snake after eating a food 
        """
        self.add_snake_segment(self.snake_segments[-1].position())

    def create_snake(self):
        """ 
        Create a snake object with previously prepared properties 
        """

        # Create starting snake object
        for position in STARTING_POSITIONS:
            self.add_snake_segment(position)

    def move(self):
        """
        Move snake segments to  given coordinates

        The last snake component is going to the position of the penultimate segment
        """

        # Moveing all segments of snake
        for snake_segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snake_segment - 1].xcor()
            new_y = self.snake_segments[snake_segment - 1].ycor()
            self.snake_segments[snake_segment].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        Change head direction to go up with snake body
        """
        # Check is head of snake is not faceing in down direction
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # If true direction change allowed

    def down(self):
        """
        Change head direction to go down with snake body
        """

        # Check is head of snake is not faceing in up direction
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # If true direction change allowed

    def left(self):
        """
        Change head direction to go left with snake body
        """

        # Check is head of snake is not faceing in right direction
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # If true direction change allowed

    def right(self):
        """
        Change head direction to go right with snake body
        """

        # Check is head of snake is not faceing in left direction
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  # If true direction change allowed
