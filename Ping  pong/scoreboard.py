from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
POSITIONS=[(-80, 240),(90,240)]
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        for p in POSITIONS:
            self.score = 0
            self.color("white")
            self.penup()
            self.goto(p)
            self.hideturtle()
            self.update_scoreboard()
            self.speed(0)
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
