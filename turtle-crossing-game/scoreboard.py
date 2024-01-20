from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-270, 250)
        self.write(f"LEVEL: {self.level}", font=FONT)


    def levelup(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT)

