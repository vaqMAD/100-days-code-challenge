from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):

        # Inherit from the turtle class init method
        super().__init__()

        # Set up the food object
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        # Call the spawn food method
        self.spawn_food()

    def spawn_food(self):
        """
        Spawn food at random location at the screen
        """

        random_x = random.randint(-480, 480)
        random_y = random.randint(-480, 480)

        self.goto(random_x, random_y)
