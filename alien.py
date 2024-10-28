from turtle import Turtle
from bullet import Bullet
import random

class Alien(Turtle):
    def __init__(self, x, y, alien_type, points):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.points = points
        self.type = alien_type

        if self.type == "large":
            self.shape("assets/alien_large_resized.gif")
        elif self.type == "medium":
            self.shape("assets/alien_medium_resized.gif")
        else:
            self.type = "small"
            self.shape("assets/alien_small_resized.gif")


        self.move_speed = 3
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            x = self.xcor()
            x += self.move_speed
            self.setx(x)

            if x > 600:
                self.direction = "left"
                y = self.ycor()
                y -= 55
                self.sety(y)

        elif self.direction == "left":
            x = self.xcor()
            x -= self.move_speed
            self.setx(x)

            if x < -600:
                self.direction = "right"
                y = self.ycor()
                y -= 55
                self.sety(y)

    def destroy(self):
        self.hideturtle()

    def shoot(self):
        if self.type == 'large':
            bullet = Bullet()
            bullet.fire(self.position())
            return bullet
        return None







