from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.setup(width=500, height=400)
user_ch = screen.textinput(title="make a bit", prompt='Which turtle is going to win '
                                                      '["red", "purple", "blue", "dark blue", "cyan", "black", "brown"]'
                                                      ',Enter the Color: ')
color = ["red", "purple", "blue", "dark blue", "cyan", "black", "brown"]
y = [-90, -60, -30, 0, 30, 60, 90]
all_turtle = []
is_on = True

for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(color[turtle_index])
    t.penup()
    t.goto(-230, y[turtle_index])
    all_turtle.append(t)


while is_on:
    for i in all_turtle:
        distance = rd.randint(0, 7)
        i.forward(distance)
        if i.xcor() > 220:
            is_on = False
            win_color = i.pencolor()
            if win_color == user_ch:
                print(f"you win! the {win_color} turtle is the  winner")
            else:
                print(f"you lost! the {win_color} turtle is the  winner")


screen.exitonclick()