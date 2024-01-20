from turtle import Turtle
import random as rd


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        x = rd.randint(-280, 280)
        y = rd.randint(-280, 280)
        self.goto(x, y)
