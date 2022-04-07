from turtle import Turtle


class Bar(Turtle):
    def __init__(self,x, y):
        super(Bar, self).__init__()
        self.shape("square")
        self.color("grey")
        self.penup()
        self.shapesize(4, 1)
        self.goto(x,y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)