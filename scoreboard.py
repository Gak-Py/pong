from turtle import Turtle
import time


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=("Futura", 30, "italic"))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("Futura", 30, "italic"))

    def get_point_l(self):
        self.l_score += 1
        self.goto(0, 0)
        self.write("Left Player WIN!", align="center", font=("Futura", 40, "italic"))
        time.sleep(3)
        self.write_score()

    def get_point_r(self):
        self.r_score += 1
        self.goto(0, 0)
        self.write("Right Player WIN!", align="center", font=("Futura", 40, "italic"))
        time.sleep(3)
        self.write_score()


