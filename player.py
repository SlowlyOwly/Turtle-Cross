from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE = 10


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def next_level(self):
        self.goto(STARTING_POSITION)