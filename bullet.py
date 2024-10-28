from turtle import Turtle

class Bullet(Turtle):
    def __init__(self, color='red'):
        super().__init__()
        self.shape("triangle")
        self.color(color)
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.hideturtle()
        self.bullet_speed_up = 30
        self.bullet_speed_down = 20
        self.active = False

    def fire(self, position, direction="up"):
        if not self.active:
            self.goto(position)
            self.showturtle()
            self.active = True
            if direction == "down":
                self.setheading(270)
            else:
                self.setheading(90)

    def move(self):
        if self.active:
            y = self.ycor()
            if self.heading() == 90:
                y += self.bullet_speed_up
            elif self.heading() == 270:
                y -= self.bullet_speed_down
            self.sety(y)

            if y > 275 or y < -400:
                self.hideturtle()
                self.active = False

