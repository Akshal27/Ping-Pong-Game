from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
ball = Ball()
score = Score()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# paddle = Turtle("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	# Detect collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Detect collision with r_paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	# detect R paddle misses
	if ball.xcor() > 380:
		ball.reset_position()
		score.l_point()

	# detect L paddle misses
	if ball.xcor() < -380:
		ball.reset_position()
		score.r_point()

screen.exitonclick()
