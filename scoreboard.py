from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.pencolor("pale violet red")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.score}", move=False, align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def crossed_finish(self):
        self.update_score()
