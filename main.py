import turtle
from random import randint
import time

# Değişkenler:
turtle_screen = turtle.Screen()
score = 0
time_left = 20
score_y_coordinate = turtle_screen.window_height() * 0.9 / 2
time_y_coordinate = turtle_screen.window_height() * 0.8 / 2
turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer2 = turtle.Turtle()
turtle_writer2.hideturtle()
image = "ghost.gif"

# Ekran:
def screen_setup():
    turtle_screen.bgcolor("#3a4163")
    turtle_screen.title("Catch the Ghost")

# Yazılar:
def scoreboard_setup():
    turtle_writer.penup()
    turtle_writer.color("white")
    turtle_writer.goto(0, score_y_coordinate)
    turtle_writer.write(f"Score: {score}", align="center", font=("Verdana", 15, "normal"))
    turtle_writer2.penup()
    turtle_writer2.color("orange")
    turtle_writer2.goto(0, time_y_coordinate)
    turtle_writer2.write(f"Time: {time_left}", align="center", font=("Verdana", 15, "normal"))

# Skoru arttır:
def increase_score(x,y):
    global score
    score = score + 1
    turtle_writer.clear()
    turtle_writer.write(f"Score: {score}", align="center", font=("Verdana", 15, "normal"))

# Geri sayım:
def countdown():
    global time_left
    if time_left > 0:
        turtle_writer2.clear()
        turtle_writer2.write(f"Time: {time_left}", align="center", font=("Verdana", 15, "normal"))
        time_left = time_left - 1
        turtle_screen.ontimer(countdown,1000)
    else:
        turtle_writer.clear()
        turtle_writer.write(f"Final Score: {score}", align="center", font=("Verdana", 15, "normal"))
        turtle_writer2.clear()
        turtle_writer2.write("Game Over!", align="center", font=("Verdana", 15, "normal"))

# Aksiyon:
def play_game():
    countdown()
    while time_left > 0:
        turtle_instance = turtle.Turtle()
        turtle_instance.hideturtle()
        turtle_instance.penup()
        turtle_screen.addshape(image)
        turtle_instance.shape(image)
        x = randint(-360, 360)
        y = randint(-300, 300)
        turtle_instance.goto(x,y)
        turtle_instance.showturtle()
        time.sleep(0.35)
        turtle_instance.onclick(increase_score)
    turtle_instance.hideturtle()

# Çalıştır:
screen_setup()
scoreboard_setup()
play_game()
turtle.mainloop()