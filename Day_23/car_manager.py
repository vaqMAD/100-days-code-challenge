from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):

        # List of all cars
        self.all_cars = []

        # The current speed of  car
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Create car at the random y coordinates, with a random frequency ranging from 1 to 6
        """

        # Create car with random frequency
        random_spawn = random.randint(1, 6)  # Generate random number
        if random_spawn == 1:  # If random number is equal to 1
            new_car = Turtle("square")  # Create car

            # Set up the car object
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=1.5)
            new_car.color(random.choice(COLORS))

            # Set up the car location
            radom_y = random.randint(-250, 250)
            new_car.goto(300, radom_y)

            # Append car to all cars list
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Move cars fom the all cars list 
        """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def leve_up(self):
        """
        Increase game difficulty - cars will go faster
        """
        self.car_speed += MOVE_INCREMENT
