from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.snake_up, "w")
screen.onkey(snake.snake_down, "s")
screen.onkey(snake.snake_left, "a")
screen.onkey(snake.snake_right, "d")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.moving_forward()

    #Detect contact with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    #Detect collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        # scoreboard.game_over()
        # for block in range(0,len(snake.blocks)):
        #     snake.blocks[block].goto(1000,1000)
        # game_on = False
        scoreboard.reset()
        snake.reset()

        # snake = Snake( )

    #Detect collision with tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
