from turtle import Turtle
import random

COLORS = ["firebrick", "salmon", "goldenrod", "olive drab", "light sky blue", "medium purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SPAWN_COR_X = 330
CAR_SPAWN_LIMIT_Y = [-240, 240]


class CarManager:
    def __init__(self):
        self.car_objects = []

    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.resizemode("user")
        car.setheading(180)
        car.turtlesize(stretch_wid=1.0, stretch_len=2.0)
        car.setx(CAR_SPAWN_COR_X)
        car.sety(random.randrange(-240, 240, 20))
        self.car_objects.append(car)

    def drive(self):
        for car in self.car_objects:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_carspeed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def detect_player(self, turtle):
        for car in self.car_objects:
            car_y = car.ycor()
            player_y = turtle.ycor()
            abs_y = abs(car_y - player_y)
            abs_x = abs(car.xcor())
            if abs_y < 18 and abs_x <= 20:
                return False
        return True

    def true_speed(self):
        global STARTING_MOVE_DISTANCE
        if STARTING_MOVE_DISTANCE > 45:
            return True
        return False
