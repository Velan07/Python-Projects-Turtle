from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def forward():
    t.forward(10)


def backward():
    t.backward(10)


def right():
    t.right(10)


def left():
    t.left(10)


def space():
    t.up()


def enter():
    t.down()


def clear():
    t.clear()
    t.penup()
    t.home()
    t.down()


screen.listen()
screen.onkey(key="space", fun=space)
screen.onkey(clear, "c")
screen.onkey(key="n", fun=enter)
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.exitonclick()
