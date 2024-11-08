from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.a = None
        self.segments = []
        self.create_snakes()
        self.head = self.segments[0]
        self.body = self.segments[1:]

    def create_snakes(self):
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        self.a = Turtle()
        self.a.penup()
        self.a.shape('circle')
        self.a.color('cyan')
        self.a.goto(position)
        self.segments.append(self.a)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
