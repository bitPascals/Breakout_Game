import turtle
from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("#750E21")
        self.shapesize(stretch_len=5, stretch_wid=2)
        self.penup()
        self.goto(x_cor, y_cor)

        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.lower_wall = self.ycor() - 15


class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 250
        self.bricks = []
        self.create_paths()

    def create_path(self, y_cor):
        for i in range(-570, 570, 103):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_paths(self):
        for i in range(self.y_start, self.y_end, 43):
            self.create_path(i)











