from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        # Inherit from the turtle class init method
        super().__init__()

        # Set up the screen object
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)

        # Set up the scoreboard variables
        self.level = 0

        # Call update scorebard fucntion
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Write current score 
        """
        self.write(f"Score: {self.level}", align="center",
                   font=("Courier", "12", "normal"))

    def increase_level(self):
        """
        Increase current score and call update scoreboard function
        """
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """
        Print game over on the screen 
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center",
                   font=("Courier", "12", "normal"))
