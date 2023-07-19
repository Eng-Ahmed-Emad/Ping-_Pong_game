from turtle import Turtle
UP=90
DOWN=180
class Player1:
    def __init__(self):
        self.create_player1()
    def create_player1(self):
            player1 = Turtle("square")
            player1.color("white")
            player1.shapesize(stretch_wid=5,stretch_len=1)
            player1.penup()
            player1.speed("fastest")
            player1.goto(-250,0)
            self.madrab1=player1

    def move_Player1_up(self):
        y=self.madrab1.ycor()
        y+=20
        self.madrab1.sety(y)

    def move_Player1_down(self):
        y = self.madrab1.ycor()
        y -= 20
        self.madrab1.sety(y)







