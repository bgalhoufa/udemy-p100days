from turtle import Turtle
with open('ex_38_score.txt', mode='r') as fr:
    f_hscore = fr.read()



ALIGN = 'center'
FONT = ('Arial', 16, 'normal')
HIGH_SCORE = int(f_hscore)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE: {self.score} High Score: {self.high_score}', align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('ex_38_score.txt', mode='w') as fw:
                fw.write(f'{self.score}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



