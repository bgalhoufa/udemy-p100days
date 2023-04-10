from turtle import Turtle

ALIGN = 'left'
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color('black')
        self.penup()
        self.goto(-270, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level {self.score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

