from turtle import Screen
import time
from player import Player
from score import Score
from cars import Car
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle cross")
screen.tracer(0)

player = Player()

car_list = []

for num in range(20):
    car = Car()
    car_list.append(car)


score = Score()

screen.listen()
screen.onkeypress(player.move_up, "Up")


game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    for car in car_list:
        car.car_move()

    for car in car_list:
        if car.xcor() < -290:
            car.create_car()
            car.goto(290, random.randrange(-250, 250, 30))

    if player.ycor() > 280:
        for car in car_list:
            car.speed_increase()
        player.next_level()
        score.score_update()

    for car in car_list:
        if player.distance(car) < 25:
            score.game_over()
            game_on = False

    if score.score == 10:
        score.win_game()
        game_on = False

screen.exitonclick()
