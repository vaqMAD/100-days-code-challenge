from turtle import Turtle
# Create list staring positions of snake objects
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 


class Snake():

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        
        # Create starting snake object
        for position in STARTING_POSITIONS:
            # Create snake object
            snake_segment = Turtle(shape="square")

            # Actions with snake object
            snake_segment.speed(speed="normal")  # Set the snake speed
            snake_segment.penup()  # Set pen to not draw
            snake_segment.resizemode("user")  # Resize snake shape
            snake_segment.shapesize(0.75, 1, 1)
            snake_segment.goto(position)  # Set starting positions# Set the size of snake

            # Set up the snake color
            snake_segment.color("white")

            # Add segment to snake list
            self.snake_segments.append(snake_segment)

    def move(self):

        # Moveing snake
        for snake_segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snake_segment - 1].xcor()
            new_y = self.snake_segments[snake_segment - 1].ycor()
            self.snake_segments[snake_segment].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN : 
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP : 
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT : 
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT : 
            self.head.setheading(RIGHT)
