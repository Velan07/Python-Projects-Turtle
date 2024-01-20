from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time
s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game.")
s.tracer(0)
s.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    if food.distance(snake.head) < 15:
        food.refresh()
        snake.add_turtle(snake.turtles[-1].position())
        scoreboard.display()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.reset()

    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            scoreboard.reset_scoreboard()
            snake.reset()



s.exitonclick()