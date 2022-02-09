from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("forest green")
        self.penup()
        self.setheading(90)

    def start_position(self):
        self.setpos(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        self.hideturtle()
        self.sety(0)
        self.write(arg="Game Over", move=False, align='center', font=("arial", 30, 'normal'))

    def hide_object(self):
        self.hideturtle()

    def crossed_finishline(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
