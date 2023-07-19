from turtle import Turtle
POSTIONS=[(-250,0),(-250,20),(-250,40),(-250,60)]
UP=90
DOWN=180
class Player1:
    def __init__(self):
        self.segments=[]
        self.create_player1()
        self.head=self.segments[0]
    def create_player1(self):
        for p in POSTIONS:
            player1 = Turtle("square")
            player1.color("white")
            player1.shapesize(stretch_wid=6,stretch_len=2)
            player1.penup()
            player1.speed("fastest")
            player1.goto(p)
            self.segments.append(player1)

    def move_up(self):
        y = self.head.ycor()
        self.head.sety(y + 20)

    def move_down(self):
        y = self.head.ycor()
        self.head.sety(y - 20)







