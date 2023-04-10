from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 16, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'{self.score_left} : {self.score_right} ', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGN, font=FONT)

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()



