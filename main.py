import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_over = Player()
game_over.hide_object()
player1 = Player()
player1.start_position()
screen.onkeypress(fun=player1.move, key="Up")
screen.onkeypress(fun=player1.move, key="w")
car = CarManager()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
screen.update()
game_is_on = True
loops = 0
while game_is_on:
    if player1.crossed_finishline():
        player1.start_position()
        car.increase_carspeed()
        scoreboard.update_score()
        scoreboard.update_scoreboard()
    loops += 1
    if not car.true_speed():
        if loops % 6 == 0:
            car.create_car()
    else:
        if loops % 3 == 0:
            car.create_car()
    car.drive()
    game_is_on = car.detect_player(player1)
    if not game_is_on:
        game_over.game_over()
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
