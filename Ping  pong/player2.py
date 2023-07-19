from turtle import Turtle
POSTIONS=[(250,0),(250,20),(250,40),(250,60)]
class Player2:
    def __init__(self):
        self.segments=[]
        self.create_player2()
        self.head=self.segments[0]
    def create_player2(self):
        for p in POSTIONS:
            player2 = Turtle("square")
            player2.color("white")
            player2.shapesize(stretch_wid=6, stretch_len=2)
            player2.penup()
            player2.speed("fastest")
            player2.goto(p)
            self.segments.append(player2)

    def move_up(self):
        y = self.head.ycor()
        self.head.sety(y + 20)

    def move_down(self):
        y = self.head.ycor()
        self.head.sety(y - 20)






