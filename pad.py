import turtle
from turtle import Turtle


class GamePad(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#B6BBC4")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(position)
        self.pace = 80

    def go_right(self):
        new_x = self.xcor() + self.pace
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - self.pace
        self.goto(new_x, self.ycor())

    def reset_pad(self):
        self.goto(0, -270)

