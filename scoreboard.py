from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        # self.goto(0,270)
        self.update_score()
        # self.goto(60,270)
        # self.update_high_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=(FONT))
        self.goto(100, 270)
        self.write(f"High Score: {self.high_score} ", False, align=ALIGNMENT, font=(FONT))

    def game_over(self):
        self.goto(0,0)
        # self.write("GAME OVER", False, align=ALIGNMENT, font=(FONT))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
