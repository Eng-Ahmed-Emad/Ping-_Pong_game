from turtle import Turtle

class Player2:
    def __init__(self):
        self.create_player2()
        self.madrab2
    def create_player2(self):
            player2 = Turtle("square")
            player2.color("white")
            player2.shapesize(stretch_wid=5, stretch_len=1)
            player2.penup()
            player2.speed("fastest")
            player2.goto(250,0)
            self.madrab2=player2

    def move_Player2_up(self):
        y=self.madrab2.ycor()
        y+=20
        self.madrab2.sety(y)

    def move_Player2_down(self):
        y = self.madrab2.ycor()
        y -= 20
        self.madrab2.sety(y)






