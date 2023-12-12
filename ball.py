from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("#8E8FFA")
        self.shapesize(stretch_len=1.1, stretch_wid=1.1)
        self.penup()
        self.goto(position)
        self.move_x = 20
        self.move_y = 20
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_ball_ycor(self):
        self.move_y *= -1
        self.ball_speed *= .9
        self.move_y += 5

    def bounce_ball_xcor(self):
        self.move_x *= -1
        self.ball_speed *= .9
        self.move_x += 5

    def reset_ball(self):
        self.goto(0, -247)
        self.bounce_ball_ycor()



