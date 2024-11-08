from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        # Inheriting from the turtle class
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        X = random.randint(-280, 280)
        Y = random.randint(-280, 280)
        self.goto(X,Y)

