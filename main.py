import time
from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# Screen object / size / color / title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Keyboard movement binding
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Main loop to run the game
game_is_on = True
while game_is_on:
    # Updating the screen every 0.1 seconds
    screen.update()
    time.sleep(0.1)

    # Calling the attribute move from the Snake user-defined class
    snake.move()
    head_x = snake.head.xcor()
    heady = snake.head.ycor()

    # Detecting the collision between snake head and the food
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if head_x > 280 or head_x < - 280 or heady > 280 or heady < - 280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()