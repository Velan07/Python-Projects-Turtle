from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"Score : {self.score}  HighScore : {self.high_score}", align="center", font=('Arial', 20, 'bold'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  HighScore : {self.high_score}", align="center", font=('Arial', 20, 'bold'))

    def reset_scoreboard(self):
        if self.score >= self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def display(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}  HighScore : {self.high_score}", align="center", font=('Arial', 20, 'bold'))

