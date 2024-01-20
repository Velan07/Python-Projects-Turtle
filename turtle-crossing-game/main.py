import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_car()

    for cars in car.all_car:
        if cars.distance(player) < 20:
            car.game_over()
            game_is_on = False

    if player.ycor() == 280:
        player.goto(0, -280)
        scoreboard.levelup()


screen.exitonclick()
