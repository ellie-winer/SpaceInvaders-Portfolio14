from turtle import Turtle

class Shooter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("assets/shooter_resized.gif")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, -300)
        self.setheading(90)
        self.move_speed = 15
        self.direction = 1  # Positive for moving right, negative for moving left

    def move_left(self):
        self.direction = -1  # Move left
        self._move()

    def move_right(self):
        self.direction = 1  # Move right
        self._move()

    def _move(self):
        x = self.xcor()
        x += self.move_speed * self.direction

        if x > 660 or x < -660:
            self.direction *= -1

        self.setx(x)
