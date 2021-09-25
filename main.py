from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from net import Net
from score import Score
import time
#screen setup

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=400)
screen.title('Ping_Pong')
net = Net()
screen.tracer(0)
y=net.ycor()
net.move_forward(0)
net.move_forward(200)
#create paddle

score = Score()
right_paddle = Paddle(380, 0)
left_paddle = Paddle(-380, 0)
ball = Ball()





screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
game_is_on = True


while game_is_on:

    time.sleep(0.025)
    screen.update()
    ball.ball_go()


    if ball.ycor() > 180 or ball.ycor() < -180:
        ball.bounce()



    if ball.distance(right_paddle) <50 or ball.distance(left_paddle) <50:
        ball.paddle_bounce()


    if ball.xcor()>380:
        ball.reset_ball()
        score.goal_r()

    if ball.xcor()<-380:
        ball.reset_ball()
        score.goal_l()






screen.exitonclick()
