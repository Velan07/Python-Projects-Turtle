from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create()
        self.head = self.turtles[0]

    def create(self):
        x = 0
        for i in range(0, 3):
            t = Turtle()
            t.penup()
            t.color("white")
            t.shape("square")
            t.setpos(x, 0)
            x -= 20
            self.turtles.append(t)

    def add_turtle(self, position):
        t = Turtle()
        t.color("white")
        t.shape("square")
        t.penup()
        t.setpos(position)
        self.turtles.append(t)

    def reset(self):
        for snake in self.turtles:
            snake.goto(1000, 1000)
        self.turtles.clear()
        self.create()
        self.head = self.turtles[0]


    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle - 1].xcor()
            new_y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.turtles[0].setheading(RIGHT)
