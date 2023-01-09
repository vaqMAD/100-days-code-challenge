from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):

        # Inherit from the turtle class init method
        super().__init__()

        # Set the necessary values
        self.score = 0

        # Set up the scoreboard object
        self.penup()
        self.hideturtle()
        self.goto(0, 450)
        self.color("white")

        # call the update scoreboard method
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Write current score 
        """
        
        self.write(f"Score: {self.score}", align="center",
                   font=("Courier", "24", "normal"))

    def increase_score(self):
        """
        Increase current score and call update scoreboard function
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """
        Print game over on the screen 
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center",
                   font=("Courier", "24", "normal"))
