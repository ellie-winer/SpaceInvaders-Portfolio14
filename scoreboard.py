from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 350)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}           Lives: {self.lives}", align="center", font=("Arial", 24, "normal"))

    def add_points(self, points):
        self.score += points
        self.update_score()

    def lose_life(self):
        self.lives -= 1
        self.update_score()