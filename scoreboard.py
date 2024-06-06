from turtle import Turtle
ALIGN_MENT = "center"
FO_NT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)

        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN_MENT, font=FO_NT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!", align=ALIGN_MENT, font=FO_NT)

    def increase_Score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()