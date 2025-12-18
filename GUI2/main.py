import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=700)
screen.tracer(0)
player=Player()
screen.listen()
screen.onkey(player.go_up,"Up")
car_manager=CarManager()
score=Scoreboard()
game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()

    if player.finish():
        player.restart()
        car_manager.level_up()
        score.increase()


screen.exitonclick()



