from turtle import Turtle



class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.score = 0
        self.penup()
        self.goto(-280, 260)
        self.ht()
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Level: {self.score}", font=("courier", 17, "bold"))

    def score_update(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 30, "bold" ))

    def win_game(self):
        self.goto(0, 30)
        self.write("You WIN!!!", align="center", font=("courier", 30, "bold"))
        self.goto(0, -20)
        self.write("Game Over", align="center", font=("courier", 20, "bold"))




