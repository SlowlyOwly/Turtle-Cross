from turtle import Turtle
import random

COLORS = ["green", "purple", "orange", "blue", "red", "grey"]


class Car(Turtle):

    def __init__(self):
        super(Car, self).__init__()
        self.car_speed = -5
        self.create_car()
        self.car_move()

    def create_car(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.seth(180)
        self.shape("square")
        self.shapesize(1, 2)
        self.goto(random.randrange(-240, 290, 20), random.randrange(-240, 250, 30))

    def car_move(self):
        new_x = self.xcor() + self.car_speed
        self.goto(new_x, self.ycor())

    def speed_increase(self):
        self.car_speed -= 2


