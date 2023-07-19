from turtle import Turtle
class Ball:
    def __init__(self):
        self.create_ball()

    def create_ball(self):
        ball=Turtle("circle")
        ball.speed(0)
        ball.color("green")
        ball.penup()
        ball.goto(0, 0)