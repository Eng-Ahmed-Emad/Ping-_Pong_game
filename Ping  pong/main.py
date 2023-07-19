import time
from turtle import Turtle,Screen
from player1 import Player1
from player2 import Player2
from ball import Ball
from scoreboard import Scoreboard

from player1 import Player1
from player2 import Player2
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
Player_1=Player1()
Player_2=Player2()
ball=Ball()
scoreboard=Scoreboard()
screen.tracer()
screen.listen()
screen.onkeypress(Player_1.move_Player1_up,"w")
screen.onkeypress(Player_2.move_Player2_up,"Up")
screen.onkeypress(Player_1.move_Player1_down,"s")
screen.onkeypress(Player_2.move_Player2_down,"Down")


Game_is_on=True
while Game_is_on:
    screen.update()
    time.sleep(0.1)








screen.exitonclick()


























screen.exitonclick()
