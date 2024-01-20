from turtle import Turtle
import random as rd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car = []

    def generate_car(self):
        rand_ch = rd.randint(0,6)
        if rand_ch == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(1, 2)
            color = rd.choice(COLORS)
            car.color(color)
            y = rd.randint(-240, 240)
            car.goto(300, y)
            self.all_car.append(car)


    def move_car(self):
        for i in range(0, len(self.all_car)):
            self.all_car[i].back(STARTING_MOVE_DISTANCE)

    def game_over(self):
        end = Turtle()
        end.hideturtle()
        end.penup()
        end.color("black")
        end.goto(-150, 0)
        end.write("Game Over!!!", font= ("Courier", 24, "normal"))
