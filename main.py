import turtle
import tkinter
from turtle import Screen
from pad import GamePad
from ball import Ball
from wall import Bricks
import time
from scoreboard import Scoreboard
from lives import Lives

# Setting up the screen
screen = Screen()
screen.bgcolor("#0F0F0F")
screen.setup(width=1200, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# Class imports
pad = GamePad((0, -270))
ball = Ball((0, -247))
scoreboard = Scoreboard()
lives = Lives()
bricks = Bricks()

# Event listeners for keyboard keys
screen.listen()
screen.onkey(pad.go_right, "Right")
screen.onkey(pad.go_left, "Left")

game = True
while game:
    # This error exception deals with the turtle.Terminator error
    try:
        # Update screen on each time the app is launched
        time.sleep(ball.ball_speed)
        screen.update()
    except turtle.Terminator:
        break
        # This error exception handles the tkinter.TclError
    try:
        ball.move()
    except tkinter.TclError:
        break
        # Ball hits the top of the y-axis and bounces back through the y-axis
    if ball.ycor() > 290:
        ball.bounce_ball_ycor()

        # Ball hits any side of the x-axis and bounces back through the x-axis
    if ball.xcor() > 570 or ball.xcor() < -570:
        ball.bounce_ball_xcor()

        # On condition that ball touches the pad, it bounces upward and game goes oon
    if ball.distance(pad) < 59 and ball.ycor() < -245:
        ball.bounce_ball_ycor()

        # If ball misses the pad and touches the floor, player looses a life.
        # When all lives are lost, lives = 0 and its game over
    if ball.ycor() < -275:
        time.sleep(0.5)
        lives.loose_life()
        if lives.lives == 0:
            lives.clear()
            lives.write(f"Game Over!", align="center", font=("Courier", 17, "normal"))
            game = False
        ball.reset_ball()
        pad.reset_pad()
        # Checking the collision of ball with bricks
    for brick in bricks.bricks:
        if ball.distance(brick) < 55:
            brick.hideturtle()
            bricks.bricks.remove(brick)
            ball.bounce_ball_ycor()
            scoreboard.increase_score()
        scoreboard.update_highest_score()

screen.mainloop()
