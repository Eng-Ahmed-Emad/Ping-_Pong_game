import time
from turtle import Turtle,Screen
import time
from player1 import Player1
from player2 import Player2
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
Player_1 = Player1()
Player_2=Player2()
ball=Ball()
scoreboard=Scoreboard()
screen.onkey(Player_1.move_up,"Up")
screen.onkey(Player_1.move_down,"Down")
screen.onkey(Player_2.move_up,"w")
screen.onkey(Player_2.move_down,"s")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Player_1.move_up()
    Player_1.move_down()
    Player_2.move_up()
    Player_2.move_down()

























screen.exitonclick()
