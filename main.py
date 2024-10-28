import turtle
import time
from shooter import Shooter
from alien import Alien
from bullet import Bullet
from scoreboard import Scoreboard
from images import resize_images
import random

resize_images()

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=1320, height=800)
screen.tracer(0)
screen.bgpic("assets/space_bg_resized.gif")

screen.register_shape("assets/shooter_resized.gif")
screen.register_shape("assets/alien_large_resized.gif")
screen.register_shape("assets/alien_medium_resized.gif")
screen.register_shape("assets/alien_small_resized.gif")
screen.register_shape("assets/explosion_resized.gif")

shooter = Shooter()
scoreboard = Scoreboard()

aliens = []
rows = 5
columns = 11
alien_start_y = 300
alien_gap_x = 60
alien_gap_y = 70

bullets = []
last_bullet_time = 0
last_shoot_time = 0

def create_aliens():
    global aliens
    aliens.clear()
    for row in range(rows):
        for col in range(columns):
            alien_x = -350 + (col * alien_gap_x)
            alien_y = alien_start_y - (row * alien_gap_y)
            if row in [0, 1]:
                alien_type = "large"
                points = 30
            elif row in [2, 3]:
                alien_type = "medium"
                points = 20
            else:
                alien_type = "small"
                points = 10

            alien = Alien(alien_x, alien_y, alien_type, points)
            aliens.append(alien)

create_aliens()

game_over_display = turtle.Turtle()
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, -350)

win_display = turtle.Turtle()
win_display.color("green")
win_display.penup()
win_display.hideturtle()
win_display.goto(0, -350)

instructions_display = turtle.Turtle()
instructions_display.color("white")
instructions_display.penup()
instructions_display.hideturtle()
instructions_display.goto(0, 50)

def show_instructions():
    instructions_display.clear()
    instructions_display.write("Use arrow keys to move left and right and the space bar to shoot\n\nPress 'S' to start", align="center", font=("Courier", 24, "normal"))

def start_game():
    instructions_display.clear()
    main_loop()

def reset_game():
    global bullets, aliens, last_bullet_time
    for alien in aliens:
        alien.hideturtle()
        alien.clear()
    bullets.clear()
    game_over_display.clear()
    win_display.clear()
    scoreboard.clear()
    scoreboard.score = 0
    scoreboard.lives = 3
    scoreboard.update_score()
    scoreboard.goto(0, 350)
    last_bullet_time = 0
    shooter.goto(0, -300)
    create_aliens()

def display_game_over():
    game_over_display.write("Game Over!\nPress 'P' to Play Again", align="center", font=("Courier", 24, "normal"))

def display_win():
    win_display.write("You Win!\nPress 'P' to Play Again", align="center", font=("Courier", 24, "normal"))

def play_again():
    reset_game()
    main_loop()

def is_collision(t1, t2):
    return t1.distance(t2) < 25

def fire_bullet():
    global last_bullet_time
    current_time = time.time()
    if current_time - last_bullet_time >=1:
        bullet = Bullet(color='blue')
        bullet.fire(shooter.position(), direction="up")
        bullets.append(bullet)
        last_bullet_time = current_time

def alien_shoot():
    global last_shoot_time
    current_time = time.time()
    if current_time - last_shoot_time >= 3:
        if aliens:
            random_alien = random.choice([alien for alien in aliens if alien.type == "large"])
            bullet = Bullet(color="red")
            bullet.fire(random_alien.position(), direction="down")
            bullets.append(bullet)
        last_shoot_time = current_time

explosion_display = turtle.Turtle()
explosion_display.penup()
explosion_display.hideturtle()

def show_explosion(position):
    explosion_display.goto(position)
    explosion_display.shape("assets/explosion_resized.gif")
    explosion_display.showturtle()
    screen.update()
    time.sleep(0.5)
    explosion_display.hideturtle()

def main_loop():
    global game_is_on
    game_is_on = True
    while game_is_on:
        screen.update()
        screen.listen()
        screen.onkeypress(shooter.move_left, "Left")
        screen.onkeypress(shooter.move_right, "Right")
        screen.onkeypress(fire_bullet, "space")

        alien_shoot()

        for alien in aliens:
            alien.move()
            if alien.ycor() < -230:
                game_is_on = False
                display_game_over()
                break

        for bullet in bullets:
            bullet.move()
            if bullet.color()[0] == "blue":
                for alien in aliens:
                    if bullet.active and is_collision(bullet, alien):
                        bullet.hideturtle()
                        bullet.active = False
                        alien.destroy()
                        aliens.remove(alien)
                        scoreboard.add_points(alien.points)

            if bullet.color()[0] == "red":
                if bullet.active and is_collision(bullet, shooter):
                    bullet.hideturtle()
                    bullet.active = False
                    time.sleep(1)
                    shooter.hideturtle()
                    show_explosion(shooter.position())
                    scoreboard.lives -= 1
                    scoreboard.update_score()
                    screen.update()
                    shooter.showturtle()
                    time.sleep(1)
                    if scoreboard.lives <= 0:
                        game_is_on = False
                        display_game_over()
                elif bullet.ycor() < shooter.ycor() - 25:
                    bullet.hideturtle()
                    bullet.active = False

            for other_bullet in bullets:
                if bullet.active and other_bullet.active and bullet.color()[0] == "blue" and other_bullet.color()[
                    0] == "red":
                    if is_collision(bullet, other_bullet):
                        bullet.hideturtle()
                        bullet.active = False
                        other_bullet.hideturtle()
                        other_bullet.active = False

        if not aliens:
            game_is_on = False
            display_win()

        bullets[:] = [bullet for bullet in bullets if bullet.active]

    screen.listen()
    screen.onkeypress(play_again, "p")

show_instructions()
screen.listen()
screen.onkeypress(start_game, "s")
screen.mainloop()

