from turtle import Turtle
ALIGNMENT = "center"
FONT = "courier", 15, "normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.score = 0

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(f"GG's Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER! SCORE = {self.score}", False, align=ALIGNMENT, font=FONT)


